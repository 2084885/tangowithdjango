# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.ForeignKey(to='rango.Category'),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='page',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
