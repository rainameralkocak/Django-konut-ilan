from django.db import models
from django.contrib.auth.models import User

class Konut(models.Model):
    SAHIP_TURU_CHOICES = [
        ('sahibinden', 'Sahibinden'),
        ('emlakci', 'Emlakçı'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    konut_turu  = models.CharField(max_length=100)
    aciklama = models.TextField()
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    sehir = models.CharField(max_length=50)
    ilce = models.CharField(max_length=50)
    oda_sayisi = models.IntegerField()
    metrekare = models.IntegerField()
    tarih = models.DateTimeField(auto_now_add=True)
    sahip_turu = models.CharField(max_length=20, choices=SAHIP_TURU_CHOICES, default='sahibinden')
    resim = models.ImageField(upload_to='konut_resimleri/', blank=True, null=True) 


    def __str__(self):
        return self.konut_turu 
