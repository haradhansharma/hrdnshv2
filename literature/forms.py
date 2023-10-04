from django import forms
from .models import Story, StoryRaw, StoryOutline, IdeaUtilization


class IdeaUtilizationForm(forms.ModelForm):
    class Meta:
        model = IdeaUtilization
        fields = ['idea']
        
    def __init__(self, *args, **kwargs):
        super(IdeaUtilizationForm, self).__init__(*args, **kwargs)
        
        # Define the CSS class you want to add to all fields
        css_class = 'form-control'

        # Iterate through all fields in the form
        for field_name, field in self.fields.items():
            # Add the class attribute to each field
            field.widget.attrs['class'] = css_class
            field.widget.attrs['rows'] = 5

class StoryRawForm(forms.ModelForm):
    class Meta:
        model = StoryRaw
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(StoryRawForm, self).__init__(*args, **kwargs)
        
        # Define the CSS class you want to add to all fields
        css_class = 'form-control'

        # Iterate through all fields in the form
        for field_name, field in self.fields.items():
            # Add the class attribute to each field
            field.widget.attrs['class'] = css_class
            field.widget.attrs['rows'] = 3
        
        
class OutlineForm(forms.ModelForm):
    
    # Define the checkbox field
    line_response = forms.BooleanField(
        label='Line Response',
        required=False,  # Set to True if it's a required field
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    class Meta:
        model = StoryOutline
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(OutlineForm, self).__init__(*args, **kwargs)
        
        # Define the CSS class you want to add to all fields
        css_class = 'form-control'

        # Iterate through all fields in the form
        for field_name, field in self.fields.items():
                
            if isinstance(field, forms.BooleanField):
                # This field is a BooleanField
                field.widget.attrs['class'] = 'form-check-input'
            else:
                # Add the class attribute to other fields
                field.widget.attrs['class'] = css_class
                field.widget.attrs['rows'] = 3
                
                
class StoryForm(forms.ModelForm):

    class Meta:
        model = Story
        exclude = []
        fields = '__all__'
        
        
    def __init__(self, *args, **kwargs): 
   
        super(StoryForm, self).__init__(*args, **kwargs)          
        
        self.fields['story_outline'].widget = forms.HiddenInput()

        # Define the CSS class you want to add to all fields
        css_class = 'form-control'
        
        # Iterate through all fields in the form
        for field_name, field in self.fields.items():       
            
            if isinstance(field, forms.BooleanField):
                # This field is a BooleanField
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Textarea):
                
                field.widget.attrs['class'] = css_class
                field.widget.attrs['rows'] = 4
            else:
                # Add the class attribute to other fields
                field.widget.attrs['class'] = css_class
                
