# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 00:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ide', '0005_auto_20171117_0012'),
        ('api', '0003_auto_20171117_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileentity',
            name='repo',
        ),
        migrations.AddField(
            model_name='fileentity',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='ide.Project'),
        ),
    ]
