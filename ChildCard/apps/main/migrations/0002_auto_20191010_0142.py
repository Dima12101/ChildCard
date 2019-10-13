# Generated by Django 2.2.5 on 2019-10-09 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='path_child_photo',
            field=models.FilePathField(blank=True, default=None, null=True, verbose_name='путь к фото'),
        ),
        migrations.AlterField(
            model_name='card',
            name='creator_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создатель карточки'),
        ),
    ]