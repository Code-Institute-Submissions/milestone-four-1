# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-24 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0007_commission_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='commissiontype',
            name='completed_url',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='commissiontype',
            name='preview_url',
            field=models.CharField(default='', max_length=254),
        ),
    ]