from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from lab1 import views

urlpatterns = [
    url(r'^$', views.home_index, name='home-index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
