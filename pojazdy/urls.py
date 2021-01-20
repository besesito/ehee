from django.urls import path
from pojazdy import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.pojazdy, name = 'pojazdy'),
    path('przeglady', views.przeglady, name = 'przeglady'),
    path('dodaj', views.dodaj, name = 'dodaj'),
    path('tachografy', views.tachografy, name = 'tachografy'),
    path('<int:pojazd_id>', views.detail, name = 'detail'),
    path('edit/<int:pojazd_id>', views.edit, name = 'edit'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)