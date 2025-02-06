from django import forms
from .models import Participant

class ParticipantSignupForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['register_number', 'college_name', 'department', 'whatsapp_number', 'year_of_study']
