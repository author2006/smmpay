# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 12:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0005_auto_20171031_1400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favoriteadvert',
            options={'ordering': ('-pk',), 'verbose_name': 'favorite', 'verbose_name_plural': 'favorites'},
        ),
        migrations.AlterModelOptions(
            name='phrase',
            options={'ordering': ('pk',), 'verbose_name': 'phrase', 'verbose_name_plural': 'phrases'},
        ),
    ]