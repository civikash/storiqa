from django.contrib import admin
from django.urls import path
from landing.views import landing, tarifs

app_name = 'landing'

urlpatterns = [
    path('', landing.AppView.as_view(), name='landing'),
    path('tarifs/', tarifs.TarifsView.as_view(), name='tarifs')
]
