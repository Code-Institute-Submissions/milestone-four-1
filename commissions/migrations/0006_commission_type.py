# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-23 11:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0005_auto_20200523_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='commission',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='commissions.CommissionType'),
        ),
    ]
