# Generated by Django 3.2.3 on 2021-05-22 19:06

from django.db import migrations, models
import siterysin.models


class Migration(migrations.Migration):

    dependencies = [
        ('siterysin', '0007_auto_20210522_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=siterysin.models.file_path)),
            ],
        ),
    ]
