from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Konut

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class KonutForm(forms.ModelForm):
    class Meta:
        model = Konut
        fields = ['konut_turu', 'aciklama', 'fiyat', 'sehir', 'ilce', 'oda_sayisi', 'metrekare', 'sahip_turu', 'resim']

class KonutFilterForm(forms.Form):
    sehir = forms.ChoiceField(choices=[], required=False)
    konut_turu = forms.ChoiceField(choices=[], required=False)
    sahip_turu = forms.ChoiceField(choices=[('', 'Seçiniz'), ('sahibinden', 'Sahibinden'), ('emlakci', 'Emlakçı')], required=False)
    fiyat_min = forms.DecimalField(required=False, min_value=0)
    fiyat_max = forms.DecimalField(required=False, min_value=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Şehir ve konut türü seçeneklerini dinamik yapalım:
        from .models import Konut
        sehirler = Konut.objects.values_list('sehir', flat=True).distinct()
        konut_turleri = Konut.objects.values_list('konut_turu', flat=True).distinct()

        self.fields['sehir'].choices = [('', 'Seçiniz')] + [(s, s) for s in sehirler]
        self.fields['konut_turu'].choices = [('', 'Seçiniz')] + [(k, k) for k in konut_turleri]