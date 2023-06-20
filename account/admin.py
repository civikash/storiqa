from django.contrib import admin
from account.models import Account, Child, Balance, Transaction, AccountInformation

@admin.register(AccountInformation)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Child)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Balance)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Transaction)
class AccountAdmin(admin.ModelAdmin):
    pass