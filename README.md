Sahibinden Kiralık Konut İlanları Uygulaması
Bu proje, Django framework kullanılarak geliştirilmiş, kullanıcıların kiralık ve satılık konut ilanları oluşturup yönetebileceği bir web uygulamasıdır. Sahibinden.com ana sayfasına benzer şekilde responsive ve modern bir tasarıma sahiptir.
Özellikler
•	Kullanıcı kaydı ve giriş işlemleri (Django User modeli ile)
•	Konut ilanları oluşturma, güncelleme ve silme
•	İlanlarda şehir, konut türü, sahip türü ve fiyat aralığına göre filtreleme
•	Bootstrap 5 ile responsive ve modern UI tasarımı
•	Fiyatların okunabilirliği için `humanize` filtreleri kullanımı
Teknolojiler
•	Python 3.11
•	Django 5.2.1
•	SQLite (varsayılan veritabanı)
•	Bootstrap 5
•	Django Crispy Forms (isteğe bağlı)
Kurulum
Depoyu klonlayın:

```bash
git clone <repo-url>
cd <proje-dizini>
```
Sanal ortam oluşturun ve aktif edin:

```bash
python -m venv env
source env/bin/activate  # Windows için: env\Scripts\activate
```
Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```
Veritabanını oluşturun ve migrate edin:

```bash
python manage.py migrate
```
Superuser oluşturun (isteğe bağlı):

```bash
python manage.py createsuperuser
```
Projeyi başlatın:

```bash
python manage.py runserver
```
Tarayıcıda açın: http://127.0.0.1:8000
Dikkat Edilmesi Gerekenler
•	`django.contrib.humanize` uygulaması `INSTALLED_APPS` içine eklenmelidir.
•	Bootstrap CSS ve JS dosyaları CDN üzerinden dahil edilmiştir.
•	Form alanları için `widget_tweaks` gibi paketler kullanılmış olabilir, kurulu olmasına dikkat edin.
Proje Dosya Yapısı
corporate/
├── tcore/                # Ana uygulama
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── anasayfa.html
│   │   ├── ilanlarim.html
│   │   └── ...
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── corporate/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── manage.py
└── requirements.txt


