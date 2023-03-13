# Generated by Django 4.1.7 on 2023-03-13 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0005_shop_remove_detailshop_add_delete_categoryshop_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='photos',
            new_name='cover',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='items',
            new_name='stock',
        ),
        migrations.CreateModel(
            name='DetailShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=2000)),
                ('photos', models.CharField(max_length=2000)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp.shop')),
            ],
        ),
    ]
