# Generated by Django 4.2.5 on 2023-10-23 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildbeats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subclub',
            name='image',
            field=models.ImageField(default='', upload_to='trendles/images'),
        ),
    ]
