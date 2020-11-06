from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import *

# remove labels and adding attributes
class ChangePassword(PasswordChangeForm):
    class Meta():
        model = User
        fields = ('password',)

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['class'] = 'input'
        self.fields['password'].widget.attrs['autocomplete'] = 'off'
        self.fields['password1'].widget.attrs['placeholder'] = 'Confirm'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': 'Email Address', 'id': 'email', 'title': 'Your Email is Safe With US'},))

    class Meta:
        model = User
        fields = ('username',
                  'email', 'password', )

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['username'].widget.attrs['id'] = 'username'
        self.fields['username'].help_text = ''
        self.fields['password'].help_text = ''
        self.fields['password'].label = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Username'


class EditUserDetail(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('dp', 'contact', 'marital')

    def __init__(self, *args, **kwargs):
        super(EditUserDetail, self).__init__(*args, **kwargs)
        self.fields['contact'].widget.attrs['class'] = 'input'
        self.fields['dp'].widget.attrs['class'] = 'input'
        self.fields['marital'].label = "Married"
        self.fields['dp'].label = "Pick dp"


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': 'Enter email...', 'id': 'email', 'title': 'Your Email is Safe With US'},))

    class Meta():
        model = User
        fields = ('username',
                  'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['username'].widget.attrs['id'] = 'username'
        self.fields['username'].help_text = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Username'

        self.fields['password1'].widget.attrs['class'] = 'input'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter password...'
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs['class'] = 'input'
        self.fields['password2'].widget.attrs['placeholder'] = 'Enter password again...'
       # self.fields['password2'].label = ""
        self.fields['password2'].help_text = ""
