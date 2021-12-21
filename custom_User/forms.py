from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)



class User_Signup_Form(forms.Form):
    email = forms.EmailField(label= '', widget= forms.EmailInput(attrs= {'placeholder': 'Email Address', 'class': 'input-field'}))
    username = forms.CharField(label= '', widget= forms.TextInput(attrs= {'placeholder': 'Username', 'class': 'input-field'}))
    first_name = forms.CharField(label= '', widget= forms.TextInput(attrs= {'placeholder': 'First Name', 'class': 'input-field'}))
    last_name = forms.CharField(label= '', widget= forms.TextInput(attrs= {'placeholder': 'Last Name', 'class': 'input-field'}))
    password = forms.CharField(label= '', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'input-field'}))
    password_confirmation = forms.CharField(label= '', widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation', 'class': 'input-field'}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__exact=email).exists():
            raise forms.ValidationError("This is an invalid user.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username__exact=username).exists():
            raise forms.ValidationError("This is an invalid user.")
        return username


class User_Signin_Form(forms.Form):
    email= forms.CharField(label= '', widget = forms.TextInput(attrs={'placeholder': 'Email Address'}))
    password= forms.CharField(label= '', widget = forms.PasswordInput(attrs={'placeholder': 'Password'}))
