from django import forms


class JobForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    bigDescription = forms.CharField(label='bigDescription', max_length=100)
    smallDescription = forms.CharField(label='smallDescription', max_length=100)