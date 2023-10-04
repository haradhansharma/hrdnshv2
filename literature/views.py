import json
from pprint import pprint
import re
import time
import uuid
from django.conf import settings
from django.forms import formset_factory, inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
import openai
from home.decorators import superuser_required
from literature.forms import IdeaUtilizationForm, OutlineForm, StoryRawForm, StoryForm
from literature.models import Story, StoryOutline, StoryRaw
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages as msg
from django.contrib.auth.decorators import login_required

@superuser_required
def delete_idea(request, pk):
    story_raw = get_object_or_404(StoryRaw, pk=pk)
    idea = story_raw.idea
    idea.delete()
    
    return HttpResponseRedirect(reverse('literature:home'))

@login_required
@superuser_required
def home(request):
    q = request.GET.get('q')

    if q is not None:
        if len(q) < 3:
            msg.warning(request, 'At least 3 character required!')
            return HttpResponseRedirect(request.path)
        story_raws =  StoryRaw.objects.filter(Q(idea__idea__icontains=q) | Q(title__icontains=q) | Q(genre__icontains=q) | Q(type__icontains=q)).order_by('-created')
    else:    
        story_raws = StoryRaw.objects.all().order_by('-created')
    
    form = IdeaUtilizationForm()   
     
    paginator = Paginator(story_raws, 10)
    page = request.GET.get('page')     
    
    try:
        story_raws = paginator.page(page)
    except PageNotAnInteger :
        story_raws = paginator.page(1)
    except EmptyPage:
        story_raws = paginator.page(paginator.num_pages)  
        
        
    if request.method == 'POST':
        form = IdeaUtilizationForm(request.POST)  
        if form.is_valid():
            idea  = form.save(commit=False)
            
            prompt = {
                'prompt': f'Based on the idea above please suggest the following in the format below:\n\n'
                        f'Title:"""insert title here. Avoid "\n" character instead use comma""", '
                        f'Genre:"""insert genre here. Avoid "\n" character instead use comma""", '
                        f'Type:"""insert type here. Avoid "\n" character instead use comma""", '
                        f'Character:"""insert character here. Avoid "\n" character instead use comma""", '
                        f'Setting:"""insert settings here. Avoid "\n" character instead use comma""", '
                        f'Conflict:"""insert conflict here. Avoid "\n" character instead use comma""", '
                        f'Tone:"""insert tone here. Avoid "\n" character instead use comma""", '
                        f'Style:"""insert style here. Avoid "\n" character instead use comma""", '
                        f'Topic:"""inset topic here. Avoid "\n" character instead use comma""", '
                        f'Purpose:"""insert purpose here. Avoid "\n" character instead use comma""", '
                        f'Audience:"""insert audience here. Avoid "\n" character instead use comma""", '
                        f'Key points:"""insert key points here. Avoid "\n" character instead use comma""", '
                        f'Theme:"""insert theme here. Avoid "\n" character instead use comma""", '
                        f'Mood:"""insert mood here. Avoid "\n" character instead use comma""", '
                        f'Species:"""insert species here. Avoid "\n" character instead use comma""", '
                        f'Quest:"""insert quest here. Avoid "\n" character instead use comma""", '                        
            }

            messages = []

            messages.append({'role': 'system', 'content': "You are a helpful assistant focused on suggesting appropriate parameters for writing literature. Your duty is to perform deep analysis and provide relevant suggestions in creative manners."})
            messages.append({'role': 'user', 'content': f"This is the plot:\n\n'''{form.cleaned_data['idea']}'''"})
            messages.append({'role': 'user', 'content': f"{prompt}"})  # Send prompt as a regular user message

            response = generate_from_chatgpt(messages, temp=1)
            print('response_____________________')
            pprint(response)
                  
            try:
                # Split the response text into lines
                response_lines = response.split('\n')
                
                print('response_lines____________________')
                print(response_lines)
                
                # Initialize an empty dictionary to store the structured data
                structured_data = {}

                # Loop through the response lines and populate the dictionary
                for line in response_lines:
                    try:
                        print('line_________________________')
                        print(line)
                        
                        key, value = line.split(': ', 1)
                        print('key, value__________________________________________')
                        print(key, value)
                        
                        structured_data[key] = value
                    except Exception as e:
                        print(f"problem in unpack {e}")
                        continue
                print('structured_data__________________________________')
                print(structured_data)
                
                # Convert the structured data into JSON format
                
                json_data = json.dumps(structured_data, indent=4)
                print('json_data_____________________')
                print(json_data)
                
                idea.idea_response = json_data
                idea.save()
                
                data = json.loads(idea.idea_response)
                
                print('data________________________________')
                print(data)
                
                
                story_raw = idea.storyraw
                
                story_raw.title= data.get('Title')
                story_raw.tenre= data.get('Genre')
                story_raw.type= data.get('Type')
                story_raw.character= data.get('Character')
                story_raw.setting= data.get('Setting')
                story_raw.conflict= data.get('Conflict')
                story_raw.tone= data.get('Tone')
                story_raw.style= data.get('Style')
                story_raw.topic= data.get('Topic')
                story_raw.purpose= data.get('Purpose')
                story_raw.audience= data.get('Audience')
                story_raw.key_points= data.get('Key points')
                story_raw.theme= data.get('Theme')
                story_raw.mood= data.get('Mood')
                story_raw.species= data.get('Species')
                story_raw.quest= data.get('Quest')
                
                story_raw.save()
                
            except Exception as e:
                print(f"the proem occured due to: {e}")
                raise ValueError(f'imappropriate value from response:{e}')  
            
            
            return HttpResponseRedirect(reverse('literature:generate_story_title_and_outline', args=[int(story_raw.pk)]))
        
    
    context = {
        'story_raws' : story_raws,
        'form' : form
    }
    
    
    return render(request, 'literature/home.html', context)
    
@login_required
@superuser_required
def generate_from_chatgpt(messages, temp):
    openai.api_key = settings.OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=temp
    )
    return response['choices'][0]['message']['content']


@login_required
@superuser_required
def generate_story_title_and_outline(request, pk):
    story_raw_id = pk  
    
    story_raw_obj = get_object_or_404(StoryRaw, pk=story_raw_id)
        
    idea_res = json.loads(story_raw_obj.idea.idea_response)
    # idea_res = story_raw_obj.idea.idea_response
    
    
    poem_indicator = ['poem', 'Poem', 'Poetry']    
    if request.method == 'POST':
            
        story_raw_form = StoryRawForm(request.POST, instance = story_raw_obj)
            
        if story_raw_form.is_valid():
            
            cleaned_data = story_raw_form.cleaned_data
            
            genre = cleaned_data.get('genre')
            character = cleaned_data.get('character')
            type = cleaned_data.get('type')
            setting = cleaned_data.get('setting')
            conflict = cleaned_data.get('conflict')
            tone = cleaned_data.get('tone')
            style = cleaned_data.get('style')
            topic = cleaned_data.get('topic')
            purpose = cleaned_data.get('purpose')
            audience = cleaned_data.get('audience')
            key_points = cleaned_data.get('key_points')
            theme = cleaned_data.get('theme')
            mood = cleaned_data.get('mood')
            rhyme_meter = cleaned_data.get('rhyme_meter')
            imagery_symbolism = cleaned_data.get('imagery_symbolism')
            characters = cleaned_data.get('characters')
            scenes = cleaned_data.get('scenes')
            dialogue = cleaned_data.get('dialogue')
            world_building = cleaned_data.get('world_building')
            species = cleaned_data.get('species')
            quest = cleaned_data.get('quest')
            crime = cleaned_data.get('crime')
            detective = cleaned_data.get('detective')
            clues_red_herrings = cleaned_data.get('clues_red_herrings')
            historical_figures = cleaned_data.get('historical_figures')
            character_arcs = cleaned_data.get('character_arcs')
            meet_cute = cleaned_data.get('meet_cute')
            obstacles_to_love = cleaned_data.get('obstacles_to_love')
            resolution = cleaned_data.get('resolution')
            atmosphere = cleaned_data.get('atmosphere')
            threat_entity = cleaned_data.get('threat_entity')
            suspense_dread = cleaned_data.get('suspense_dread')
            age_group = cleaned_data.get('age_group')
            moral_lesson = cleaned_data.get('moral_lesson')
            
            
            messages = []

            system_message = f'You are a helpful assistant that writes literature in the {genre} genre. Your task is to provide segmented Outlines with peoper analysis to be a best {genre}. Each segment should follow the format: "Segment: [Signment Indicator]\n\n" \n"Outline: [Outline List]\n\n".'

            user_messages = [
                {'role': 'user', 'content': f"Genre: {genre}"},
                {'role': 'user', 'content': f"Type: {type}"}
            ]

            parameters = [
                ('Character', character),
                ('Setting', setting),
                ('Conflict', conflict),
                ('Tone', tone),
                ('Style', style),
                ('Topic', topic),
                ('Purpose', purpose),
                ('Audience', audience),
                ('Key points', key_points),
                ('Theme', theme),
                ('Mood', mood),
                ('Rhyme_meter', rhyme_meter if rhyme_meter or type in poem_indicator or genre in poem_indicator else None),
                ('Imagery symbolism', imagery_symbolism),
                ('Characters', characters),
                ('Scenes', scenes),
                ('Dialogue', dialogue),
                ('World building', world_building),
                ('Species', species),
                ('Quest', quest),
                ('Crime', crime),
                ('Detective', detective),
                ('Clues Red Herrings', clues_red_herrings),
                ('Historical figures', historical_figures),
                ('Character Arcs', character_arcs),
                ('Meet Cute', meet_cute),
                ('Obstacles to love', obstacles_to_love),
                ('Resolution', resolution),
                ('Atmosphere', atmosphere if genre == 'Horror' else None),
                ('Threat Entity', threat_entity if genre == 'Horror' else None),
                ('Suspense Dread', suspense_dread if genre == 'Horror' else None),
                ('Age Group', age_group if genre == 'Children Literature' else None),
                ('Moral lesson', moral_lesson if genre == 'Children Literature' else None)
            ]

            # Add system message
            messages.append({'role': 'system', 'content': system_message})

            # Add user messages
            messages.extend(user_messages)

            # Add parameter-specific user messages
            for param_name, param_value in parameters:
                if param_value:
                    messages.append({'role': 'user', 'content': f"{param_name}: {param_value}"})                           
            
            
            story_raw = story_raw_form.save()            
            story_raw_obj = story_raw
            
            # Convert messages to the required format
            chat_messages = [{'role': message['role'], 'content': message['content']} for message in messages]   
   
            if 'genarate_outline' in request.POST or 'regenarate_outline' in request.POST : 
                print('connecting_________________________')                
                generated_outline = generate_from_chatgpt(chat_messages, temp = 1.2)    
                pprint(generated_outline)
                # Use regular expression to split the response text into segments
                # Use regular expression to extract segments and outlines
                # Define a list of regex patterns to try
                regex_patterns = [
                    r'Segment: (.*?)\n\nOutline:\n(.*?)\n\n',
                    r'Segment: (.*?)\nOutline:(.*?)\n\n',
                    r'Segment\s*:\s*(.*?)\s*Outline\s*:\s*(.*?)\s*',
                    r'Segment:(.*?)Outline:(.*?)\s*',
                    r'Segment:(.*?)Outline:(.*?)'
                ]

                segmented_data = []

                # Try each regex pattern until a match is found
                for pattern in regex_patterns:
                    segmented_data = re.findall(pattern, generated_outline, re.DOTALL)
                    if len(segmented_data) > 0:
                        break  # Exit the loop if a match is found
                print('segmented_data____________________')
                print(segmented_data)
                

                # Create a list of dictionaries
                segmented_outlines_list = [{'segment': segment, 'outline': outline.strip()} for segment, outline in segmented_data]
                # segmented_outlines_list = [{'segment': segment.strip(), 'outline': outline.strip()} for segment, outline in segmented_data]

                 
                print('segmented_outlines_list:_____________')   
                print(segmented_outlines_list)
             
                
                                
                if story_raw.type in poem_indicator or story_raw.genre in poem_indicator:     
                    print('for poem________________')      
                    prepeared_segment = ''
                    for item in segmented_outlines_list:
                        prepeared_segment += f"Segment: {item.get('segment')}\nOutline:\n {item.get('outline')}\n\n"
                          
                    outline_objects = [StoryOutline(story_raw=story_raw, segment=prepeared_segment)]
                else:          
                    print('for others_______________________________________________')         
                    outline_objects = [StoryOutline(story_raw=story_raw, segment=f"Segment: {item.get('segment')}\nOutline:\n {item.get('outline')}\n\n") for item in segmented_outlines_list]
                    print('outline_objects:_____________________')
                    print(outline_objects)
                    
                dele = StoryOutline.objects.filter(story_raw__pk = story_raw_id).delete()   
                print(f'{dele}___________________')
                StoryOutline.objects.bulk_create(outline_objects)
            
                return HttpResponseRedirect(reverse('literature:story_outline', args=[int(story_raw.pk)]))            
        return HttpResponseRedirect(reverse('literature:generate_story_title_and_outline', args=[int(story_raw.pk)]))
            
    else:     
        story_raw_form = StoryRawForm(instance = story_raw_obj)
        

    return render(
        request, 
        'literature/create_story_home.html', 
        {
        'form': story_raw_form, 
        'story_raw_id':story_raw_id, 
        'idea_res' : idea_res,
        'story_raw_obj' : story_raw_obj
        }
        )
from django.db import models

@login_required
@superuser_required
def story_outline(request, pk):
 
    story_raw = get_object_or_404(StoryRaw, pk=pk)

    StoryOutlineFormSet = inlineformset_factory(StoryRaw, StoryOutline, fk_name='story_raw', form = OutlineForm, extra=0)
    
    outline_fromset = StoryOutlineFormSet(request.POST or None, prefix='story_outline', instance=story_raw)   
    
    for form in outline_fromset:  
        form.fields['segment'].label = mark_safe(form.instance.segment.split('\n')[0]) if form.instance.segment is not None else ''
        form.fields['DELETE'].help_text = "Check this box to delete this item. The operation can not be undone!"
    
    if request.method == 'POST':
  
        outline_fromset = StoryOutlineFormSet(request.POST, prefix='story_outline', instance=story_raw) 
        
        response_type = dict()  
        
        if outline_fromset.is_valid():
            forms_to_delete = []       
            for form in outline_fromset:                
                id = form.cleaned_data['id']               
                delete = form.cleaned_data['DELETE'] 
                segment = form.cleaned_data['segment']  
                line_response = form.cleaned_data['line_response']  
                
                
                response_type.update({id:line_response})            
                
                if delete:                    
                    StoryOutline.objects.get(id = id).delete()
                    forms_to_delete.append(form)
            
            for form in forms_to_delete:
                outline_fromset.forms.remove(form)
                
            outline_fromset.save()   
          
             
            if 'save_and_stay' in request.POST:       
           
                return HttpResponseRedirect(reverse('literature:story_outline', args=[int(story_raw.pk)])) 
       
            if not 'save_and_stay' in request.POST: 
                            
                parameters = []
                skip_field = ['idea', 'created', 'updated' ]
                for field in story_raw._meta.get_fields():
                    if isinstance(field, models.Field):
                        name = field.name
                        if name not in skip_field:
                            field_value = getattr(story_raw, field.attname, '')                        
                            parameters.append((name, field_value))

                # Filter out fields with None values
                skip_value = ['', None, 'N/A', 'NA']
                parameters = [(name, value) for name, value in parameters if value not in skip_value]   
                
                para_str = ''
                
                for name, value in parameters:
                    para_str += f"{name}: {value}\n"               
                
                outline_messages = [{'role': 'system', 'content': f'You are a helpful assistant with a unique creativity and writing style that creates {story_raw.genre} literature in form of {story_raw.type} with nice conclusion, taking into account the following parameters:\n\n{para_str}'}]             
                
                
                outline_res = ''
                outline_segments = dict()
                outlines = story_raw.storyoutline.all()            
                
                id_to_delete = []
                for outline in outlines:
                    if not outline.story_raw.has_story or 'regenarate_story' in request.POST:
                        outline_res += f'{outline.segment}\n\n'
                        outline_segments.update({outline : outline.segment})
                        id_to_delete.append(outline.id)
                    
             
                
                outline_messages.append({'role': 'assistant', 'content': f'Here are the outline of the plot:\n\n{outline_res}.'})                
                outline_messages.append({'role': 'user', 'content': f'Excellent! Please focus on creating the {story_raw.type} while following each chapter. Do not include the provided outline in the writings, and there is no need to ask for additional information.'})

                
                story_objects = []            
            
                segment_part = []
                for outline, segment in outline_segments.items():   
                    
                    
                    if response_type[outline]:  #if line wise response true
                        segment_part.clear()  
                      
                        for line in segment.split('\n'):                          
                            if "Segment:" not in line and "Outline:" not in line:                              
                                segment_part.append({'role': 'user', 'content': f"Please write the following section of the plot only in creative manner:\n\n{line}.\n\nI'll be providing each part one by one if there is pending."})
                                outline_messages.extend(segment_part)  
                                segment_response = generate_from_chatgpt(outline_messages, temp = 0.8)                    
                                story_objects.append(Story(story_outline=outline, sigment_story=segment_response))  
                                
                                time.sleep(5) 
                    else: 
                        segment_part.clear()  
                        print('noooooooo lined response__________________')                   
                        segment_part.append({'role': 'user', 'content': f"Please write the following section of the plot only in creative manner:\n\n{segment}.\n\nI'll be providing each part one by one if there is pending."})
                    
                        outline_messages.extend(segment_part)   
               
                        
                        segment_response = generate_from_chatgpt(outline_messages, temp = 1.0)                    
                        story_objects.append(Story(story_outline=outline, sigment_story=segment_response))  
                        
                        time.sleep(5)
                                
                if len(story_objects) > 0:
                    Story.objects.filter(story_outline_id__in = id_to_delete).delete()
                    Story.objects.bulk_create(story_objects)
            
            return HttpResponseRedirect(reverse('literature:story', args=[int(story_raw.pk)]))
    
    context = {     
        'formset' : outline_fromset,
        'story_raw' : story_raw
    }
    
    
    return render(request, 'literature/story_raw_outline.html', context)

from django.utils.safestring import mark_safe

@login_required
@superuser_required
def story(request, pk):
    story_raw = get_object_or_404(StoryRaw, pk=pk)
    story_outlines = story_raw.storyoutline.values_list('pk', flat=True)
    
    StoryFormSet = formset_factory(StoryForm, extra=0)
    
    queryset = Story.objects.filter(story_outline_id__in=story_outlines)
    
    if request.method == 'POST':
        story_formset = StoryFormSet(request.POST, prefix='story-segment')
        if story_formset.is_valid():
            for form, instance in zip(story_formset, queryset):
                if form.has_changed():  # Check if the form data has changed
                    sigment_story = form.cleaned_data['sigment_story']
                    instance.sigment_story = sigment_story
                    instance.save()
            return HttpResponseRedirect(reverse_lazy('literature:story', args=[int(story_raw.pk)]))
    else:
        form_data_list = [
            {
                'sigment_story': item.sigment_story,
                'field_label': item.story_outline.segment,
                'story_outline': item.story_outline,
                'id': item.id,
                'story_outline_id': item.story_outline.id
            }
            for item in queryset
        ]
        
        story_formset = StoryFormSet(prefix='story-segment', initial=form_data_list)
        
        for form in story_formset:
            form.fields['sigment_story'].label = mark_safe(form.initial['field_label'].replace('\n', '<br>'))
    
    context = {
        'story_raw': story_raw,
        'formset': story_formset
    }
    
    return render(request, 'literature/story.html', context)