from django.shortcuts import render

def pojazdy (request):
    return render(request, 'pojazdy/pojazdy.html')

def dodaj (request):
    return render(request, 'pojazdy/dodaj.html')

