from django.shortcuts import render
from AppMy.models import *
from django.utils.text import slugify

# Create your views here.

def indexPage(request ):
    haberler = Haberler.objects.all()
    context = {
        'haberler':haberler,
    }
    return render(request, 'index.html',context)


def girisPage(request):
    context = {}
    return render(request, 'giris_yap.html',context)

def haber_eklePage(request):
    if request.method == "POST":
        haber_baslik = request.POST.get('baslik')
        haber_ozet = request.POST.get('haber_ozet')
        haber_icerik = request.POST.get('haber_icerik')
        haber_resim = request.FILES.get('haber_resim')
        haberler = Haberler(haber_basligi=haber_baslik, haber_ozet=haber_ozet, haber_icerigi=haber_icerik, haber_resmi=haber_resim,slug=slugify(haber_baslik))
        haberler.save()

    context = {}
    return render(request, 'haber_ekle.html',context)

def detailsPage(request,slug):
    haber = Haberler.objects.get(slug=slug)
    context = {
        'haber':haber
    }
    return render(request, 'details.html',context)


def denemePage(request):
    data = Haberler.objects.all()
    context = {
        'data':data
    }
    return render(request, 'deneme.html',context)