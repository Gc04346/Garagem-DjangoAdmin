# Generated by Django 2.0.4 on 2019-07-15 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0008_auto_20190715_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='ano',
            field=models.IntegerField(default=2000),
        ),
    ]
