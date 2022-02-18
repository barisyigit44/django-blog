from django.db import models
from django.contrib.auth.models import AbstractUser
from config import settings
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

class CustomUserModel(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/',blank=True, null=True)

    class Meta:
        db_table = 'user'
        verbose_name_plural = 'Kullanicilar'
        verbose_name = 'Kullanici'

    def __str__(self):
        return self.username

    def delete(self, using=None, keep_parents=False):
        self.avatar.delete(self.username)
        super().delete()


    def get_avatar(self):
        return self.avatar