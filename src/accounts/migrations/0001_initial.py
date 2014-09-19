# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordering', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('image', models.ImageField(upload_to=b'accounts/service/')),
            ],
            options={
                'ordering': ('ordering',),
            },
            bases=(models.Model,),
        ),
    ]
