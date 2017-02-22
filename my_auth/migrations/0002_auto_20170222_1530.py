# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-22 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tokens',
            name='user_id',
        ),
        migrations.AddField(
            model_name='tokens',
            name='user_email',
            field=models.CharField(default='user@example.com', max_length=50),
            preserve_default=False,
        ),
    ]
