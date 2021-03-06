# Generated by Django 4.0 on 2021-12-31 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_yorummodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='IletisimModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('isim_soyisim', models.CharField(max_length=50)),
                ('mesaj', models.TextField(max_length=50)),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'İletişim',
                'verbose_name_plural': 'İletişim',
                'db_table': 'iletisim',
            },
        ),
    ]
