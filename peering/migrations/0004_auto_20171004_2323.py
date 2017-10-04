# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peering', '0003_auto_20170903_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autonomoussystem',
            name='ipv4_as_set',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='autonomoussystem',
            name='ipv4_max_prefixes',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='autonomoussystem',
            name='ipv6_as_set',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='autonomoussystem',
            name='ipv6_max_prefixes',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
