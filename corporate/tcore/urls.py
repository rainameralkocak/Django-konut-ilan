from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.anasayfa, name='anasayfa'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('konut-ekle/', views.ilan_ekle, name='ilan_ekle'),
    path('konutlarim/', views.ilanlarim, name='ilanlarim'),
    path('konut-guncelle/<int:id>/', views.ilan_guncelle, name='ilan_guncelle'),
    path('konut-sil/<int:id>/', views.ilan_sil, name='ilan_sil'),

    path('filtrele/', views.filtrele, name='filtrele'),
]
