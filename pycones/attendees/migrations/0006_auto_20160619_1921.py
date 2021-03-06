# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 17:21
from __future__ import unicode_literals

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('attendees', '0005_auto_20151104_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]
