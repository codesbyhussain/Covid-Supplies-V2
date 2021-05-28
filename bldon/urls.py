from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

appname= 'bldon'
urlpatterns=[

path('',views.index, name= 'main'),
path('register/', views.donorregister, name = 'register'),
path('eligible/', views.eligible, name = 'eligible'),
path('setappointment/<int:donor_id>', views.app, name = 'appointment'),
path('register/login/',views.login, name = 'login')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
