import os
from django.template import base
from django.views.generic import DetailView
from account.models import CustomUserModel
from django.shortcuts import get_object_or_404, render
from blog.models.yazi import YazilarModel
from django.core.paginator import Paginator

from config import settings

class ProfilDetailView(DetailView):
    template_name = 'pages/profil.html'
    context_object_name = 'profil'

    def get_object(self):
        return get_object_or_404(
            CustomUserModel, username=self.kwargs.get('username')
        )