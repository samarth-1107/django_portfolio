from django import forms
from .models import ContactForm

class CreateContact(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['full_name', 'email', 'phone_number', 'description']
