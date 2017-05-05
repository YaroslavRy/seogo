# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seotools', '0005_auto_20170505_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metatags',
            name='description_text',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='metatags',
            name='page_uri',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='metatags',
            name='title_text',
            field=models.CharField(default='', max_length=128),
        ),
    ]