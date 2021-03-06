from django.db import models
from autoslug import AutoSlugField

class DerslerModel(models.Model):
    baslik = models.CharField(max_length=20)
    resim = models.ImageField(upload_to = "ders_resimleri")
    icerik = models.TextField(max_length=150)
    ücret = models.CharField(max_length=20)
    tür = models.CharField(max_length=30)
    #!yazar_fotografi = models.ImageField(upload_to="egitmen_resimleri")
    
    kısa_özet1 = models.CharField(max_length=50)
    kısa_özet2 = models.CharField(max_length=50)
    kısa_özet3 = models.CharField(max_length=50)
    kısa_özet4 = models.CharField(max_length=50)
    kısa_özet5 = models.CharField(max_length=50)

    kısa_özet1_tanıtım = models.TextField()
    kısa_özet1_tanıtım_baslik = models.TextField() #!max_length=50

    kısa_özet2_tanıtım = models.TextField()
    kısa_özet2_tanıtım_baslik = models.TextField()

    kısa_özet3_tanıtım = models.TextField()
    kısa_özet3_tanıtım_baslik = models.TextField()

    kısa_özet4_tanıtım = models.TextField()
    kısa_özet4_tanıtım_baslik = models.TextField()

    kısa_özet5_tanıtım = models.TextField()
    kısa_özet5_tanıtım_baslik = models.TextField()

    """ #! sınırlamaları yap ve yazar fotoğrafı ekle
    egitmen_isim = models.CharField()
    bitirme_tarihi = models.CharField()
    süre = models.CharField()
    """
    slug = AutoSlugField(populate_from = "baslik",unique=True)

    class Meta:
        db_table = "DerslerTablo"
        verbose_name = "Dersler"
        verbose_name_plural = "Ders-Ekle"

    def __str__(self):
        return self.baslik