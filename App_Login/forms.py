from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from App_Login.models import Profile
from django.forms import ModelForm
class SignUpForm(UserCreationForm):
    email=forms.EmailField(label='Email Address', required=True)
    class meta:
        model=User
        fields=('username','email','password1','password2')


class UserProfileChangeForm(UserChangeForm):
    class meta:
        model=User
        fields=('username','email','first_name','last_name','password')




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']