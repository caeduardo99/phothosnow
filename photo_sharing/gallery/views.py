from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Photo
from django.conf import settings
import qrcode
import os

import os
from django.conf import settings
import qrcode

def upload_photo(request):
    if request.method == 'POST' and request.FILES.getlist('photos'):
        client_id = request.POST.get('client_id')
        client = get_object_or_404(Client, id=client_id)
        
        # Guardar cada foto asociada al cliente
        for photo_file in request.FILES.getlist('photos'):
            photo = Photo(client=client, image=photo_file)
            photo.save()

        # Generar enlace a la galería del cliente y el código QR
        gallery_link = f"{settings.SITE_URL}/gallery/{client.id}/"
        qr = qrcode.make(gallery_link)

        # Asegurar que el directorio qr_codes existe
        qr_directory = os.path.join(settings.MEDIA_ROOT, 'qr_codes')
        os.makedirs(qr_directory, exist_ok=True)
        
        # Guardar el QR en el directorio qr_codes
        qr_path = os.path.join(qr_directory, f'client_{client.id}_qr.png')
        qr.save(qr_path)

        # Guardar la ruta relativa del QR en el modelo del cliente
        client.qr_code = os.path.join('qr_codes', f'client_{client.id}_qr.png')
        client.save()

        return render(request, 'upload_success.html', {'client': client, 'qr_path': client.qr_code})
    
    clients = Client.objects.all()
    return render(request, 'upload_photo.html', {'clients': clients})


def client_gallery(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    photos = client.photos.all()  # Asegúrate de que `photos` es el nombre del campo de relación
    return render(request, 'client_gallery.html', {'client': client, 'photos': photos})