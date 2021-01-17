from django.db import models
import datetime

class Pojazd(models.Model):
    nazwa = models.TextField()
    marka = models.TextField(blank=True)
    model = models.TextField(blank=True)
    rejestracja = models.TextField(blank=True)
    vin = models.TextField(blank=True)
    przeglad = models.DateField(default=datetime.date.today(), blank=True, null=True)
    tachograf = models.DateField(default=datetime.date.today(), blank=True, null=True)
    picture = models.ImageField(blank=True)

    def dni_przeglad(self):
        today = datetime.date.today()
        days = self.przeglad - today
        return "{} dni".format(days.days)
    def dni_tacho(self):
        today = datetime.date.today()
        days = self.tachograf - today
        return "{} dni".format(days.days)
    def __str__(self):
        return self.nazwa
    def date_przeglad(self):
        return self.przeglad.strftime("%d-%m-%Y")
    def date_tacho(self):
        return self.tachograf.strftime("%d-%m-%Y")
