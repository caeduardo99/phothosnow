from django.db import models
from django.utils.crypto import get_random_string

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='client_photos/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for {self.client.name}"
