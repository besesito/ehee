from django.shortcuts import render
from .models import Pojazd
from django.utils import timezone

def pojazdy (request):
    return render(request, 'pojazdy/pojazdy.html')

def dodaj (request):
    if request.method == 'POST':
        if request.POST['nazwa']:
            pojazd = Pojazd()
            pojazd.nazwa = request.POST['nazwa']
            pojazd.marka = request.POST['marka']
            pojazd.model = request.POST['model']
            pojazd.rejestracja = request.POST['rejestracja']
            pojazd.przeglad = request.POST['przeglad']
            pojazd.vin = request.POST['vin']
            pojazd.data_dodania = timezone.datetime.now()
            pojazd.user = request.user
            pojazd.save()
            return render(request, 'pojazdy/dodaj.html', {'info' : 'Pojazd został pymyślnie dodany'})
        return render(request, 'pojazdy/dodaj.html', {'danger' : 'Proszę wpisać nazwę pojazdu'})
    return render(request, 'pojazdy/dodaj.html')

