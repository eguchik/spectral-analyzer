# Generated by Django 3.1.7 on 2021-05-19 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(upload_to='')),
                ('wl_corr', models.IntegerField()),
                ('wl_range_start', models.IntegerField()),
                ('wl_range_end', models.IntegerField()),
            ],
        ),
    ]
