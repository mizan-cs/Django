# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 22:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20171201_0432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='person',
        ),
        migrations.AddField(
            model_name='person',
            name='massage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.Conversation'),
        ),
    ]