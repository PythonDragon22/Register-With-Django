from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout
from custom_User.forms import User_Signup_Form, User_Signin_Form
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

def home_page(request):
    return render(request, 'custom_User/home_page.html')

class User_Signup_View(View):
    def get(self, request, *args, **kwargs):

        signup_form = User_Signup_Form()
        return render(request, 'custom_User/user_signup.html', context= {'signup_form': signup_form})

    def post(self, request, *args, **kwargs):
        signup_form = User_Signup_Form(request.POST, request.FILES)      # grab the signup form with its data if exists
        if signup_form.is_valid():
            if signup_form.cleaned_data['password'] and signup_form.cleaned_data['password_confirmation'] and signup_form.cleaned_data['password'] == signup_form.cleaned_data['password_confirmation']:
                if User.objects.filter(email= signup_form.cleaned_data['email']).exists():
                    messages.error(request, 'That email is already taken')
                    return redirect('user_signup_page')

                if User.objects.filter(username= signup_form.cleaned_data['username']).exists():
                    messages.error(request, 'That username is already taken')
                    return redirect('user_signup_page')

                else:
                    new_user = User.objects.create_user(
                        email= signup_form.cleaned_data['email'],
                        username= signup_form.cleaned_data['username'],
                        first_name= signup_form.cleaned_data['first_name'],
                        last_name= signup_form.cleaned_data['last_name'],
                        password= signup_form.cleaned_data['password'],
                    )
                    new_user.save()
                    messages.success(request, 'You have signed up successfully')
                    return redirect('user_signin_page')
            else:
                messages.error(request, 'Passwords do not match')
                return redirect('user_signup_page')
        return render(request, 'custom_User/user_signup.html', context= {'signup_form': signup_form})


class User_Signin_View(View):
    def get(self, request, *args, **kwargs):

        signin_form = User_Signin_Form()
        return render(request, 'custom_User/user_signin.html', context= {'signin_form': signin_form})

    def post(self, request, *args, **kwargs):
        signin_form = User_Signin_Form(request.POST)
        if signin_form.is_valid():
            user = authenticate(email= signin_form.cleaned_data['email'], password= signin_form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('home_page')

            else:
                messages.error(request, 'Invalid credentials')
                return redirect('user_signin_page')
        return render(request, 'custom_User/user_signin.html', context= {'signin_form': signin_form})


class User_Signout_View(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'You are now logged out')
        return render(request, 'custom_User/user_signout.html')
