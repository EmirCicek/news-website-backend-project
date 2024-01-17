from django.db import models
from django.utils.text import slugify

# Create your models here.

class Haberler(models.Model):
    haber_basligi = models.CharField(("Haber Başlığı"), max_length=200)
    slug = models.SlugField(("Slug"))
    haber_ozet = models.CharField(("Haber Özeti"), max_length=500)
    haber_icerigi = models.TextField(("Haber İçeriği"))
    haber_resmi = models.ImageField(("Haber Resmi"), upload_to='haber', max_length=1000)
    def __str__(self) -> str:
        return self.haber_basligi
