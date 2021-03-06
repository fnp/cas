# Generated by Django 2.1.7 on 2019-04-01 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssh_keys', '0002_auto_20190330_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='sshkey',
            name='algorithm',
            field=models.CharField(default='', editable=False, max_length=32, verbose_name='algorithm'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sshkey',
            name='bit_length',
            field=models.IntegerField(editable=False, null=True, verbose_name='bit length'),
        ),
        migrations.AddField(
            model_name='sshkey',
            name='md5_hash',
            field=models.CharField(default='', editable=False, max_length=128, verbose_name='MD5 hash'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sshkey',
            name='comment',
            field=models.CharField(editable=False, max_length=255, verbose_name='comment'),
        ),
    ]
