# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(null=True, auto_now=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(null=True, auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('가격', models.CharField(max_length=20, null=True)),
                ('image_file', models.ImageField(upload_to='static_files/uploaded/original/%Y/%m/%d')),
                ('text', models.TextField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, to='thankq.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
