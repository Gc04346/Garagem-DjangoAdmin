# Generated by Django 2.0.4 on 2019-07-13 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='estado',
            field=models.CharField(choices=[('ZK', 'ZeroKm'), ('SN', 'Seminovo'), ('US', 'Usado')], default='ZK', max_length=2),
        ),
        migrations.AlterField(
            model_name='carro',
            name='modelo',
            field=models.CharField(choices=[('FE', 'Ferrari'), ('LG', 'Lamborghini'), ('MC', 'Mercedes'), ('CH', 'Chevrolet'), ('TY', 'Toyota'), ('HY', 'Hyundai')], default='FE', max_length=2),
        ),
    ]
