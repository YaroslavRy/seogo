from django import forms

class NameForm(forms.Form):
	headers = forms.CharField(label='Введите URL', max_length=128)

	# A/B test form
	group_a_visits = forms.CharField(label='Группа А визиты', max_length=128)
	group_b_visits = forms.CharField(label='Группа B визиты', max_length=128)
	group_a_conv = forms.CharField(label='Группа A конверсии', max_length=128)
	group_b_conv = forms.CharField(label='Группа B конверсии', max_length=128)