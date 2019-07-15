from django.db import models

class Carro(models.Model):
    chassi = models.CharField(max_length=17, primary_key=True)
    MARCAS = (
        ('Ferrari', 'Ferrari'),
        ('Lamborghini', 'Lamborghini'),
        ('Mercedes', 'Mercedes'),
        ('Chevrolet', 'Chevrolet'),
        ('Toyota', 'Toyota'),
        ('Hyundai', 'Hyundai'),
    )
    ESTADOS = (
        ('ZeroKm', 'ZeroKm'),
        ('Seminovo', 'Seminovo'),
        ('Usado', 'Usado'),
    )
    marca = models.CharField(max_length=15, choices=MARCAS, default='Hyundai')
    modelo = models.CharField(max_length=20)
    ano = models.IntegerField(default=2000)
    cor = models.CharField(max_length=20)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='ZeroKm')
    ar_condicionado = models.BooleanField()
    vidro_eletrico = models.BooleanField()
    airbag = models.BooleanField()
    preco = models.FloatField(default=0.00)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{self.marca} {self.modelo}'.format(self=self)
