# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-26 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0004_auto_20170225_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.CharField(max_length=150),
        ),
    ]
