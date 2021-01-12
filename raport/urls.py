from django.urls import path
from raport import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.raport, name = 'raport'),
    path('wynik', views.wynik, name = 'wynik'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)