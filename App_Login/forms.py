from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from App_Login.models import Profile
from django.forms import ModelForm
class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    password1 = forms.CharField(required=True, label="",
                                widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(required=True, label="",
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
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