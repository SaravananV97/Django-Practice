from django import forms
from django.contrib.auth.models import User
from usr_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput()) #password input for userform
    class Meta():# takes a model and a field
        model = User
        fields = ('username','email','password') # take only 3 fields from user

class UserFieldInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo # use our own model that has fields from User
        fields = ('portfolio_site','profile_pic') # consider the additional fields for the form
