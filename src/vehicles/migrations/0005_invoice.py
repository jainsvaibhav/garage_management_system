# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-10 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_auto_20171009_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.CharField(max_length=12)),
                ('is_purchased', models.BooleanField()),
                ('is_sold', models.BooleanField()),
                ('purchased_amount', models.PositiveIntegerField()),
                ('sold_amount', models.PositiveIntegerField()),
                ('expense', models.PositiveIntegerField()),
                ('date_time', models.DateTimeField()),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.UserDetails')),
                ('vehicle_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.VehicleDetails')),
            ],
        ),
    ]
