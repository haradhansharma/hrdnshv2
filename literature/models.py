import uuid
from django.db import models
from django.urls import reverse

class IdeaUtilization(models.Model):
    idea = models.TextField(verbose_name="Describe your idea in maximum 500 characters", help_text="The place is to describe ideas to get best parameters to write literature. Primarily system will suggest title, genre, type, main charecter, settings, conflict, tone, style, topic,purpose, audience, keypoints, theme, mood, species quest.")
    idea_response = models.JSONField(null=True, blank=True)

class StoryRaw(models.Model):
    GENRE_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Poetry', 'Poetry'),
        ('Fantasy', 'Fantasy'),
        ('Mystery', 'Mystery'),
        ('Historical Fiction', 'Historical Fiction'),
        ('Science Fiction', 'Science Fiction'),      
        ('Realistic  Fiction', 'Realistic  Fiction'),       
        ('Dystopian  Fiction', 'Dystopian  Fiction'),       
        

          
        ('Romance', 'Romance'),
        ('Horror', 'Horror'),    
        ('Memoir', 'Memoir'),
        ('Satire', 'Satire'),
        ('Fable', 'Fable'),
        ('Tragedy', 'Tragedy'),
        ('Suspense', 'Suspense'),
        ('Thriller', 'Thriller'),
        ('Political Thriller', 'Political Thriller'),
        ('Drama', 'Drama'),
        
        
        
        
        
        
        
        ('Social Realism', 'Social Realism'),
        
       
        
        ('Children Literature', 'Children Literature'),
    ]  
    
    idea = models.OneToOneField(IdeaUtilization, on_delete=models.CASCADE, primary_key=True, editable=False)
    
    title = models.CharField(
        max_length=250,    
        blank=True,
        null=True,    
        help_text="It an keep blank to add from response of chatGPT"
    )
    
    
    genre = models.CharField(
        blank=True,
        null=True,
        max_length=250,
        choices=GENRE_CHOICES,
        help_text="Select the genre of your story."
    )
    
    type = models.CharField(
        blank=True,
        null=True,
        max_length=200,        
        help_text="The type of your literature (e.g., 'Essay, Drama, Poem, Story, Novel, Short Story, Epic')."
    )
    
    character = models.TextField(
  
        blank=True,
        null=True,
        help_text="The main character in your story (e.g., 'Detective John Smith')."
    )
    setting = models.TextField(
    
        blank=True,
        null=True,
        help_text="The primary setting of your story. An specific time, session or location (e.g., 'future, Victorian London')."
    )
    conflict = models.TextField(
        blank=True,
        null=True,
        help_text="Describe the central conflict or problem in your story."
    )
    tone = models.TextField(
   
        blank=True,
        null=True,
        help_text="The tone of your story (e.g., 'Classical, Baroque, Victorian, Realistic, Modernist, Surrealistic, Naturalistic, Absurdist, Epic, Tragic, Mysterious', 'Romantic')."
    )
    style = models.TextField(
        blank=True,
        null=True,
        help_text="The narrative style (e.g., 'First-person', 'Third-person, Third-Person Limited, Third-Person Omniscient, Second-Person, Epistolary, Stream of Consciousness, Multi-Person, Unreliable Narrator, Framed Narrative')."
    )
    topic = models.TextField(
       
        blank=True,
        null=True,
        help_text="Specify the topic or subject of your non-fiction story (e.g., 'History of Space Exploration')."
    )
    purpose = models.TextField(
        
        blank=True,
        null=True,
        help_text="Describe the purpose of your non-fiction story (e.g., 'Inform readers about scientific discoveries')."
    )
    audience = models.TextField(

        blank=True,
        null=True,
        help_text="Identify the target audience for your non-fiction story (e.g., 'General readers', 'Experts')."
    )
    
    key_points = models.TextField(
        blank=True,
        null=True,
        help_text="List key points, facts, or information you want in your non-fiction story."
    )
    
    theme = models.TextField(       
        blank=True,
        null=True,
        help_text="The central theme of your story (e.g., 'Love', 'Adventure, Conflict, Identity, Coming of Age, Power and Corruption, Justice and Injustice, Isolation and Alienation, Nature vs. Nurture, Freedom and Oppression, Death and Mortality, Friendship, Ambition and Desire, Society and Social Change, Betrayal, Memory and Nostalgia, Hope and Despair, Technology and Progress, Family, Survival, Fate and Free Will, Redemption')."
    )
    mood = models.TextField(

        blank=True,
        null=True,
        help_text="The mood or emotional atmosphere of your story (e.g., 'Joyful', 'Melancholic, Eerie, Tense, Gloomy, Whimsical, Nostalgic, Serene, Horrific, Humorous, Surreal, Romantic, Mysterious, Empowering, Regretful, Hopeful')."
    )
    rhyme_meter = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Specify the rhyme scheme or meter for your poem (e.g., 'ABAB', 'Haiku, Sonnet, Limerick, Villanelle, Pantoum, Sestina, Tanka, Ghazal, Ode, Ballad, Triolet')."
    )
    imagery_symbolism = models.TextField(
        blank=True,
        null=True,
        help_text="Describe any specific imagery or symbolism you want in your poem."
    )
    characters = models.TextField(
        blank=True,
        null=True,
        help_text="Describe the main characters in your drama (e.g., 'Character A: Ambitious detective')."
    )
    scenes = models.TextField(
        blank=True,
        null=True,
        help_text="Outline key scenes or settings in your drama."
    )
    dialogue = models.TextField(
        blank=True,
        null=True,
        help_text="Provide dialogue prompts for important interactions in your drama."
    )
    world_building = models.TextField(
        blank=True,
        null=True,
        help_text="Describe the unique world or setting in your fantasy story."
    )
    species = models.TextField(
        blank=True,
        null=True,
        help_text="Introduce unique species or beings in your fantasy story."
    )
    quest = models.TextField(
        blank=True,
        null=True,
        help_text="Outline the main quest or adventure in your fantasy story."
    )
    crime = models.TextField(
        blank=True,
        null=True,
        help_text="Describe the central crime or mystery that needs solving in your mystery story."
    )
    detective = models.TextField(
   
        blank=True,
        null=True,
        help_text="Introduce the detective or protagonist tasked with solving the mystery."
    )
    clues_red_herrings = models.TextField(
        blank=True,
        null=True,
        help_text="Suggest clues and potential red herrings to make the mystery engaging."
    )
    time_period = models.TextField(

        blank=True,
        null=True,
        help_text="Specify the historical time period in your historical fiction story."
    )
    historical_figures = models.TextField(
        blank=True,
        null=True,
        help_text="Mention any real historical figures or events you want to include in your story."
    )
    character_arcs = models.TextField(
        blank=True,
        null=True,
        help_text="Describe character arcs or development for characters in your historical fiction story."
    )
    meet_cute = models.TextField(
        blank=True,
        null=True,
        help_text="Describe the initial encounter or 'meet-cute' between romantic leads in your romance story."
    )
    obstacles_to_love = models.TextField(
        blank=True,
        null=True,
        help_text="Highlight obstacles, conflicts, or misunderstandings that challenge the romance in your story."
    )
    resolution = models.TextField(
        blank=True,
        null=True,
        help_text="Indicate how the romantic relationship should evolve and conclude."
    )
    atmosphere = models.TextField(
        blank=True,
        null=True,
        help_text="Describe the eerie or unsettling atmosphere in your horror story."
    )
    threat_entity = models.TextField(
        blank=True,
        null=True,
        help_text="Specify the nature of the threat, monster, or entity causing fear in your horror story."
    )
    suspense_dread = models.TextField(
        blank=True,
        null=True,
        help_text="Emphasize building suspense and a sense of dread in your horror story."
    )
    age_group = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Specify the target age group for your children's literature (e.g., 'Ages 5-8')."
    )
    moral_lesson = models.TextField(
        blank=True,
        null=True,
        help_text="Include any moral lessons or messages you want to convey in your children's literature story."
    )
    
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)   

    def __str__(self):
        return f'{self.title} -- {self.genre} -- {self.type}'
    
    @property
    def has_outline(self):
        if self.storyoutline.all().exists():
            return True
        return False
    
    @property
    def has_story(self):
        # Check if a StoryOutline related to this StoryRaw has a Story
        story_outline = self.storyoutline.first()
        
        if story_outline is not None:
            story = (story_outline.story.all()).exists()       
            return story
        return False
    
    def get_absolute_url(self):
        return reverse('literature:generate_story_title_and_outline', args=[self.pk])
    
class StoryOutline(models.Model):
    story_raw = models.ForeignKey(StoryRaw, on_delete=models.CASCADE, related_name='storyoutline')
    segment = models.TextField(null=True, blank=True, help_text="Story will be created based on the outline provided in this segment. But you have the flexibility to edit the outline.")
    
    # @property
    # def has_story(self):
    #     return hasattr(self, 'story') and bool(self.story.sigment_story)            

    
class Story(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    story_outline = models.ForeignKey(StoryOutline, on_delete=models.CASCADE, related_name='story')    
    sigment_story = models.TextField(null=True, blank=True)
    
