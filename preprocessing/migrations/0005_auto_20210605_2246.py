# Generated by Django 3.1.7 on 2021-06-05 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preprocessing', '0004_fileupload_wl_range_end'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='wl_range_end',
        ),
        migrations.RemoveField(
            model_name='fileupload',
            name='wl_range_start',
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='wl_corr',
            field=models.IntegerField(default=900),
        ),
    ]
