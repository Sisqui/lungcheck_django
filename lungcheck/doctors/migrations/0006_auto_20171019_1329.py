# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-19 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_auto_20170528_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='checked',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='doctor_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='doctor_review',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='healthy',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
    ]