from django import forms

class NameForm(forms.Form):
	headers = forms.CharField(label='URL', max_length=128)