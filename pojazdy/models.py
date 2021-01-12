from django.db import models
from django.contrib.auth.models import User

class Pojazd(models.Model):
    nazwa = models.TextField()
    marka = models.TextField()
    model = models.TextField()
    rejestracja = models.TextField()
    vin = models.TextField()
    przeglad = models.DateField()
    data_dodania = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nazwa