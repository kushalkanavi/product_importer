# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-28 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_auto_20190728_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=8),
        ),
    ]
