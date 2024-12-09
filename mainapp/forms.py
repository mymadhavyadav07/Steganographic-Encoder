from django import forms

class DecodeForm(forms.Form):
    image = forms.ImageField(label='Select an image')

class EncodeForm(forms.Form):
    text= forms.CharField(max_length=100, label='Type a message')
    image = forms.ImageField(label='Select an image')