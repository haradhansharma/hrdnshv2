from django import forms
from django.conf import settings
from pkg_resources import require

class LookingForm(forms.Form):     
    
   
    # looking_for = forms.ChoiceField(widget=forms.Select, choices=settings.LOOKING)
    looking_for = forms.ChoiceField(choices=settings.LOOKING, required=False, widget=forms.Select(attrs={'class': 'form-select', }))
    def clean(self):
        super().clean()
        looking_for = self.cleaned_data.get("looking_for")
    
        
        if not looking_for:
            msg = "You probably forgot to choose how I can help you!"
            self.add_error('looking_for', msg)
        