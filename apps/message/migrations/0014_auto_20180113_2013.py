# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-13 20:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0013_auto_20180113_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateField(default=datetime.datetime.now, max_length=20, verbose_name='发送时间'),
        ),
    ]