# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-03-13 07:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('major', models.CharField(max_length=30)),
                ('tel_num', models.IntegerField()),
                ('num_people', models.IntegerField(verbose_name=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29))),
                ('rend_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('room_number', models.SmallIntegerField(choices=[(0, '회의실 1'), (1, '회의실 2'), (2, '회의실 3')], default=0)),
                ('reservation_accept', models.BooleanField(default=False)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
