# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-06 10:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_auto_20170805_0317'),
    ]

    operations = [
        migrations.CreateModel(
            name='solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.TextField(default=' ', max_length=1024)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.forum_form')),
            ],
        ),
    ]
