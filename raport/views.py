from django.shortcuts import render
import operator

def home(request):
    return render(request, 'raport/home.html')

def raport(request):
    return render(request, 'raport/raport.html')

def wynik(request):
    if request.method == 'POST':
        fulltext = request.POST['fulltext']
        lista = []
        for x in range(1, 29):
            lista.append("Wanna {} ".format(x))
            lista.append("Oś {} ".format(x))
        slownik = {}
        for pojazd in lista:
            slownik[pojazd] = fulltext.count(pojazd)
        kursy = sorted(slownik.items(), key=operator.itemgetter(1), reverse=True)
        return render(request, 'raport/wynik.html', {'kursy': kursy })