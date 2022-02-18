from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.messages.api import success
from django.http import request
from blog.models import YazilarModel
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class YaziSilDeleteView(LoginRequiredMixin, DeleteView):

    login_url = reverse_lazy('giris') # Eğer giriş yapmadan yazı ekle sayfasına gitmek isterse onu giriş sayfasına gönder .
    template_name = 'pages/yazi_sil_onay.html'
    success_url = reverse_lazy('yazilarim')

    def get_queryset(self):
        yazi = YazilarModel.objects.filter(slug=self.kwargs['slug'], yazar = self.request.user)
        return yazi