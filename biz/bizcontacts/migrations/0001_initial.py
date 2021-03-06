# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 03:09
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(blank=True, max_length=300)),
                ('address2', models.CharField(blank=True, max_length=300)),
                ('city', models.CharField(blank=True, max_length=300)),
                ('state', models.CharField(blank=True, max_length=300)),
                ('country', models.CharField(blank=True, max_length=300)),
                ('postal_code', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('business_name', models.CharField(blank=True, max_length=200)),
                ('cell_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')])),
                ('work_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.CharField(blank=True, max_length=200, validators=[django.core.validators.RegexValidator(regex='\\w+@\\w+\\.\\w+$')])),
                ('notes', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_url', models.CharField(blank=True, max_length=300)),
                ('back_url', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bizcontacts.Image'),
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='address',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bizcontacts.Contact'),
        ),
    ]
