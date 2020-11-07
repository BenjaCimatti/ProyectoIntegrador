from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import QuarterMatch
from django.forms import HiddenInput


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class QuarterMatchForm(forms.ModelForm):

	class Meta:

		model = QuarterMatch
		fields = ['matchNumber',]
		widgets = {'matchNumber': HiddenInput(),}
