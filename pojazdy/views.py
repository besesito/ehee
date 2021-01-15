from django.shortcuts import render
from .models import Pojazd
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import operator

@login_required(login_url="/login")
def pojazdy (request):
    lista_pojazdow = Pojazd.objects.order_by('przeglad')


    return render(request, 'pojazdy/pojazdy.html', {'pojazdy':lista_pojazdow})

@login_required(login_url="/login")
def dodaj (request):
    if request.method == 'POST':
        if request.POST['nazwa']:
            pojazd = Pojazd()
            pojazd.nazwa = request.POST['nazwa']
            pojazd.marka = request.POST['marka']
            pojazd.model = request.POST['model']
            pojazd.rejestracja = request.POST['rejestracja']
            pojazd.przeglad = request.POST['przeglad']
            pojazd.tachograf = request.POST['tachograf']
            pojazd.vin = request.POST['vin']
            pojazd.data_dodania = timezone.datetime.now()
            pojazd.save()
            return render(request, 'pojazdy/dodaj.html', {'info' : 'Pojazd został pymyślnie dodany'})
        return render(request, 'pojazdy/dodaj.html', {'danger' : 'Proszę wpisać nazwę pojazdu'})
    return render(request, 'pojazdy/dodaj.html')

