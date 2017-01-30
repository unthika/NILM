# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-11 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0002_electricitycwe_electricitydwe_predayelectricitycwe_predayelectricitydwe_predayelectricityfge_preelec'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreDElectricityFge',
            fields=[
                ('datetime_hour', models.CharField(max_length=18, primary_key=True, serialize=False)),
                ('p', models.FloatField(db_column='P')),
                ('pt', models.FloatField(db_column='Pt')),
                ('q', models.FloatField(db_column='Q')),
                ('qt', models.FloatField(db_column='Qt')),
            ],
            options={
                'db_table': 'pre_d_electricity_fge',
                'managed': False,
            },
        ),
    ]