# Generated by Django 2.2 on 2019-04-05 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_alias_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='AliasUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='date')),
                ('count', models.PositiveSmallIntegerField(verbose_name='count')),
                ('alias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alias', to='emails.Alias')),
            ],
            options={
                'verbose_name': 'alias usage',
                'verbose_name_plural': 'alias usage',
                'unique_together': {('alias', 'date')},
            },
        ),
    ]
