# Generated by Django 3.1.7 on 2021-04-11 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete_imagecreate'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(upload_to='')),
                ('n_differential', models.IntegerField()),
                ('polyorder', models.IntegerField()),
                ('window_length', models.IntegerField()),
                ('n_smooth', models.IntegerField()),
            ],
        ),
    ]