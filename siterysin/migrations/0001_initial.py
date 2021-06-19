# Generated by Django 3.2.3 on 2021-05-21 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='no-title', max_length=100)),
                ('text', models.TextField(blank=True, default='no-text')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='')),
            ],
        ),
    ]