# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-08 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicledetails',
            name='registration_no',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]