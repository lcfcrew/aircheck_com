# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('text', models.CharField(max_length=256)),
                ('latitude', models.DecimalField(blank=True, decimal_places=12, max_digits=15, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=12, max_digits=15, null=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('twitter_id', models.CharField(blank=True, max_length=128, null=True)),
                ('twitter_name', models.CharField(blank=True, max_length=128, null=True)),
                ('language', models.CharField(blank=True, max_length=64, null=True)),
                ('language_iso', models.CharField(blank=True, max_length=2, null=True)),
                ('language_score', models.FloatField(blank=True, null=True)),
                ('sentiment', models.FloatField(blank=True, null=True)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
