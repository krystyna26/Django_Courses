# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-23 21:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_table', '0002_auto_20171022_0331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='creeated_at',
            new_name='created_at',
        ),
    ]
