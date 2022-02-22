# Generated by Django 3.0 on 2022-02-16 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0004_auto_20220215_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurAvesome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textt', models.CharField(max_length=20, verbose_name='Text')),
                ('textt2', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'OurAwesome',
                'verbose_name_plural': 'OurAwesomes',
            },
        ),
        migrations.CreateModel(
            name='DescriptionOur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Description')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bboard.Category')),
            ],
            options={
                'verbose_name': 'Our Description',
                'verbose_name_plural': 'Our Description',
            },
        ),
    ]
