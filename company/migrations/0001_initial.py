# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 05:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('abbreviated_name', models.CharField(max_length=20)),
                ('company_description', models.CharField(blank=True, max_length=500, null=True)),
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
            name='CompanyMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('1', 'Mr.'), ('2', 'Ms.')], max_length=40, null=True)),
                ('name', models.CharField(max_length=300)),
                ('isActive', models.NullBooleanField(default=True)),
                ('isDelete', models.NullBooleanField(default=False)),
                ('insertUser', models.CharField(default='system', max_length=50)),
                ('insertDate', models.DateField(blank=True, default=None, null=True)),
                ('updateUser', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('updateDate', models.DateField(blank=True, default=None, null=True)),
                ('project', models.CharField(default='1', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyMemberDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.NullBooleanField(default=True)),
                ('isDelete', models.NullBooleanField(default=False)),
                ('insertUser', models.CharField(default='system', max_length=50)),
                ('insertDate', models.DateField(blank=True, default=None, null=True)),
                ('updateUser', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('updateDate', models.DateField(blank=True, default=None, null=True)),
                ('project', models.CharField(default='1', max_length=100)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.CompanyMember')),
                ('member_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.CompanyDetail')),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation_title', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('isActive', models.NullBooleanField()),
                ('isDelete', models.NullBooleanField()),
                ('insertUser', models.CharField(max_length=50)),
                ('insertDate', models.DateField(blank=True, null=True)),
                ('updateUser', models.CharField(max_length=50)),
                ('updateDate', models.DateField(blank=True, null=True)),
                ('project', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='companymemberdetail',
            name='member_designation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Designation'),
        ),
    ]
