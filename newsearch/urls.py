from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
appname = 'newsearch'
urlpatterns = [

                  path('newsearch/', views.index, name='search'),
                  path('details/<int:hospital_id>/', views.details, name='details'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
