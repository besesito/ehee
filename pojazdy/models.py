from django.db import models
import datetime

class Pojazd(models.Model):
    nazwa = models.TextField()
    marka = models.TextField()
    model = models.TextField()
    rejestracja = models.TextField()
    vin = models.TextField()
    przeglad = models.DateField()
    tachograf = models.DateField()
    data_dodania = models.DateTimeField()
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