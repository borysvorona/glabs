# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MathExpression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DecimalField(decimal_places=6, default=0.0, max_digits=10)),
                ('end', models.DecimalField(decimal_places=6, default=1.0, max_digits=10)),
                ('expression', models.CharField(max_length=124)),
            ],
            options={
                'db_table': 'math_expression',
            },
        ),
    ]
