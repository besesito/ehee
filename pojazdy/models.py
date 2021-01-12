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

    def pub_date_pretty(self):
        return self.pub_date.strftime("%d-%m-%Y")
