# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-10 22:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0008_accounting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounting',
            name='purchase_bill_no',
        ),
    ]