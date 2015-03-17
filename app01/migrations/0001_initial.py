# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('uid', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('gender', models.NullBooleanField()),
                ('email', models.EmailField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
