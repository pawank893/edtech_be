# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-16 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edtech', '0005_choice_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice',
            field=models.CharField(max_length=1000),
        ),
    ]
