# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-18 21:42
from __future__ import unicode_literals

import cashondelivery.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashondelivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cashondeliverytransaction',
            options={'ordering': ('-date_created',),
                     'verbose_name': 'Cash on Delivery'},
        ),
        migrations.AlterField(
            model_name='cashondeliverytransaction',
            name='amount',
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Amount'),
        ),
        migrations.AlterField(
            model_name='cashondeliverytransaction',
            name='confirmed',
            field=models.BooleanField(default=False, verbose_name='Confirmed'),
        ),
        migrations.AlterField(
            model_name='cashondeliverytransaction',
            name='currency',
            field=models.CharField(
                blank=True, max_length=8, null=True, verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='cashondeliverytransaction',
            name='date_confirmed',
            field=models.DateTimeField(
                auto_now=True, verbose_name='Date Confirmed'),
        ),
        migrations.AlterField(
            model_name='cashondeliverytransaction',
            name='date_created',
            field=models.DateTimeField(
                auto_now_add=True, verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='cashondeliverytransaction',
            name='order_number',
            field=models.CharField(
                max_length=128, verbose_name='Order Number'),
        ),
        migrations.AlterField(
            model_name='cashondeliverytransaction',
            name='reference',
            field=models.CharField(blank=True, default=cashondelivery.models._make_uuid,
                                   max_length=100, unique=True, verbose_name='Reference'),
        ),
    ]
