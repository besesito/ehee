from django.urls import path
from pojazdy import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.pojazdy, name = 'pojazdy'),
    path('dodaj', views.dodaj, name = 'dodaj'),
    path('<int:pojazd_id>', views.detail, name = 'detail'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)