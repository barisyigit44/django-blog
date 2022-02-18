from django import forms
from django.forms import fields
from blog.models import IletisimModel
from django.core.mail import send_mail

class IletisimForm(forms.ModelForm):
    class Meta:
        model = IletisimModel
        fields = ('isim_soyisim','email','mesaj')

    def send_email(self, mesaj,email,isim_soyisim):
        send_mail(
            subject= email,
            message = mesaj + "\n Gönderenin Adı Soyadı : " +isim_soyisim,
            from_email = None,
            recipient_list = ['barisyigitw@gmail.com'],
            fail_silently = False

        )