# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 22:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20171201_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.Person'),
        ),
    ]
