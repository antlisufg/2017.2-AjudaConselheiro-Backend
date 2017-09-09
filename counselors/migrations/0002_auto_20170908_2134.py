# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 21:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('counselors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='counselor',
            old_name='phone_number',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='counselor',
            name='full_name',
        ),
        migrations.AddField(
            model_name='counselor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='counselor',
            name='first_name',
            field=models.CharField(default='NOME', max_length=100),
        ),
        migrations.AddField(
            model_name='counselor',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='counselor',
            name='last_name',
            field=models.CharField(default='SOBRENOME', max_length=100),
        ),
        migrations.AddField(
            model_name='counselor',
            name='password',
            field=models.CharField(default='SENHA', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='counselor',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]