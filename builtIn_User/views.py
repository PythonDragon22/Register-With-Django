from django.shortcuts import render, redirect

from django.urls import reverse
from django.contrib.auth import login
from builtIn_User.forms import CustomUserCreationForm, UserForm , ProfileForm

# Create your views here.

def dashboard(request):
    return render(request, "builtIn_User/user_dashboard.html")


def register(request):
    if request.method == "GET":
        return render(request, "builtIn_User/user_signup.html", {"form": CustomUserCreationForm})

    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))


def profile(request):
    logged_in_user = request.user
    profile = Profile.objects.get(user = logged_in_user)
    return render(request,'builtIn_User/profile.html',{'profile': profile})


def profile_edit(request):
    logged_in_user = request.user
    profile = Profile.objects.get(user = logged_in_user)

    if request.method=='POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile )
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('dashboard'))

    else :
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request,'builtIn_User/profile_edit.html',{'userform':userform , 'profileform':profileform})