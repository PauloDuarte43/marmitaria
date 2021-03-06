# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-10 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_auto_20180408_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='produtodespesa',
            name='quantidade',
            field=models.DecimalField(decimal_places=4, max_digits=19),
        ),
        migrations.AlterField(
            model_name='produtoreceita',
            name='quantidade',
            field=models.DecimalField(decimal_places=4, max_digits=19),
        ),
    ]
