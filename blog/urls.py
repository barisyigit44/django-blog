from django.shortcuts import redirect
from django.urls import path , include
from blog.models import yorum
from blog.views import IletisimFormView ,anasayfa , KategoriListView , yazilarim, DetayView, YaziEkleCreateView, YaziGuncelleUpdateView, yorum_sil, YaziSilDeleteView
from django.views.generic import TemplateView, RedirectView


urlpatterns = [
    path('',anasayfa, name ='anasayfa'),
    path('hakkimda', TemplateView.as_view(
        template_name = 'pages/hakkimda.html'
    ), name = 'hakkimda'),
    path('email-gonderildi',TemplateView.as_view(
        template_name = 'pages/email-gonderildi.html'
    ),name='email-gonderildi'),
    path('yonlendir',RedirectView.as_view(
        url = 'https://www.google.com'
    ), name = 'yonlendir'),
    path('iletisim',IletisimFormView.as_view(), name = 'iletisim'), # Çağırabilmek için isim verdik .
    path('kategori/<slug:kategoriSlug>',KategoriListView.as_view(), name='kategori'),
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>',DetayView.as_view() , name='detay'),
    path('yazi-ekle', YaziEkleCreateView.as_view() , name='yazi-ekle'),
    path('yazi-sil/<slug:slug>', YaziSilDeleteView.as_view(), name='yazi-sil'),
    path('yorum-sil/<int:id>', yorum_sil , name='yorum-sil'),
    path('yazi-guncelle/<slug:slug>', YaziGuncelleUpdateView.as_view(), name='yazi-guncelle'),
]
