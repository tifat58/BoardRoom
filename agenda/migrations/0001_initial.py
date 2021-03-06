# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 05:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('short_description', models.CharField(blank=True, max_length=100, null=True)),
                ('full_article', models.CharField(max_length=3000)),
                ('isActive', models.NullBooleanField()),
                ('isDelete', models.NullBooleanField()),
                ('insertUser', models.CharField(max_length=50)),
                ('insertDate', models.DateField(blank=True, null=True)),
                ('updateUser', models.CharField(max_length=50)),
                ('updateDate', models.DateField(blank=True, null=True)),
                ('project', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('meeting_no', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.CharField(max_length=1000)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('isActive', models.NullBooleanField()),
                ('isDelete', models.NullBooleanField()),
                ('insertUser', models.CharField(max_length=50)),
                ('insertDate', models.DateField(blank=True, null=True)),
                ('updateUser', models.CharField(max_length=50)),
                ('updateDate', models.DateField(blank=True, null=True)),
                ('project', models.CharField(max_length=100)),
                ('company_meeting', models.ForeignKey(blank=True, default=-1, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.CompanyDetail')),
            ],
        ),
        migrations.AddField(
            model_name='agenda',
            name='meeting_agenda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agenda.Meeting'),
        ),
    ]
