###### Nama aplikasi:
# 📖 librory 📚
###### Nama: Michelle Elizabeth Amanda Hutasoit
###### Kelas: PBP C

###### Aplikasi Adaptable yang sudah di-deploy: [link](https://librory.adaptable.app)

## 1. Cara mengimplementasikan checklist:
### Tugas 2
#### 2.1 Membuat sebuah proyek Django baru
Untuk dapat membuat sebuah proyek Django baru, dibutuhkan sebuah direktori yang telah terhubung ke suatu repositori Git. Maka dari itu, saya **membuat direktori dengan nama ```librory``` yang terhubung dengan repositori Git yang bernama ```librory```** juga. Setelah itu, saya membuat dan **mengaktifkan virtual environment** pada direktori ```librory``` agar package dan dependencies dari aplikasi tidak bertabrakan dengan versi lain yang ada di komputer saya.

Setelah berhasil melakukan set up, saya membuat berkas yang berisi dependencies yang akan saya butuhkan dalam mengembangkan aplikasi, yaitu **django, gunicorn, whinoise, psycopg2-binary, requests, dan urllib3**. Melalui berkas tersebut, saya **meng-install dependencies** yang telah dispesifikasikan dan **membuat proyek Django dengan nama ```librory```**. Proses tersebut saya lakukan dengan menjalankan perintah **```django-admin startproject librory .```**, perintah tersebut akan membuat proyek Django baru dengan nama ```librory```. Titik yang dituliskan pada akhir perintah dimaksudkan agar proyek dibuat tepat di direktori di mana saya sedang bekerja tanpa membuat sebuah folder untuk proyek tersebut.

#### 2.2 Membuat aplikasi dengan nama ```main``` pada proyek tersebut
Sama seperti yang sebelumnya dilakukan saat membuat sebuah proyek Django baru, virtual environment pada direktori terkait, dalam hal ini direktori ```librory```, harus diaktifkan terlebih dahulu. Setelah itu, saya **membuat aplikasi dengan nama ```main```** dengan menjalankan perintah **```python manage.py startapp main```**. Perintah tersebut akan membuat aplikasi baru bernama ```main``` di dalam proyek Django terkait dan aplikasi akan berada dalam konteks dan pengaturan yang sama dengan proyek. Akan tetapi, meskipun aplikasi ```main``` telah berhasil dibuat, aplikasi belum terdaftar ke dalam proyek, maka dari itu saya **menambahkan aplikasi ```main``` ke dalam list ```INSTALLED_APPS``` yang berada di berkas ```settings.py```**.

#### 2.3 Melakukan routing pada proyek agar dapat menjalankan aplikasi main
Untuk melakukan routing, saya **membuat berkas ```urls.py``` di dalam direktori ```main```** dan **mengimport ```path``` dari ```django.urls```** untuk mendefinisikan pola URL. Berkas ```urls.py``` yang dibuat di dalam direktori ```main``` ditujukan untuk mengatur rute URL pada aplikasi ```main```. Sebelumnya, pada berkas ```views.py```, saya telah menambahkan fungsi ```show_main``` sebagai tampilan, maka dari itu saya **mengimport fungsi ```show_main```** untuk kemudian ditampilkan ketika URL terkait diakses. Saya juga **menambahkan variabel bernama ```app_name```** yang kemudian digunakan untuk memberikan nama unik pada pola URL dalam aplikasi. 

#### 2.4 Membuat model pada aplikasi main dengan nama ```Item``` dan memiliki atribut:
1. ```name``` dengan tipe CharField: judul buku
2. ```amount``` dengan tipe IntegerField: jumlah buku
3. ```rented``` dengan tipe IntegerField: jumlah buku yang disewa
4. ```category``` dengan tipe CharField: kategori buku
5. ```description``` dengan tipe TextField: deskripsi/sinopsis buku

Untuk membuat model pada aplikasi ```main``` sesuai dengan class dan atribut yang saya inginkan, saya terlebih dahulu **mengimport modul ```models``` dari modul ```django.db```**. Setelah itu, saya **membuat class dengan nama ```Item``` yang menerima parameter ```models.Model```**, parameter tersebut merupakan kelas dasar yang akan digunakan untuk mendefinisikan model dalam Django. Di dalam class ```Item```, saya **menambahkan atribut ```name``` dengan tipe CharField** yang hanya menerika karakter dengan panjang maksimal 255 karakter, **atribut ```amount``` dengan tipe IntegerField**, **atribut ```rented``` dengan tipe IntegerField**, **atribut ```category``` dengan tipe CharField** yang hanya menerika karakter dengan panjang maksimal 255 karakter, dan **atribut ```description``` dengan tipe TextField**.

#### 2.5 Membuat sebuah fungsi pada ```views.py``` untuk dikembalikan ke dalam sebuah template ```HTML``` yang menampilkan nama aplikasi, nama, dan kelas
Sebelum saya membuat fungsi pada berkas ```views.py```, saya terlebih dahulu **mengimport ```render``` dari modul ```django.shortcuts```** untuk me-render tampilan HTML dengan data yang akan diintegrasikan melalui fungsi. Setelah itu, saya **membuat fungsi dengan nama ```show_main``` pada berkas ```views.py```** sebagai data acuan yang kemudian akan ditampilkan pada tampilan ```HTML```. 

Saya **membuat sebuah dictionary dengan nama ```context```** yang berisi **key ```app_name``` dengan value ```librory```**, **key ```name``` dengan value ```Michelle Elizabeth Amanda Hutasoit```**, dan **key ```class``` dengan value ```PBP C```**. **Fungsi ```show_main``` akan me-return ```render(request, "main.html", context)```** di mana fungsi ```render``` akan me-render tampilan berdasarkan request/objek HTTP yang dikirim oleh pengguna pada berkas template ```main.html```, dengan dictionary ```context``` yang berisi data yang akan digunakan dan ditampilkan dalam tampilan dinamis.

Setelah selesai melakukan set up pada berkas ```views.py```, saya kemudian memodifikasi template pada berkas ```main.html``` agar data pada dictionary ```context``` dapat digunakan. Saya **menambahkan ```{{ app_name }}```, ```{{ name }}```, dan ```{{ class }}```** pada template sesuai dengan posisi yang diinginkan untuk menampilkan value dari variabel yang telah didefinisikan dalam dictionary ```context```.

#### 2.6 Membuat sebuah routing pada ```urls.py``` aplikasi main untuk memetakan fungsi yang telah dibuat pada ```views.py```
Setelah berhasil melakukan set up pada aplikasi ```main```, saya mengonfigurasi routing URL pada proyek ```librory```. Jika berkas ```urls.py``` pada aplikasi ```main``` ditujukan untuk mengatur rute URL pada aplikasi ```main```, maka berkas ```urls.py``` pada proyek ```librory``` ditujukan untuk mengatur rute URL pada tingkat proyek. Pada direktori ```librory```, telah terdapat berkas ```urls.py``` sehingga saya tidak perlu membuat berkas tersebut kembali. Pada berkas tersebut, saya **mengimport fungsi ```include```** untuk mengimpor rute URL dari aplikasi ```main``` **ke dalam berkas ```urls.py``` proyek ```librory```**. Saya juga **menambahkan ```path('main/', include('main.urls'))```** pada list urlpatterns agar path url ```main/``` akan diarahkan ke rute yang didefinisikan dalam berkas ```urls.py``` pada aplikasi ```main```.

#### 2.7 Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat
Untuk melakukan deployment ke Adaptable, saya terlebih dahulu **melakukan add, push, dan commit perubahan pada direktori kepada repositori**. Hal ini dilakukan karena deployment akan dihubungkan dengan akun GitHub serta repositori yang berkaitan. Setelah selesai menambahkan perubahan pada repositori, saya **membuat akun Adaptable.io** menggunakan akun GitHub dan **menekan tombol ```New App```**. Saya **memilih opsi ```Connect an Existing Repository```** dan **memilih repositori ```librory```** karena saya ingin men-deploy aplikasi tersebut. Saya **memilih branch ```main```** sebagai deployment branch, kemudian saya **memilih ```Python App Template```** sebagai template deployment, serta **```PostgreSQL```** sebagai tipe basis data yang akan digunakan. Setelah itu, saya **memilih versi ```Python 3.10```** sesuai versi Python yang saya install dan **memasukkan perintah ```python manage.py migrate && gunicorn librory.wsgi```** pada bagian Start Command. Setelah itu, saya **memasukkan ```librory``` sebagai nama aplikasi**, **mencentang bagian ```HTTP Listener on PORT```**, dan men-deploy aplikasi dengan **menekan tombol ```Deploy App```**. Apabila terdapat perubahan/pembaruan pada repositori, saya akan menekan tombol dengan tiga titik dan me-redeploy aplikasi.

### Tugas 3
#### 3.1 Membuat input ```form``` untuk menambahkan objek model pada app sebelumnya
Sebelum saya membuat form registrasi, saya **membuat skeleton** sebagai kerangka views dari aplikasi saya agar desain lebih konsisten dan redundansi kode dapat diminimalisir. Saya membuat skeleton dengan **membuat folder ```templates``` pada root folder** dan **menambahkan berkas ```base.html```** pada folder tersebut. Berkas ```base.html``` akan digunakan sebagai kerangka umum untuk halaman aplikasi lainnya dalam proyek.

Setelah itu, agar skeleton dapat terdeteksi sebagai berkas template dan digunakan kerangka umum, saya menambahkan kode **```'DIRS': [BASE_DIR / 'templates']``` ke dalam variabel ```TEMPLATES```** di dalam berkas ```settings.py``` pada subdirektori ```librory```. Saya juga mengganti kode pada berkas ```main.html``` pada subdirektori ```templates``` yang ada pada direktori ```main``` dengan menggunakan ```main.html``` sebagai template utama.

Dalam pembuatan form registrasi, saya **membuat berkas baru dengan nama ```forms.py``` pada direktori ```main```** untuk membuat struktur form yang dapat menerima data item baru. Saya menambahkan kode
```
from django.forms import ModelForm
from main.models import Item

class ProductForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "rented", "category", "description"]
```
- ```model = Item``` ditujukan agar isi dari form akan disimpan menjadi sebuah objek Item.
- ```fields = ["name", "amount", "rented", "category", "description"]``` menunjukkan field dari model Item yang digunakan untuk form.

Setelah itu saya **membuka berkas ```views.py```** yang ada pada folder ```main``` dan **mengimport beberapa modul** sebagai berikut:
```
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
```
Saya juga **membuat fungsi baru dengan nama ```create_item```** yang menerima parameter ```request``` dan menambahkan kode sebagai berikut:
```
def create_item(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```
- ```form = ProductForm(request.POST or None)``` digunakan untuk membuat ```ProductForm``` baru dengan mamsukkan QueryDict berdasarkan input dari user pada ```request.POST```
- ```form.is_valid()``` digunakan untuk memvalidasi isi input dari form
- ```form.save()``` digunakan untuk membuat dan menyimpan data dari form
- ```return HttpResponseRedirect(reverse('main:show_main'))``` digunakan untuk melakukan redirect ke halaman aplikasi awal setelah data form berhasil disimpan

Setelah itu, saya **menambahkan kode ```items = Item.objects.all()```** pada fungsi ```show_main``` di berkas ```views.py``` pada folder ```main``` untuk mengambil seluruh objek Item yang telah tersimpan pada database. Setelah memperbarui fungsi ```show_main``` dan membuat fungsi ```create_item```, saya **membuka berkas ```urls.py```** pada folder ```main``` dan **mengimport fungsi ```create_item```** yang telah dibuat sebelumnya. Saya juga menambahkan path url ke dalam ```urlpatterns``` agar fungsi ```create_item``` dapat diakses. Saya **menambahkan path url dengan menambahkan kode ```path('create-item', create_item, name='create_item'),```**.

Kemudian saya **membuat berkas ```create_item.html```** pada direktori ```main/templates``` dan mengisi berkas tersebut dengan kode sebagai berikut:
```
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
- ```<form method="POST">``` digunakan untuk menandakan block untuk form dengan metode POST
- ```{% csrf_token %}``` digunakan sebagai security untuk mencegah serangan berbahaya
- ```{{ form.as_table }}``` digunakan untuk menampilkan fields form yang sudah dibuat pada ```forms.py``` sebagai table
- ```<input type="submit" value="Add Item"/>``` digunakan sebagai tombol submit untuk mengirimkan request ke view ```create_item(request)``


#### 3.2 Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format ```HTML```, ```XML```, ```JSON```, ```XML by ID```, dan ```JSON by ID```
Pertama-tama, saya membuka berkas ```views.py``` pada folder ```main``` dan **mengimport ```HttpResponse```** untuk menginformasikan ```client``` dan ```Serializer``` untuk mengubah objek ke dalam suatu format yang memudahkan transmisi data dalam jaringan atau penyimpanan dalam database. Untuk mengimport keduanya, saya menambahkan kode sebagai berikut:
```
from django.http import HttpResponse
from django.core import serializers
```

- Untuk melihat objek yang ditambahkan dalam format HTML saya menggunakan fungsi ```show_main```
- Untuk melihat objek yang ditambahkan dalam format XML saya membuat fungsi ```show_xml```
- Untuk melihat objek yang ditambahkan dalam format JSON saya membuat fungsi ```show_json```
- Untuk melihat objek yang ditambahkan dalam format XML by ID saya membuat fungsi ```show_xml_by_id```
- Untuk melihat objek yang ditambahkan dalma format JSON by ID saya membuat fungsi ```show_xml_by_id```

##### Format HTML
Saya **menambahkan kode di dalam ```{% block content %}```** pada berkas ```main.html``` untuk menampilkan data produk dalam bentuk table serta tombol ```Add New Item``` yang akan redirect ke halaman form. Kode yang ditambahkan adalah sebagai berikut:
```
<table>
    <tr>
        <th>Name</th>
        <th>Amount</th>
        <th>Rented</th>
        <th>Category</th>
        <th>Description</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for item in items %}
        <tr>
            <td>{{item.name}}</td>
            <td>{{item.amount}}</td>
            <td>{{item.rented}}</td>
            <td>{{item.category}}</td>
            <td>{{item.description}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_item' %}">
    <button>
        Add New Item
    </button>
</a>

{% endblock content %}
```

##### Format XML
Saya **membuat fungsi bernama ```show_xml```** pada berkas ```views.py``` dalam folder ```main``` yang menerima parameter request dengan kode sebagai berikut:
```
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
- ```data = Item.objects.all()``` digunakan untuk menyimpan hasil query dari seluruh data yang ada pada Item
- ```return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")``` digunakan untuk mereturn ```HttpResponse``` berisi parameter data hasil query yang diserialisasi oleh ```serializers``` menjadi XML

##### Format JSON
Saya **membuat fungsi bernama ```show_json```** pada berkas ```views.py``` dalam folder ```main``` yang menerima parameter request dengan kode sebagai berikut:
```
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
- ```data = Item.objects.all()``` digunakan untuk menyimpan hasil query dari seluruh data yang ada pada Item
- ```return HttpResponse(serializers.serialize("json", data), content_type="application/json")``` digunakan untuk mereturn ```HttpResponse``` berisi parameter data hasil query yang diserialisasi oleh ```serializers``` menjadi JSON

##### Format XML by ID
Saya **membuat fungsi bernama ```show_xml_by_id```** pada berkas ```views.py``` dalam folder ```main``` yang menerima parameter request dan id dengan kode sebagai berikut:
```
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
- ```data = Item.objects.filter(pk=id)``` digunakan untuk menyimpan hasil query dari data yang ada pada Item sesuai dengan id
- ```return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")``` digunakan untuk mereturn ```HttpResponse``` berisi parameter data hasil query yang diserialisasi oleh ```serializers``` menjadi XML

##### Format JSON by ID
Saya **membuat fungsi bernama ```show_json_by_id```** pada berkas ```views.py``` dalam folder ```main``` yang menerima parameter request dan id dengan kode sebagai berikut:
```
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
- ```data = Item.objects.filter(pk=id)``` digunakan untuk menyimpan hasil query dari data yang ada pada Item sesuai dengan id
- ```return HttpResponse(serializers.serialize("json", data), content_type="application/json")``` digunakan untuk mereturn ```HttpResponse``` berisi parameter data hasil query yang diserialisasi oleh ```serializers``` menjadi JSON

#### 3.3 Membuat ```routing URL``` untuk masing-masing views yang telah ditambahkan
Setelah selesai membuat seluruh fungsi yang dibutuhkan, saya membuka berkas ```urls.py``` pada folder ```main``` dan **mengimport seluruh fungsi yang telah dibuat** sebelumnya. Saya mengimport seluruh fungsi dengan kode sebagai berikut:
```
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
```
Setelah itu, saya **menambahkan path url ke dalam ```urlpatterns```** untuk mengakses fungsi yang sudah diimport dengan kode sebagai berikut:
```
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id')
]
```
### Tugas 4
#### 4.1 Mengimplementasikan fungsi ```registrasi```, ```login```, dan ```logout``` untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar
Sebelum mengimplementasikan fungsi ```registrasi```, ```login```, dan ```logout```, saya mengimport beberapa modul yang dibutuhkan sebagai berikut pada berkas ```view.py``` pada subdirektori ```main```:
```
from django.shortcuts import redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  
```
- ```login_required``` digunakan untuk mengharuskan pengguna masuk/login sebelum dapat mengakses aplikasi
- ```UserCreationForm``` adalah formulir bawaan yang akan digunakan sebagai template pembuatan formulir pendaftaran pengguna dalam aplikasi
- ```authenticate``` adalah fungsi yang akan digunakan untuk melakukan autentikasi pengguna dalam aplikasi
- ```login``` adalah fungsi yang akan digunakan untuk melakukan login jika autentikasi pengguna dalam aplikasi berhasil
- ```logout``` adalah fungsi yang akan digunakan untuk melakukan logout

Setelah mengimport seluruh modul yang dibutuhkan, saya membuat fungsi ```register``` pada berkas ```view.py``` pada subdirektori ```main``` untuk menghasilkan formulir registrasi secara otomatis. Fungsi ini juga akan menghasilkan akun pengguna ketika form disubmit. Isi dari fungsi tersebut adalah 

#### 4.2 Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal
Saya menekan text "Register Now" dan mengisi fields username, password, dan password confirmation. Setelah selesai mengisi seluruh fields, saya menekan tombol daftar untuk mendaftarkan akun. Setelah berhasil membuat akun, saya kembali ke halaman login dan mengisi fields username dan password sesuai dengan akun yang telah saya buat sebelumnya.
Untuk menambahkah data dummy, saya menekan tombol add new item dan mengisi fields name, amount, rented, category, dan description. Setelah selesai mengisi seluruh fields, saya menekan tombol add item dan item yang telah ditambahkan akan muncul pada tabel di main page. 

#### 4.3 Menghubungkan model ```Item``` dengan ```User```
Untuk menghubungkan model ```Item``` dengan ```User```, saya membuka ```models.py``` yang ada pada subdirektori ```main``` dan mengimport User dengan potongan kode sebagai berikut:
```
from django.contrib.auth.models import User
```
Setelah itu, pada model ```Item```, saya menambahkan atribut ```user``` dengan potongan kode sebagai berikut:
```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
Potongan kode tersebut berfungsi untuk menghubungkan satu produk dengan satu user melalui sebuah relationship sehingga suatu produk pasti terasosiasikan dengan seorang user.
Setelah itu, saya membuka berkas ```views.py``` pada subdirektori ```main``` dan mengubah potongan kode pada fungsi ```create_item``` menjadi sebagai berikut:
```
if form.is_valid() and request.method == "POST":
     item = form.save(commit=False)
     item.user = request.user
     item.save()
     return HttpResponseRedirect(reverse('main:show_main'))
```
- ```item = form.save(commit=False)``` digunakan untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari form ke database dan memungkinkan pengguna untuk memodifikasi objek sebelum disimpan ke database.
- ```item.user = request.user``` digunakan untuk mengisi field ```user``` dengan objek ```User``` yang sedang terotorisasi untuk menandakan bahwa objek tersebut dimiliki oleh pengguna yang sedang login.

Setelah itu, saya mengubah fungsi ```show_main``` menjadi sebagai berikut:
```
items = Item.objects.filter(user=request.user)
```
dan mengubah value dari key ```name``` pada dictionary ```context``` menjadi ```request.user.username```.
- ```items = Item.objects.filter(user=request.user)``` digunakan untuk menampikan objek ```Item``` yang terasosiasi dengan pengguna yang sedang login. 
- ```request.user.username``` digunakan untuk menampilkan username pengguna yang sedang login pada halaman main.

Setelah itu saya melakukan migrasi dengan menjalankan perintah ```python manage.py makemigrations```, saya memilih pilihan 1 untuk menetapkan default value untuk field user pada semua row yang telah dibuat pada basis data dan memilih pilihan 1 lagi untuk menetapkan user dengan ID 1 pada model yang sudah ada. Setelah itu saya melakukan migrasi dengan menjalankan perintah ```python manage.py migrate```.

#### 4.4 Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan ```cookies``` seperti ```last login``` pada halaman utama aplikasi
Untuk menampilkan detail informasi pengguna yang sedang logged in dan menerapkan cookies pada halaman utama aplikasi, saya membuka berkas ```views.py``` pada subdirektori ```main``` dan meng-import beberapa modul sebagai berikut:
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
- ```import datetime``` digunakan untuk mengimport datetime yang kemudian akan digunakan untuk menyimpan waktu saat user log in.
- ```from django.http import HttpResponseRedirect``` digunakan untuk mengimport HttpResponseRedirect yang kemudian akan digunakan untuk redirect user ke halaman yang ditujukan.
- ```from django.urls import reverse``` digunakan untuk mengimport reverse yang kemudian akan digunakan untuk mengakses URL secara backward.

Setelah itu, pada fungsi ```login_user```, saya mengganti kode pada fungsi ```login_user``` menjadi sebagai berikut:
```
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```
- ```login(request, user)``` digunakan untuk mengarahkan user untuk login terlebih dahulu.
- ```response = HttpResponseRedirect(reverse("main:show_main"))``` digunakan untuk membuat response.
- ```response.set_cookie('last_login', str(datetime.datetime.now()))``` digunakan untuk membuat cookie ```last_login``` dan menambahkannya ke dalam response.

Setelah itu, pada fungsi ```show_main```, saya menambahkan key ```last_login``` dengan value ```request.COOKIES['last_login']``` ke dalam dictionary ```context``` untuk menambahkan informasi cookie ```last_login``` pada response yang akan ditampilkan di halaman web. Setelah itu saya mengubah fungsi ```logout_user``` menjadi sebagai beikut:
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
- ```logout(request)``` digunakan untuk meng-logout user.
- ```response = HttpResponseRedirect(reverse('main:login'))``` digunakan untuk membuat response.
- ```response.delete_cookie('last_login')``` digunakan untuk menghapus cookie ```last_login``` saat pengguna logout.

Sebagai langkah terakhir, saya membuka berkas ```main.html``` dan menambahkan potongan kode ```<h5>Sesi terakhir login: {{ last_login }}</h5>``` untuk menampilkan cookie ```last_login``` pada halaman utama.

### Tugas 5
#### 5.1 Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin
##### Kustomisasi halaman login
Untuk menambahkan kustomisasi halaman login, saya menambahkan kode sebagai berikut pada block content:
```
<style>
button {
    background-color: #04AA6D;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    width: 100%;
}
  
button:hover {
    opacity: 0.8;
}
  
.cancelbtn {
    width: auto;
    padding: 10px 18px;
    background-color: #f44336;
}
  
.imgcontainer {
    text-align: center;
    margin: 24px 0 12px 0;
}
  
.img.avatar {
    width: 40%;
    border-radius: 50%;
}
  
.container {
    padding: 16px;
}
  
span.psw {
    float: right;
    padding-top: 16px;
}
  
/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
    span.psw {
       display: block;
       float: none;
    }
    .cancelbtn {
       width: 100%;
    }
}
</style>
```

##### Kustomisasi halaman register
Untuk menambah kustomisasi halaman register, saya menambahkan kode sebagai berikut pada block content:
```
<style>
  
    button {
        background-color: #04AA6D;
        color: white;
        padding: 14px 20px;
        margin: 8px 0;
        border: none;
        cursor: pointer;
        width: 100%;
    }
      
    button:hover {
        opacity: 0.8;
    }
      
    .cancelbtn {
        width: auto;
        padding: 10px 18px;
        background-color: #f44336;
    }
      
    .imgcontainer {
        text-align: center;
        margin: 24px 0 12px 0;
    }
      
    .img.avatar {
        width: 40%;
        border-radius: 50%;
    }
      
    .container {
        padding: 16px;
    }
      
    span.psw {
        float: right;
        padding-top: 16px;
    }
      
    /* Change styles for span and cancel button on extra small screens */
    @media screen and (max-width: 300px) {
        span.psw {
           display: block;
           float: none;
        }
        .cancelbtn {
           width: 100%;
        }
    }
    </style>
```

##### Kustomisasi halaman utama
Untuk menambah kustomisasi halaman utama, saya menambahkan kode sebagai berikut pada block content:
```
    <style>
    .center-element {
        text-align: center;
    }

    h1 {
        font-size: calc(1.375rem + 1.5vw);
        color:white;
    }

    h6 {
        font-size: 1rem;
        color: white;
    }
    
    p {
        font-size: 13px;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 1rem;
    }
    
    table, th, td {
        border: 1px solid var(--bs-border-color);
        text-align: center;
    }

    th, td {
        padding: 0.5rem; 
    }

    button {
        border-radius: 15px;
        border: none;
        padding: 5px 10px;
        cursor: pointer;
    }

    body {
        font: 20px Montserrat, sans-serif;
        line-height: 1.8;
        color: #f5f6f7;
    }

    .margin {
        margin-bottom: 45px;
        margin-left: 45px;
        margin-right: 45px;
    }

    .bg-1 { 
        background-color: #1abc9c; /* Green */
        color: #ffffff;
    }

    .bg-2 { 
        background-color: #474e5d; /* Dark Blue */
        color: #ffffff;
    }

    .bg-3 { 
        background-color: #ffffff; /* White */
        color: #555555;
    }

    .bg-4 { 
        background-color: #2f2f2f; /* Black Gray */
        color: #fff;
    }

    .container-fluid {
        padding-top: 70px;
        padding-bottom: 70px;
    }

    .navbar {
        padding-top: 15px;
        padding-bottom: 15px;
        border: 0;
        border-radius: 0;
        margin-bottom: 0;
        font-size: 12px;
        letter-spacing: 5px;
    }
    
    .navbar-nav  li a:hover {
        color: #1abc9c !important;
        font-size: small;
    }
    </style>

    <nav class="navbar navbar-default">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">{{ name }}</a>
          </div>
            <div class="nav navbar-nav navbar-right">
                <a href="{% url 'main:logout' %}">
                    <button class="btn btn-outline-success" type="button">Logout</button>
                </a>
            </div>
        </div>
    </nav>

    <body>
        <div class="container-fluid bg-1 text-center">
            <h1>Librory</h1>
            <p>Unveiling the World's Tales at Your Fingertips</p>
        </div>

        <div class="container-fluid bg-2 text-center">
            <h4 class="margin">What Is Librory</h4>
            <p class="margin">Introducing Librory, your gateway to a world of books. Explore our vast collection, check the availability of each title, and stay informed about the number of copies in circulation. With real-time information at your fingertips, you'll have all you need to embark on your reading journey. Discover, enjoy, and immerse yourself in the magic of literature through our app.</p>
        </div>

        <div class="container-fluid bg-3 text-center">    
            <h3 class="margin">Find Your Favorite Book</h3><br>
            <div class="center-element">
                <div class="row">
                    {% for item in items %}
                    <div class="col-xs-12 col-sm-6 col-md-4">
                        <div class="card mx-auto p-3" style="width: 18rem;">
                            <div class="card-body">
                                <h4 class="card-title">{{ item.name }}</h4>
                                <p class="card-text">{{ item.category }}</p>
                                <p class="card-text">Amount: {{ item.amount }}</p>
                                <p class="card-text">Rented: {{ item.rented }}</p>
                                <p class="card-text">{{ item.description }}</p>
                                <a href="{% url 'main:edit_item' item.pk %}" class="btn btn-primary">Edit</a>
                                <a href="{% url 'main:delete_item' item.pk %}" class="btn btn-primary">Delete</a>
                            </div>
                        </div>
                    </div>
                    {% endfor %}
                </div>

                <p></p>
                <a href="{% url 'main:create_item' %}">
                    <button class="btn btn-outline-success" type="button">Add Item</button>
                </a>
            </div>
        </div>

        <footer class="container-fluid bg-4 text-center">
            <p>Last login: {{ last_login }}</p> 
        </footer>

    </body>
```

#### 5.2 Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card
Untuk menggunakan Card, saya menambahkan kdoe sebagai berikut:
```
<div class="container-fluid bg-3 text-center">    
    <h3 class="margin">Find Your Favorite Book</h3><br>
    <div class="center-element">
        <div class="row">
            {% for item in items %}
            <div class="col-xs-12 col-sm-6 col-md-4">
                <div class="card mx-auto p-3" style="width: 18rem;">
                    <div class="card-body">
                        <h4 class="card-title">{{ item.name }}</h4>
                        <p class="card-text">{{ item.category }}</p>
                        <p class="card-text">Amount: {{ item.amount }}</p>
                        <p class="card-text">Rented: {{ item.rented }}</p>
                        <p class="card-text">{{ item.description }}</p>
                        <a href="{% url 'main:edit_item' item.pk %}" class="btn btn-primary">Edit</a>
                        <a href="{% url 'main:delete_item' item.pk %}" class="btn btn-primary">Delete</a>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>

        <p></p>
        <a href="{% url 'main:create_item' %}">
            <button class="btn btn-outline-success" type="button">Add Item</button>
        </a>
    </div>
</div>
```
### Tugas 6
#### 6.2 Mengubah kode _cards_ data item agar dapat mendukung AJAX GET
Untuk mengubah kode _cards_ data item agar dapat mendukung AJAX GET, saya menambahkan potongan kode sebagai berikut di berkas ```main.html``` pada berkas ```templates``` pada direktori ```main```:
```
async function getItems() {
    return fetch("{% url 'main:get_item_json' %}").then((res) => res.json())
}

async function refreshItems() {
    let cardHtml = ''
    document.getElementById("item_card").innerHTML = cardHtml
    const items = await getItems();

    items.forEach((item) => {
        cardHtml += `
        <div class="card-item">
            <div class="card mx-auto p-3" style="width: 18rem;">
                <div class="card-body">
                    <h4 class="card-title">${item.fields.name}</h4>
                    <p class="card-text">${item.fields.category}</p>
                    <p class="card-text">Amount</p>
                    <p class="card-text">
                        <div class="btn-container">
                            <button class="btn decrement-btn" onclick="decrementAmount(${item.pk})">-</button>
                            <span id="amount-${item.pk}">${item.fields.amount}</span>
                            <button class="btn increment-btn" onclick="incrementAmount(${item.pk})">+</button>
                        </div>
                    </p>
                    <p class="card-text">Rented</p>
                    <p class="card-text">
                        <div class="btn-container">
                            <button class="btn decrement-btn" onclick="decrementRented(${item.pk})">-</button>
                            <span id="rented-${item.pk}">${item.fields.rented}</span>
                            <button class="btn increment-btn" onclick="incrementRented(${item.pk})">+</button>
                        </div>
                    </p>
                    <p class="card-text">${item.fields.description}</p>
                    <a style="justify-content: baseline;" href='edit-item/${item.pk}' class="btn btn-outline-warning" onclick="editItem(${item.pk})">Edit</a>
                    <button style="justify-content: baseline;" class="btn btn-outline-danger" onclick="deleteItem(${item.pk})">Delete</button>
                </div>
            </div>
        </div>
        `;
    });

    document.getElementById("item_card").innerHTML = `<div class="card-container">${cardHtml}</div>`;
}
```
#### 6.3 Membuat sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item
Untuk menambahkan sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item, saya menambahkan kode sebagai berikut di berkas ```main.html``` pada folder ```templates``` pada direktori ```main```:
```
<div class="text-center mt-3">
    <button type="button" class="btn btn-light" data-bs-toggle="modal" data-bs-target="#addItemModal">Add Book</button>
</div>
```
#### 6.4 Membuat fungsi _view_ baru untuk menambahkan item baru ke dalam basis data
Untuk membuat fungsi _view_ baru untuk menambahkan item baru ke dalam basis data saya menambahkan kode sebagai berikut di berkas ```views.py``` pada direktor ```main```:
```
@csrf_exempt
def create_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        rented = request.POST.get("rented")
        category = request.POST.get("category")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, rented=rented, category=category, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```
#### 6.5 Membuat path ```/create-ajax/``` yang mengarah ke fungsi _view_ yang sudah dibuat di poin 6.4
Untuk membuat path ```/create-ajax/``` yang mengarah ke fungsi ```create_ajax``` pada poin 6.4, saya menambahkan kode sebagai berikut di berkas ```urls.py``` pada direktori ```main```:
```
from main.views import get_item_json, create_ajax
urlpatterns = [
    ...
    path('create-ajax/', create_ajax, name='create_ajax'),
]
```
#### 6.6 Menghubungkan form yang telah dibuat di dalam modal ke path ```/create-ajax/```
Untuk menghubungkan form yang telah dibuat di dalam modal ke path ```/create_ajax/```, saya menambahkan kode sebagai berikut di berkas ```main.html``` pada folder ```templates``` pada direktori ```main```:
```
function addItem() {
    fetch("{% url 'main:create_ajax' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(refreshItems)

    document.getElementById("form").reset()
    return false
}
```
#### 6.7 Melakukan perintah collectstatic
Saya menjelaskan perintah ```python manage.py collectstatic``` pada command prompt.

## 2. Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan kaitan antara urls.py, views.py, models.py, dan berkas HTML

 ```
 ----- (request) -----> URLconf 
 ↑                         |
 |                         | (pilih view)
 |                         ↓
User                     Views <--- (query, respon data) ---> Model <--- (transaksi data) ---> Database
 ↑                         |
 |                         | (pilih template HTML)
 |     (tampilan           ↓ 
 ------ halaman ------ Template
          web)
```

Berkas ```urls.py``` pada proyek ```librory``` ditujukan untuk mengatur rute URL dan menghubungkan URL ```main/``` ke rute yang didefinisikan dalam berkas ```urls.py``` pada aplikasi ```main```. Rute ini kemudian akan menghubungkan url dengan fungsi ```view``` yang sesuai pada berkas ```views.py```.

Berkas ```views.py``` ditujukan untuk menangani permintaan HTTP dari client melalui interaksi dengan berkas ```models.py``` dan merender berkas ```main.html```.

Berkas ```models.py``` ditujukan sebagai defisinisi model basis data yang digunakan oleh aplikasi. Berkas ```views.py``` akan berinteraksi dengan berkas ```models.py``` untuk mengambil atau menyimpan data ke dalam database.

Berkas ```HTML``` ditujukan sebagai template yang digunakan untuk me-render halaman web. Berkas ```views.py``` akan merender berkas HTML dengan mengisi data yang telah dimasukkan pada dictionary ```context```. Hasil dari proses render tersebut kemudian dikirimkan sebagai respons ke client untuk dirender di browser. 

## 3. Alasan penggunaan virtual environment dan kemampuan membuat aplikasi web berbasis Django tanpa menggunakan virtual environment
Saya menggunakan virtual environment agar package dan dependencies dari aplikasi tidak bertabrakan dengan versi lain yang ada di komputer saya. Virtual environment berguna untuk mengisolasi setiap proyek sehingga setiap proyek dapat memiliki versi berbeda dari paket-paket Python, Django, dan dependenciesnya. 

Akan tetapi, aplikasi web berbasis Django tetap dapat dibuat tanpa menggunakan virtual environment. Meskipun dapat dilakukan, hal ini tetap tidak dianjurkan karena apabila pengembangan diakukan pada beberapa proyek dalam waktu bersamaan maka proyek tidak terisolasi dan masalah-masalah akan sulit terdeteksi.

## 4. Penjelasan mengenai MVC, MVT, MVVM dan perbedaan dari ketiganya.
#### MVC
MVC atau Model View Controller adalah pola arsitektur dalam membuat dan membangun aplikasi web yang terdiri dari tiga bagian, yaitu ```Model```, ```View```, dan ```Controller```. ```Model``` adalah bagian yang ditujukan untuk mengelola basis data. Sedangkan ```View``` adalah bagian yang ditujukan untuk menampilkan data dari ```Model``` dan menanggapi input dari pengguna. ```Controller``` adalah bagian yang ditujukan untuk menghubungkan serta mengatur ```Model``` dan ```View``` agar dapat saling terhubung.

#### MVT
MVT atau Model View Template adalah pola arsitektur dalam membuat dan membangun aplikasi web yang terdiri dari tiga bagian, yaitu ```Model```, ```View```, dan ```Template```. ```Model``` adalah bagian yang ditujukan untuk mengelola basis data. Sedangkan ```View``` adalah bagian yang ditujukan untuk menampilkan data dari ```Model``` dan menanggapi input dari pengguna. Template adalah bagian yang ditujukan untuk mengatur tampilan ```HTML``` dan bagaimana data dari ```Model``` akan ditampilkan sesuai ```View```.

#### MVVM
MVVM atau Model View ViewModel adalah pola arsitektur dalam membuat dan membangun aplikasi web yang terdiri dari tiga bagian, yaitu ```Model```, ```View```, dan ```ViewModel```. ```Model``` adalah bagian yang ditujukan untuk mengelola basis data. Sedangkan ```View``` adalah bagian pasif yang ditujukan untuk menampilkan data dari ```Model```. ```ViewModel``` adalah bagian yang ditujukan untuk menghubungkan ```Model``` dan ```View``` serta memetakan data dari ```Model``` ke format yang ditampilkan oleh ```View```.

### Perbedaan antara ketiganya
1. MVC
    * ```Model``` dan ```View``` terpisah dan tidak berinteraksi satu sama lain
    * ```Controller``` berfungsi sebagai perantara dan kontrol alur aplikasi
2. MVT
    * ```Template``` membantu memisahkan tampilan dari logika aplikasi
3. MVVM
    * ```View``` hanya menampilkan data dan tidak mengandung logika
    * ```ViewModel``` berfungsi sebagai perantara antara Model dan View serta mengontrol logika pemetaan data

## 5. Perbedaan antara form ```POST``` dan form ```GET``` dalam Django
#### POST
- Data yang dikirim dari form akan dikirim sebagai ```request body``` dalam request HTTP sehingga tidak terlihat dalam URL
- Biasanya digunakan untuk mengirim form untuk membuat, mengubah, atau menghapus data dalam database

#### GET
- Data yang dikirim dari form akan ditambahkan ke URL sebagai query string
- Biasanya digunakan untuk mengambil data dari server tanpa mempengaruhi data yang sudah ada

## 6. Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data
#### XML
- Berisi informasi yang dibungkus di dalam tag. Programmer perlu menulis program untuk mengirim, menerima, menyimpan, atau menampilkan informasi tersebut
#### JSON
- Berisi informasi dengan format berbentuk text. Data disimpan dalam bentuk key dan value
#### HTML
- Berbasis tag yang digunakan untuk mendefinisikan elemen-elemen pada halaman web.

## 7. Alasan mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern
JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena JSON memiliki format yang lebih ringkas dan mudah dibaca oleh manusia. Selain kemudahannya untuk dibaca, ukuran data JSON juga cenderung lebih kecil dibandingkan dengan format lain. Hal ini menjadi penting karena aplikasi web modern harus memiliki kinerja tinggi, untuk mencapai hal tersebut, pengurangan beban pada jaringan akan sangat berpengaruh pada kinerja aplikasi web. Penggunaan JSON juga memungkinkan programmer untuk menyusun data secara hierarkis saat kompleksitas data dibutuhkan. Selain kelebihan-kelebihan yang telah disebutkan sebelumnya, JSON juga merupakan format data yang dapat digunakan lintas platform dan didukung penggunaannya pada hampir semua bahasa pemrograman. Kelebihannya ini membuat JSON unggul dalam pertukaran data antara aplikasi yang berjalan di berbagai lingkungan pengembangan.

## 8. Mengakses kelima URL menggunakan Postman
### 1. path('create-item', create_item, name='create_item'): http://localhost:8000/create-item
![Screenshot 2023-09-18 002632](https://github.com/eelizabethmichelle/librory/assets/124945174/416e5ac0-7498-46cb-80bd-5de40995ee37)
### 2. path('xml/', show_xml, name='show_xml'): http://localhost:8000/xml/
![Screenshot 2023-09-18 003318](https://github.com/eelizabethmichelle/librory/assets/124945174/29b18b17-f078-478e-be16-488f0c492f6a)
![Screenshot 2023-09-18 003511](https://github.com/eelizabethmichelle/librory/assets/124945174/66f46cad-8fa5-4d78-af52-380240563ca1)
### 3. path('json/', show_json, name='show_json'): http://localhost:8000/json/
![Screenshot 2023-09-18 003402](https://github.com/eelizabethmichelle/librory/assets/124945174/f9a8f852-4a3f-4601-a4cf-d09591e1ad69)
![Screenshot 2023-09-18 003436](https://github.com/eelizabethmichelle/librory/assets/124945174/a9cf9c59-d95d-413e-a9a7-b50b750c9628)
### 4. path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'): http://localhost:8000/xml/1
![Screenshot 2023-09-18 003603](https://github.com/eelizabethmichelle/librory/assets/124945174/042f121e-42de-4085-ba21-52387611d82f)
![Screenshot 2023-09-18 003616](https://github.com/eelizabethmichelle/librory/assets/124945174/a8b1fd72-ae19-43fa-992f-3f175e99dbab)
### 5. path('json/<int:id>/', show_json_by_id, name='show_json_by_id'): http://localhost:8000/json/1
![Screenshot 2023-09-18 003636](https://github.com/eelizabethmichelle/librory/assets/124945174/d2d18d68-7eeb-4a6c-8a76-3fcb63358aa6)
![Screenshot 2023-09-18 003649](https://github.com/eelizabethmichelle/librory/assets/124945174/27fdfdc0-2951-4bd3-a391-2e62648eaf70)

## 9. Kelebihan dan kekurangan Django ```UserCreationForm```
UserCreationForm adalah impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web. Dengan formulir ini, pengguna baru dapat mendaftar dengan mudah di situs web tanpa harus menulis kode dari awal.
#### Kelebihan UserCreationForm
1. Cepat dan mudah digunakan karena tidak perlu menuliskan kode dari awal.
2. Dapat memvalidasi untuk memastikan bahwa input yang dimasukkan oleh pengguna sesuai dengan persyaratan dasar seperti panjang kata sandi yang cukup dan alamat email yang valid.
3. Terintegrasi dengan model User yang ada di Django sehingga data pengguna baru dapat dengan mudah disimpan ke dalam database.
4. Dapat disesuaikan sesuai dengan kebutuhan dengan menambahkan bidang tambahan atau mengubah pesan kesalahan yang ditampilkan kepada pengguna.
#### Kekurangan UserCreationForm
1. Memiliki tampilan bawaan yang sederhana.
2. Tidak cocok untuk kasus khusus yang kompleks.
3. Tidak mendukung fitur tambahan seperti autentikasi melalui media sosial.
4. Tergantung pada Django sehingga terdapat limitasi saat diintegrasikan dengan kerangka kerja lain.

## 10. Perbedaan antara autentikasi dan otorisasi dalam konteks Django
#### Autentikasi
Autentikasi adalah proses untuk memverifikasi identitas pengguna dengan tujuan untuk memastikan bahwa pengguna yang mengakses aplikasi adalah pengguna yang sesungguhnya. Proses ini biasa dilakukan dengan memverifikasi kredentials dan identitas entitas. Autentikasi berfokus pada pemeriksaan apakah pengguna memiliki kredensial yang benar untuk mengakses sistem.
#### Autorisasi
Autorisasi adalah proses untuk mengatur dan mengendalikan izin akses pengguna terhadap sumber daya atau aksi tertentu dalam aplikasi dengan tujuan untuk mengatur apa yang dapat dan tidak dapat diakses oleh pengguna yang telah diautentikasi. Autorisasi berfokus pada pengaturan hak akses dan aturan yang mengendalikan apa yang pengguna boleh dan tidak boleh lakukan dalam aplikasi.

## 11. Pengertian cookies dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna
Cookies adalah informasi sederhana yang dapat digunakan web untuk mengidentifikasi pengguna dalam sesi web yang disimpan di sisi klien oleh server web. 
Django menggunakan cookies untuk mengelola data sesi pengguna dan menyimpan informasi sederhana yang dapat digunakan oleh server untuk mengidentifikasi pengguna atau mengingat preferensi pengguna. 

## 12. Keamanan penggunaaan cookies secara default dalam pengembangan web dan risiko potensial yang harus diwaspadai
Penggunaan cookies secara default dalam pengembangan web memiliki beberapa implikasi keamanan yang perlu diperhatikan, yaitu:
1. Pencurian informasi pribadi
Cookies yang tidak dienkripsi dengan baik dapat menyebabkan terjadinya pelanggaran keamanan seperti pencurian nama pengguna, alamat email, atau token otentikasi.
2. CSRF (Cross-Site Request Forgery)
Cookies yang digunakan untuk autentikasi dapat menjadi sasaran serangan CSRF sehingga aksi atau perubahan yang unauthorized dapat dilakukan dengan mengatasnamakan pengguana.
3. XSS (Cross-Site Scriptiing)
Serangan ini dapat dilakukan dengan penyisipan skrip berbahaya dalam cookies sehingga ketika cookies dieksekusi oleh browser pengguna, serangan XSS dapat terjadi.
4. User tracking
Cookies sering digunakan oleh perusahaan untuk melacak aktivitas pengguna secara online sehingga hal ini dapat melanggar privasi pengguna.
5. Penggunaan cookies yang berlebihan dan tidak aman
Penggunaan cookies yang terlalu banyak dalam satu aplikasi web dapat menghambat kinerja dan menjadi target penyerangan seperti peretasan sesi atau pencurian cookies apabila cookies tidak diatur dengan benar atau memiliki atribut yang tidak aman.

## 13. Manfaat dari setiap element selector dan waktu yang tepat untuk menggunakannya
#### Type Selector
Type selector dapat memilih smeua elemen dengan tipe tertentu. Selektor ini lebih baik digunakan ketika pengubahan gaya untuk semua elemen dengan tipe yang sama harus dilakukan.
#### Class Selector
Class selector dapat memilih elemen berdasarkan kelas yang diberikan. Selector ini lebih baik digunakan ketika pengaplikasian gaya tertentu atas kelas tertentu harus dilakukan. 
#### ID Selector
ID selector dapat memilih elemen berdasarkan ID yang diberikan. Selector ini lebih baik digunakan ketika pengidentifikasian atas elemen tertentu harus dilakukan. 
#### Universal Selector
Universal selector dapat memilih semua elemen di halaman HTML. Selector ini lebih baik digunakan ketika dibutuhkan pengubahan gaya untuk semua elemen pada halaman HTML.
#### Pseudo-class Selector
Pseudo-class selector dapat memilih elemen berdasarkan keadaan atau interaksi pengguna seperti ':hover' atau ':active'. Selector ini lebih baik digunakan ketika pmberian gaya tambahan saat elemen dalam keadaan tertentu perlu dilakukan.

## 14. HTML5 Tag
- ```<html>```: elemenn root dari setiap halaman web HTML5
- ```<head```: berisi informasi tentang dokumen terkait, seperti jduul halaman, metadata, dan tautan ke file eksternal
- ```<body>```: mengandung semua konten yang akan ditampilkan
- ```<meta>```: untuk menyertakan metadata dalam halaman web, seperti karakter set yang digunakan dan deskripsi halaman
- ```<title>```: untuk menentukan judul halaman yang akan ditampilkan di tab browser
- ```<link>```: untuk menghubungkan halaman web dengan file eksternal, seperti file CSS
- ```<style>```: untuk menuliskan CSS inline yang akan ditampilkan pada halaman
- ```<script>```: untuk menyertakan script JavaScript pada halaman
- ```<header>```: untuk mengelompokkan elemen-elemen yang merupakan kepala dari halaman
- ```<footer>``` untuk mengelompokkan elemen-elemen yang merupakan informasi penutupan halaman
- ```nav```: untuk mengelompokkan tautan navigasi atau menu
- ```<main>```: untuk mengidentifikasi konten utama halaman
- ```<section>```: untuk mengelompokkan konten yang memiliki topik tetentu dalam halaman
- ```<form>```: untuk membuat formulir interaktif yang memungkinkan pengguna untuk mengirimkan data

## 15. Perbedaan antara margin dan padding
#### Margin
- Margin menandakan ruang di sekitar elemen HTML di luar batas elemen itu sendiri
- Digunakan untuk mengatur jarak antara elemen dengan elemen lain di sekitarnya atau dengan elemen lain dalam kontainer yang lebih besar
- Hanya mendefinisikan ruang antara elemen dengan elemen lainnya dan tidak memiliki warna atau latar belakang
- Dapat memiliki nilai positif maupun negatif

#### Padding
- Padding menandakan ruang di sekitar elemen HTML di dalam batas elemen itu sendiri
- Digunakan untuk mengatur jarak antara konten elemen dan batas elemennya
- Memiliki warna atau latar belakang

## 16. Perbedaan antara framework CSS Tailwind dan Bootstrap. dan waktu terbaik dalam penggunaan keduanya
#### CSS Tailwind
- Utility-first approach. Menggabungkan kelas CSS ke dalam elemen HTML
- Flexible configuration. Tailwind dapat dikonfigurasi untuk emnghasilkan elas-kelas yang sesuai dengan kebutuhan halaman
- Memiliki ukuran yang lebih kecil daripada bootstrap

#### Bootstrap
- Component-based approach. Didasarkan pada komponen-komponen siap pakai
- Consistent design. Bootstrap dapat diimplementasikan untuk menghasilkan tampilan yang konsisten di seluruh halaman
- Memiliki dokumentasi yang sangat baik

#### CSS Tailwind > Bootstrap
- Membutuhkan tingkat kustomisasi yang tinggi
- Meminimalisir penggunaan memori
- Menghindari konflik kelas CSS pada proyek yang lebih besar

#### Bootstrap > CSS Tailwind
- Membangun halaman dengan cepat tanpa banyak kustomisasi
- Membutuhkan konsistensi desain yang itnggi
- Mengutamakan dokumentasi yang kuat

## 17. Perbedaan antara asynchronous programming dengan synchronous programming
#### Asynchronous programming
- Tugas-tugas dapat dieksekusi secara paralel
- Ketika dijalankan, tugas bersifat non-blocking
- Memerlukan callback functions
- Digunakan ketika ada tugas-tugas yang memerlukan waktu lama

#### Synchronous programming
- Tugas-tugas dieksekusi secara sequential
- Ketika dijalankan, tugas bersifat blocking
- Tidak memerlukan konsep callback atau promise 
- Digunakan ketika ada tugas-tugas yang memerlukan proses berurutan

## 18. Paradigma event-driven programming dan salah satu contoh penerapannya pada tugas ini
Paradigma event-driven programming adalah pendekatan dalam pemrograman di mana program menjalankan suatu tugas dengan merespon pada peristiwa yang terjadi, seperti button clicks. 
Contoh penerapakannya pada tugas ini adalah penggunaan button "Add Book" yang apabila diclick maka modal akan dimunculkan. Contoh kode yang digunakan, yaitu ```document.getElementById("button_add").onclick = addItem```.

## 19. Penerapan asynchronous programming pada AJAX.
1. Menggunakan objek XMLHttpRequest atau Fetch API
Membuat permintaan HTTP asynchronous menggunakan objek XMLHttpRequest atau Fetch API.
2. Mengirim permintaan ke server
Mengirim permintaan HTTP dengan menggunakan metode ```open()``` untuk mengkonfigurasi permintaan dan ```send()``` untuk mengirimnya. Dalam AJAX, permintaan berupa ```GET``` dan ```POST```.
3. Menggunakan callback untuk menangani respons
Memproses data yang diterima dan melakukan tindakan yang sesuai. 
4. Mengatur asynchronous
Dalam objek XMLHttpRequest permintaan dapat diatur sebagai asynchronous dengan ```xhr.open(method, url, true)``` atau menggunakan ```fetch``` dengan menggunakan ```.then()``` dan ```.catch()``` untuk menangani callback.

## 20. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
#### Fetch API
1. Kelebihan
- API mengikuti standar ECMAScript dan menjadi bagian integral dari peramban web utama
- Fetch API mengembalikan objek Promise sehingga pengkodean asynchronous lebih mudah dibaca
- Fetch API mendukung berbagai jenis respons data, seperti JSON, XML, HTML, dll

2. Kekurangan
- Fetch API tidak didukung oleh beberapa peramban web lama. 

#### Library jQuery
1. Kelebihan
- jQuery memiliki kompatibilitas yang sangat baik dengan berbagai peramban web, termasuk peramban web lama sehingga cocok untuk proyek dengan basis pengguna yang beragam
- Sintaks mudah dipahami dan ringan sehingga cepat dipelajari oleh pengembang pemula

2. Kekurangan
- Dapat menambahkan overhead yang tidak perlu ke proyek-proyek yang sederhana atau kecil
- Penggunaan callback dapat menghasilkan callback hell