from django.db import models
import datetime

class Pojazd(models.Model):
    nazwa = models.TextField()
    marka = models.TextField(blank=True)
    model = models.TextField(blank=True)
    rejestracja = models.TextField(blank=True)
    vin = models.TextField(blank=True)
    firma = models.TextField(blank=True)
    przeglad = models.DateField(blank=True, null=True)
    legalizacja = models.DateField(blank=True, null=True)
    tachograf_info = models.TextField(blank=True)
    pobrane_dane = models.BooleanField(default=False)
    picture = models.ImageField(blank=True)

    def dni_przeglad(self):
        if self.przeglad == None:
            pass
        else:
            today = datetime.date.today()
            days = self.przeglad - today
            return days.days
    def dni_tacho(self):
        if self.legalizacja == None:
            pass
        else:
            today = datetime.date.today()
            days = self.legalizacja - today
            return days.days
    def __str__(self):
        return self.nazwa
    def date_przeglad(self):
        if self.przeglad == None:
            pass
        else:
            return self.przeglad.strftime("%d-%m-%Y")

    def przeglad_edit(self):
        if self.przeglad == None:
            pass
        else:
            return self.przeglad.strftime("%Y-%m-%d")

    def date_tacho(self):
        if self.legalizacja == None:
            pass
        else:
            return self.legalizacja.strftime("%d-%m-%Y")

    def tacho_edit(self):
        if self.legalizacja == None:
            pass
        else:
            return self.legalizacja.strftime("%Y-%m-%d")
