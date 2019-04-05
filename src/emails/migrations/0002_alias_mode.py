# Generated by Django 2.2 on 2019-04-05 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alias',
            name='mode',
            field=models.CharField(blank=True, choices=[('', 'Forward everything'), ('@FORWARD', 'Do not forward e-mail marked as spam.')], default='', max_length=255, verbose_name='mode'),
        ),
    ]