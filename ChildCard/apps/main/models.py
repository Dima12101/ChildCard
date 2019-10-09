from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    child_name = models.CharField(verbose_name='имя ребёнка', max_length=50)
    creator_id = models.ForeignKey(User, verbose_name='создатель карточки', on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='дата создания')

    def __str__(self):
        return self.child_name

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
