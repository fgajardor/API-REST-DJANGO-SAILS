# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('tipoPedido', models.CharField(max_length=20)),
                ('valor', models.IntegerField()),
            ],
        ),
    ]
