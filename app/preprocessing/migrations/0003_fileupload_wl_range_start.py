# Generated by Django 3.1.7 on 2021-05-19 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preprocessing', '0002_auto_20210519_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='wl_range_start',
            field=models.IntegerField(default=0),
        ),
    ]
