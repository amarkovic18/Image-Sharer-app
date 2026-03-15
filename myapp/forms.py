from django import forms

class AddForm(forms.Form):
    text=forms.CharField()
    image=forms.FileField()