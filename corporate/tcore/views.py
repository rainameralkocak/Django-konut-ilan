from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, KonutForm,KonutFilterForm
from .models import Konut
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

# Ana sayfa
def anasayfa(request):
    return render(request, 'anasayfa.html')

# Kullanıcı Kayıt
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Kullanıcı Giriş
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('ilanlarim')
        else:
            return render(request, 'login.html', {'error': 'Kullanıcı adı veya şifre yanlış'})
    return render(request, 'login.html')

# Çıkış
def logout_view(request):
    logout(request)
    return redirect('anasayfa')

# İlan Ekle
@login_required
def ilan_ekle(request):
    if request.method == 'POST':
        form = KonutForm(request.POST, request.FILES)
        if form.is_valid():
            ilan = form.save(commit=False)
            ilan.user = request.user
            ilan.save()
            return redirect('ilanlarim')
    else:
        form = KonutForm()
    return render(request, 'ilan_ekle.html', {'form': form})

# Kendi ilanlarını listele
@login_required
def ilanlarim(request):
    ilanlar = Konut.objects.filter(user=request.user)
    return render(request, 'ilanlarim.html', {'ilanlar': ilanlar})

# Güncelle
@login_required
def ilan_guncelle(request, id):
    ilan = get_object_or_404(Konut, id=id, user=request.user)
    if request.method == 'POST':
        form = KonutForm(request.POST, request.FILES, instance=ilan)  
        if form.is_valid():
            form.save()
            return redirect('ilanlarim')
    else:
        form = KonutForm(instance=ilan)
    return render(request, 'ilan_güncelle.html', {'form': form})


# Sil
@login_required
def ilan_sil(request, id):
    ilan = get_object_or_404(Konut, id=id, user=request.user)
    if request.method == 'POST':
        ilan.delete()
        return redirect('ilanlarim')
    return render(request, 'ilan_sil.html', {'ilan': ilan})

# Filtrele
def filtrele(request):
    ilanlar = Konut.objects.all()
    sehir = request.GET.get('sehir')
    oda = request.GET.get('oda')
    fiyat_min = request.GET.get('fiyat_min')
    fiyat_max = request.GET.get('fiyat_max')

    if sehir:
        ilanlar = ilanlar.filter(sehir__icontains=sehir)
    if oda:
        ilanlar = ilanlar.filter(oda_sayisi=oda)
    if fiyat_min:
        ilanlar = ilanlar.filter(fiyat__gte=fiyat_min)
    if fiyat_max:
        ilanlar = ilanlar.filter(fiyat__lte=fiyat_max)

    return render(request, 'filtrele.html', {'ilanlar': ilanlar})


@login_required
def ilanlarim(request):
    form = KonutFilterForm(request.GET or None)

    ilanlar = Konut.objects.filter(user=request.user)  # sadece kullanıcının ilanları

    if form.is_valid():
        sehir = form.cleaned_data.get('sehir')
        konut_turu = form.cleaned_data.get('konut_turu')
        sahip_turu = form.cleaned_data.get('sahip_turu')
        fiyat_min = form.cleaned_data.get('fiyat_min')
        fiyat_max = form.cleaned_data.get('fiyat_max')

        if sehir:
            ilanlar = ilanlar.filter(sehir=sehir)
        if konut_turu:
            ilanlar = ilanlar.filter(konut_turu=konut_turu)
        if sahip_turu:
            ilanlar = ilanlar.filter(sahip_turu=sahip_turu)
        if fiyat_min is not None:
            ilanlar = ilanlar.filter(fiyat__gte=fiyat_min)
        if fiyat_max is not None:
            ilanlar = ilanlar.filter(fiyat__lte=fiyat_max)

    context = {
        'form': form,
        'ilanlar': ilanlar,
    }
    return render(request, 'ilanlarim.html', context)