from django.shortcuts import render, get_object_or_404
from .models import Pojazd
from django.contrib.auth.decorators import login_required

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
            try:
                pojazd.picture = request.FILES['picture']
            except:
                pass
            pojazd.save()
            return render(request, 'pojazdy/dodaj.html', {'info' : 'Pojazd został pymyślnie dodany'})
        return render(request, 'pojazdy/dodaj.html', {'danger' : 'Proszę wpisać nazwę pojazdu'})
    return render(request, 'pojazdy/dodaj.html')

@login_required(login_url="/login")
def detail(request, pojazd_id):
    pojazd = get_object_or_404(Pojazd, pk=pojazd_id)
    return render(request, 'pojazdy/detail.html', {'pojazd':pojazd})

