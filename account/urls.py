from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from account.views import profile, login, register

app_name = 'account'

urlpatterns = [
    path('', login_required(profile.ProfileView.as_view(), login_url='landing:landing'), name='profile'),
    path('activate/<uidb64>/<token>/', register.ActivateAccount.as_view(), name='activate'),
    path('login/', login.LoginView.as_view(), name='login'),
    path('register/', register.RegisterView.as_view(), name='register')
]
