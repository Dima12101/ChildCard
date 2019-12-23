# Generated by Django 2.2.8 on 2019-12-22 15:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20191211_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='global_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]