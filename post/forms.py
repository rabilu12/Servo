from django import forms
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




#class Register_from(Model.Form):
#   first_name = forms.CharField(max_length=100)
#last_name = forms.CharField(widget=forms.Textarea)
# email = forms.EmailField()
#password = forms.PasswordInput()
#c_password = forms.PasswordInput()


class signform(UserCreationForm):
    email = forms.EmailField(required=True, label='email')
    class meta:
        model = User
    fields =  ('username', 'email', 'password1', 'password2' )

    