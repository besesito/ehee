from django.urls import path
from raport import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.raport, name = 'pojazdy'),
    path('/dodaj', views.raport, name = 'dodaj'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)