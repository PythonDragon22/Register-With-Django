from django.urls import path
from custom_User.views import (
    User_Signup_View,
    User_Signin_View,
    User_Signout_View,

    home_page
)

urlpatterns = [
	path('', home_page, name="home_page"),
    path('signup/', User_Signup_View.as_view(), name="user_signup_page"),
    path('signin/', User_Signin_View.as_view(), name="user_signin_page"),
    path('signout/', User_Signout_View.as_view(), name="user_signout_page"),
]
