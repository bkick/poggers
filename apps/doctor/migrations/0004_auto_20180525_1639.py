# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-25 23:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_patients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients',
            name='patients',
        ),
        migrations.DeleteModel(
            name='patients',
        ),
    ]