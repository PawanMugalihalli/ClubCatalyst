# Generated by Django 4.2.5 on 2023-11-08 03:54

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('wildbeats', '0004_alter_subclub_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='subclub',
            name='leader1mail',
            field=models.EmailField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subclub',
            name='leader1phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='subclub',
            name='leader2mail',
            field=models.EmailField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subclub',
            name='leader2phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='subclub',
            name='subleader1mail',
            field=models.EmailField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subclub',
            name='subleader1phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='subclub',
            name='subleader2mail',
            field=models.EmailField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subclub',
            name='subleader2phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='subclub',
            name='subleader3mail',
            field=models.EmailField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subclub',
            name='subleader3phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
