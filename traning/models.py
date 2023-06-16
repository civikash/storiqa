from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from account.models import Account

class Ages(models.Model):
    AGE_1 = '3 года'
    AGE_2 = '4 года'
    AGE_3 = '5 лет'
    AGE_4 = '6 лет'
    AGE_5 = '7лет'

    AGE_CHOICES = [
        (AGE_1, '3 года'),
        (AGE_2, '4 года'),
        (AGE_3, '5 лет'),
        (AGE_4, '6 лет'),
        (AGE_5, '7 лет')
    ]

    age_name = models.CharField(max_length=20, choices=AGE_CHOICES)

class Game(models.Model):
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    result = models.IntegerField(null=True)
    age = models.ForeignKey(Ages, verbose_name=_("Возраст"), on_delete=models.CASCADE)
    

    def __str__(self):
        return f"Игра #{self.id} - Пользователь: {self.user.username}, Результат: {self.result}, Возраст: {self.age}"
