from django import forms

class CreateNewList(forms.Form):
    email = forms.EmailField(label="To", max_length=200)
    subject = forms.CharField(label="Subject", max_length=200)
    content = forms.CharField(label="Content", max_length=500, widget=forms.Textarea)