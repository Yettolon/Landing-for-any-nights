# Generated by Django 3.0 on 2022-02-17 17:59

import bboard.utilities
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0011_auto_20220217_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourteam',
            name='facebook',
            field=models.CharField(blank=True, max_length=60, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='image',
            field=models.ImageField(blank=True, upload_to=bboard.utilities.get_timestamp_path, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='skype',
            field=models.CharField(blank=True, max_length=60, verbose_name='Skype'),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='twitter',
            field=models.CharField(blank=True, max_length=60, verbose_name='Twitter'),
        ),
    ]