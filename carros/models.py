from django.db import models

class Carro(models.Model):
    chassi = models.CharField(max_length=17, primary_key=True)
    MARCAS = (
        ('FE', 'Ferrari'),
        ('LG', 'Lamborghini'),
        ('MC', 'Mercedes'),
        ('CH', 'Chevrolet'),
        ('TY', 'Toyota'),
        ('HY', 'Hyundai'),
    )
    ESTADOS = (
        ('ZK', 'ZeroKm'),
        ('SN', 'Seminovo'),
        ('US', 'Usado'),
    )
    cor = models.CharField(max_length=20)
    marca = models.CharField(max_length=2, choices=MARCAS, default='FE')
    modelo = models.CharField(max_length=20)
    estado = models.CharField(max_length=2, choices=ESTADOS, default='ZK')
    ar_condicionado = models.BooleanField()
    vidro_eletrico = models.BooleanField()
    airbag = models.BooleanField()
    preco = models.DecimalField(max_digits = 9, decimal_places=2)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{self.marca} {self.modelo}'.format(self=self)

    def getCarro():
        return self
