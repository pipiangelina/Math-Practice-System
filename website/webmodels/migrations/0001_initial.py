# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 04:55
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
                ('solution', ckeditor.fields.RichTextField()),
                ('answer', ckeditor.fields.RichTextField(default='Test')),
            ],
        ),
    ]
