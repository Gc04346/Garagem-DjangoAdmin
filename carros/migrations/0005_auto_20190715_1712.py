# Generated by Django 2.0.4 on 2019-07-15 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0004_carro_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='marca',
            field=models.CharField(choices=[('Ferrari', 'Ferrari'), ('Lamborghini', 'Lamborghini'), ('Mercedes', 'Mercedes'), ('Chevrolet', 'Chevrolet'), ('Toyota', 'Toyota'), ('Hyundai', 'Hyundai')], default='Hyundai', max_length=2),
        ),
    ]
