# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-19 10:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportchallenger', '0006_auto_20170119_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_reservation', to=settings.AUTH_USER_MODEL),
        ),
    ]