from django.shortcuts import render, get_object_or_404
from .models import Kierowca
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")
def kierowcy(request):
    lista = Kierowca.objects.all()

    return render(request, 'kierowcy/kierowcy.html', {'lista':lista})