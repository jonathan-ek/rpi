# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-06 22:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_auto_20160706_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plug',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.Schedule'),
        ),
    ]
