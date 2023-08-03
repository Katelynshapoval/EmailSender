from django import forms
from .models import EmailList
class CreateNewList(forms.Form):
    email = forms.EmailField(label="To", max_length=200, required=False, widget=forms.TextInput(attrs={'placeholder': "Enter the recipient's email address", "style": "width: 300px"}))
    # group = forms.CharField(label='Choose a group', required=False, widget=forms.Select(choices=GROUPS))
    subject = forms.CharField(label="Subject", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Enter the subject', "style": "width: 300px"}))
    content = forms.CharField(label="Content", max_length=500, widget=forms.Textarea(attrs={'placeholder': 'Enter the message', "style": "height: 100px"}))

