# Generated by Django 2.2.8 on 2019-12-22 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_card_global_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='gender',
            field=models.IntegerField(choices=[(1, 'boy'), (2, 'girl')], default=1, verbose_name='пол ребёнка'),
            preserve_default=False,
        ),
    ]