# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-07 17:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('code', models.CharField(blank=True, max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('sem1', 'Semester I'), ('sem2', 'Semester II'), ('sem3', 'Semester III'), ('sem4', 'Semester IV'), ('sem5', 'Semester V'), ('sem6', 'Semester VI'), ('sem7', 'Semester VII'), ('sem8', 'Semester VIII')], default='Semester I', max_length=15, null=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Semesters',
                'verbose_name': 'Semester',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='semester.Semester'),
        ),
    ]
