# Generated by Django 3.2 on 2022-08-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_alter_food_start_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='start_price',
            field=models.IntegerField(),
        ),
    ]