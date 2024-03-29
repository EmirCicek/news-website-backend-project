# Generated by Django 5.0.1 on 2024-01-09 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Haberler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('haber_basligi', models.CharField(max_length=200, verbose_name='Haber Başlığı')),
                ('haber_ozet', models.CharField(max_length=200, verbose_name='Haber Özeti')),
                ('haber_icerigi', models.TextField(verbose_name='Haber İçeriği')),
                ('haber_resmi', models.ImageField(max_length=1000, upload_to='', verbose_name='')),
            ],
        ),
    ]
