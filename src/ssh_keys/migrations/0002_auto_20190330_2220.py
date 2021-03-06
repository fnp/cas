# Generated by Django 2.1.7 on 2019-03-30 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ssh_keys', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sshkey',
            options={'ordering': ['created_at'], 'verbose_name': 'SSH key', 'verbose_name_plural': 'SSH keys'},
        ),
        migrations.AddField(
            model_name='sshkey',
            name='comment',
            field=models.CharField(blank=True, max_length=255, verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='sshkey',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='sshkey',
            name='key',
            field=models.TextField(verbose_name='key'),
        ),
        migrations.AlterField(
            model_name='sshkey',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
