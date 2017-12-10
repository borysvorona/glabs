# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab1', '0002_mathexpression_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mathexpression',
            name='end',
            field=models.DecimalField(decimal_places=4, default=1.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='mathexpression',
            name='start',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='mathexpression',
            name='step',
            field=models.DecimalField(decimal_places=2, default=0.1, max_digits=4),
        ),
    ]