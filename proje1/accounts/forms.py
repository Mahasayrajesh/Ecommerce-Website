from django import forms
from django.contrib.auth.models import User
from accounts.models import PersonDetail

class regForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password']


class PersonProfileForm(forms.ModelForm):
    class Meta:
        model=PersonDetail
        fields="__all__"