# Generated by Django 2.1.7 on 2019-03-30 22:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ('name',), 'verbose_name': 'service', 'verbose_name_plural': 'services'},
        ),
        migrations.AlterField(
            model_name='service',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.Group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='service',
            name='key',
            field=models.CharField(blank=True, max_length=255, verbose_name='key'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='service',
            name='url',
            field=models.URLField(blank=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='service',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='users'),
        ),
        migrations.AlterField(
            model_name='service',
            name='uses_ssh',
            field=models.BooleanField(default=False, verbose_name='uses SSH'),
        ),
    ]