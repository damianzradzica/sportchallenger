# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-19 09:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportchallenger', '0004_auto_20170118_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='facility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facility_reservation', to='sportchallenger.SportFacility'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reservation', to='sportchallenger.MyUser'),
        ),
    ]
