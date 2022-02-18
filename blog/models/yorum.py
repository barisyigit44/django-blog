from django import db
from django.db import models
from blog.models import YazilarModel
from blog.abstract_models import DateAbstractModel

class YorumModel(DateAbstractModel):

    yazan = models.ForeignKey('account.CustomUserModel',on_delete=models.CASCADE, related_name='yorum') # Kullanıcı silinirse yorumları da silinsin .
    yazi = models.ForeignKey(YazilarModel, on_delete=models.CASCADE, related_name='yorumlar')
    yorum = models.TextField()

    class Meta:
        db_table = 'yorum'
        verbose_name = ("Yorum")
        verbose_name_plural =  ("Yorumlar")

    def __str__(self):
        return self.yazan.username
