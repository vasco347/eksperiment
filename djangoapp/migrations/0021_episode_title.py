# Generated by Django 4.1.7 on 2023-03-23 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0020_season_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
