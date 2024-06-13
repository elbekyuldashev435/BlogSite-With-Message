from django import forms
from .models import Contacts, Message


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('name', 'users')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']