# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_auto_20170426_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='age',
            new_name='birth_year',
        ),
        migrations.AddField(
            model_name='doctor',
            name='mail_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='mail_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]