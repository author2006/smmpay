# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-14 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0003_auto_20200219_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='for_sale',
            field=models.BooleanField(default=False, verbose_name='for sale'),
        ),
    ]
