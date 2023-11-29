from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'last name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Mark'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Markov'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Mark', 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'umail@gmail.com', 'readonly': True}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'photo'}), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'image')


