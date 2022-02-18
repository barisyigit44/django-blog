from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy
from blog.forms.yazi_guncelle import YaziGuncelleFormModel
from blog.models import YazilarModel
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin




class YaziGuncelleUpdateView(LoginRequiredMixin,UpdateView):

    login_url = reverse_lazy('giris') # Eğer giriş yapmadan yazı ekle sayfasına gitmek isterse onu giriş sayfasına gönder .
    template_name = 'pages/yazi-guncelle.html'
    fields = ('baslik','icerik','resim','kategoriler')

    def get_object(self):
        yazi = get_object_or_404(
            YazilarModel,
            slug = self.kwargs.get('slug'),
            yazar= self.request.user
        )
        return yazi
    
    def get_success_url(self):
        return reverse('detay', kwargs={
            'slug' : self.get_object().slug
        })
    