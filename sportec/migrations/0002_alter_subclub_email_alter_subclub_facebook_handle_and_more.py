# Generated by Django 4.2.5 on 2023-10-24 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportec', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subclub',
            name='email',
            field=models.EmailField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subclub',
            name='facebook_handle',
            field=models.URLField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='subclub',
            name='instagram_handle',
            field=models.URLField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='subclub',
            name='linkedin',
            field=models.URLField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='subclub',
            name='past_events',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='subclub',
            name='subleader3',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subclub',
            name='suggestion_box',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='subclub',
            name='tagline',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='subclub',
            name='upcoming_event',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='subclub',
            name='youtube_handle',
            field=models.URLField(default='', max_length=500, null=True),
        ),
    ]
