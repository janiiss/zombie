from django import forms
from main.models import Zombie, Tweet

class ZombieForm(forms.ModelForm):
	class Meta:
		model = Zombie

class TweetForm(forms.ModelForm):
	class Meta:
		model = Tweet