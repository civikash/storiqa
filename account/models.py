from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.utils.translation import gettext_lazy as _
from account.managers import AccountManager

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    permissions = models.ManyToManyField(Permission)

    class Meta:
        verbose_name = _('role')
        verbose_name_plural = _('roles')

    def __str__(self):
        return self.name


class Account(AbstractUser):
    id = models.AutoField(primary_key=True)
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    username = None
    email = models.EmailField(_('Адрес электронной почты'), unique=True)
    patronymic = models.CharField(_("Отчество"), max_length=60, null=True, blank=True)
    
    objects = AccountManager()

    roles = models.ManyToManyField(
        Role,
        verbose_name=_('roles'),
        blank=True,
        related_name='accounts'
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='account_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='account_user_permissions'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Child(models.Model):
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(_("Имя ребенка"), max_length=50)
    birth_date = models.DateField(_("Дата рождения"), auto_now=False, auto_now_add=False)
    parent = models.ForeignKey(Account, verbose_name=_("Родитель"), on_delete=models.CASCADE)


class Balance(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    balance = models.IntegerField(default=10)

    def __str__(self):
        return f"Баланс - Пользователь: {self.user.username}, Balance: {self.balance}"

class Transaction(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)