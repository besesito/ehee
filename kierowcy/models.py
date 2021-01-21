from django.db import models
from pojazdy.models import Pojazd

class Kierowca(models.Model):
    imie = models.TextField(blank=True)
    nazwisko = models.TextField(blank=True)
    karta = models.TextField(blank=True)
    pojazd = models.ManyToManyField(Pojazd)

    def __str__(self):
        return self.nazwisko

