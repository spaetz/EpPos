# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-06 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0011_auto_20170905_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]