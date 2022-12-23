from django import forms
from accounts.models import User
from accounts.validation import cheak_email,cheak_mobile
from django.contrib.auth.forms import UserChangeForm
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    comfirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['name','email','phone','gender']
        labels = {'name':'Full name'}


class UserEditForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['name','profile_pic','email','phone','gender']
        labels ={'name':'Full Name'}
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['profile_pic'].widget.attrs.update({'type': 'image'})

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
