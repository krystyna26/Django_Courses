# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-22 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('creeated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
