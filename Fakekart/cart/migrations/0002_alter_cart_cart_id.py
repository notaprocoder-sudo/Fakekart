# Generated by Django 4.1.4 on 2023-03-01 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.IntegerField(),
        ),
    ]
