from django.db import models

class Articolo(models.Model):
    id = models.AutoField(primary_key=True)
    ean = models.PositiveIntegerField(default=0)
    nome = models.CharField(max_length=64)
    descrizione = models.CharField(max_length=512, blank=True, null=True)
    prezzo = models.FloatField(default=0)

    image = models.ImageField(upload_to='foto_prodotti')

    class Meta:
        verbose_name = 'Articolo'
        verbose_name_plural = 'Articoli'
