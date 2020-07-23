from django import forms

class ProfileForm(forms.Form):
    type = forms.CharField(label='Type', max_length=100)
    name = forms.CharField(label='Name', max_length=100)
    description = forms.CharField(label='Desc', max_length=100)