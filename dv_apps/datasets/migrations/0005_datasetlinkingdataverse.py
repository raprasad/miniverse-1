# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-05 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0004_auto_20160628_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatasetLinkingDataverse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkcreatetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'datasetlinkingdataverse',
                'managed': False,
            },
        ),
    ]
