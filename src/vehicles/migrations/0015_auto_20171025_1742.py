# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-25 17:42
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0014_auto_20171025_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partydetails',
            name='aadhar_no',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99999)]),
        ),
    ]
