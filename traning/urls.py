from django.contrib import admin
from django.urls import path
from traning.views import main, games

app_name = 'traning'

urlpatterns = [
    path('', main.MainView.as_view(), name='traning'),
    path('alphabet/', main.AlphabetView.as_view(), name='alphabet'),
    path('sounds/', main.SoundsView.as_view(), name='sounds'),
    path('games/alphabet/', games.GameAlphabetView.as_view(), name='game-alphabet')
]
