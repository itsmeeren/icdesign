

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('events/', views.events_view, name='events'),
    path('events/<int:event_id>/', views.event_detail_view, name='event_detail'),
    path('aboutus', views.aboutus, name='AboutUs'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
