# Generated by Django 4.1.7 on 2023-05-13 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0042_subcategorymovie_slug_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategorymovie',
            name='slug_name',
        ),
        migrations.AddField(
            model_name='subcategorymovie',
            name='name1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='subcategorymovie',
            name='name2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='subcategorymovie',
            name='name3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='subcategorymovie',
            name='name4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='subcategorymovie',
            name='name5',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
