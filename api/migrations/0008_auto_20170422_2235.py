# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20170422_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameroom',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
