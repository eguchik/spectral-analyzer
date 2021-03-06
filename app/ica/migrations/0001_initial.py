# Generated by Django 3.1.7 on 2021-05-03 06:47

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
                ('n_components', models.IntegerField()),
                ('algo', models.CharField(choices=[('FastICA', 'FastICA'), ('InfoMax', 'InfoMax'), ('JADE', 'JADE')], max_length=255)),
            ],
        ),
    ]
