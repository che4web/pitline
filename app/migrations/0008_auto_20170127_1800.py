# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-27 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170127_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintext',
            name='text',
            field=models.TextField(blank=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='textcategory',
            name='text',
            field=models.TextField(blank=True, max_length=255, verbose_name='Текст'),
        ),
    ]