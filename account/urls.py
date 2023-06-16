from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from account.views import profile, login

app_name = 'account'

urlpatterns = [
    path('', login_required(profile.ProfileView.as_view(), login_url='landing:landing'), name='profile'),
    path('login/', login.LoginView.as_view(), name='login')
]
