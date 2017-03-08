# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-08 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('content', models.CharField(max_length=300, verbose_name='Content')),
            ],
        ),
    ]