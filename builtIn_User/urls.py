from django.urls import path
from builtIn_User.views import dashboard, register, profile, profile_edit

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("register/", register, name="register"),
    path('profile', profile, name='profile'),
    path('profile/edit', profile_edit, name='profile_edit'),
]
