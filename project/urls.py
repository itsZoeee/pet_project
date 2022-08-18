from django.contrib import admin
from django.urls import path
from mysite import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('adoptPets/', views.adoptPets, name="adoptData"),
    path('lostPets/', views.lostPets, name="lostData"),
    path('fancyCard/', views.fancyCard),
    path('dogBreed/', views.dogBreed),
    path('upload/', views.upload, name="upload"),
    path('uploadLost/', views.uploadLost, name="uploadLost"),
    path('analysisBreed/', views.analysisBreed),
    path('analysis/', views.analysis),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)