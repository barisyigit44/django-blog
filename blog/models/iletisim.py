from django.db import models



class IletisimModel(models.Model):
    email = models.EmailField(max_length=50)
    isim_soyisim = models.CharField(max_length=50)
    mesaj = models.TextField(max_length=50)
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'iletisim'
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişim'

    def __str__(self):
        return self.email
