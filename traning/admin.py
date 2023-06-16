from django.contrib import admin
from traning.models import Game, Ages

@admin.register(Game)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Ages)
class AccountAdmin(admin.ModelAdmin):
    pass