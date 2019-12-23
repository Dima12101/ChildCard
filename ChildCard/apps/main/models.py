from django.db import models
from django.contrib.auth.models import User
import uuid


class Card(models.Model):
    global_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    child_name = models.CharField(verbose_name='имя ребёнка', max_length=50)
    BOY = 1
    GIRL = 2
    GENDER_TYPES = (
        (BOY, 'boy'),
        (GIRL, 'girl'),
    )
    gender = models.IntegerField(verbose_name='пол ребёнка', choices=GENDER_TYPES)
    path_child_photo = models.FilePathField(verbose_name='путь к фото', default=None, blank=True, null=True)
    creator_id = models.ForeignKey(User, verbose_name='создатель карточки', on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='дата создания', auto_now=True)

    def __str__(self):
        return self.child_name

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
