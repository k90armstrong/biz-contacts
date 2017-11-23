# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 21:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bizcontacts', '0002_auto_20171116_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='back_url',
        ),
        migrations.RemoveField(
            model_name='image',
            name='front_url',
        ),
        migrations.AddField(
            model_name='image',
            name='back',
            field=models.FileField(null=True, upload_to='cards/'),
        ),
        migrations.AddField(
            model_name='image',
            name='front',
            field=models.FileField(default=django.utils.timezone.now, upload_to='cards/'),
            preserve_default=False,
        ),
    ]
