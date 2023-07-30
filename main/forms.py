from django import forms

class CreateNewList(forms.Form):
    email = forms.EmailField(label="To", max_length=200, widget=forms.TextInput(attrs={'placeholder': "Enter the recipient's email address", "style": "width: 300px"}))
    subject = forms.CharField(label="Subject", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Enter the subject', "style": "width: 300px"}))
    content = forms.CharField(label="Content", max_length=500, widget=forms.Textarea(attrs={'placeholder': 'Enter the message', "style": "height: 100px"}))