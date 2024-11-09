from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_photo, name='upload_photo'),  # Ruta para el fotógrafo
   path('<int:client_id>/', views.client_gallery, name='client_gallery'),  # Ruta para la galería del cliente
]
