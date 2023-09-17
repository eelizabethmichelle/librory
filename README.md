###### Nama aplikasi:
# 📖 librory 📚
###### Nama: Michelle Elizabeth Amanda Hutasoit
###### Kelas: PBP C

###### Aplikasi Adaptable yang sudah di-deploy: [link](https://librory.adaptable.app)

## 1. Cara mengimplementasikan checklist:
### Tugas 2
#### a. Membuat sebuah proyek Django baru
Untuk dapat membuat sebuah proyek Django baru, dibutuhkan sebuah direktori yang telah terhubung ke suatu repositori Git. Maka dari itu, saya **membuat direktori dengan nama ```librory``` yang terhubung dengan repositori Git yang bernama ```librory```** juga. Setelah itu, saya membuat dan **mengaktifkan virtual environment** pada direktori ```librory``` agar package dan dependencies dari aplikasi tidak bertabrakan dengan versi lain yang ada di komputer saya.

Setelah berhasil melakukan set up, saya membuat berkas yang berisi dependencies yang akan saya butuhkan dalam mengembangkan aplikasi, yaitu **django, gunicorn, whinoise, psycopg2-binary, requests, dan urllib3**. Melalui berkas tersebut, saya **meng-install dependencies** yang telah dispesifikasikan dan **membuat proyek Django dengan nama ```librory```**. Proses tersebut saya lakukan dengan menjalankan perintah **```django-admin startproject librory .```**, perintah tersebut akan membuat proyek Django baru dengan nama ```librory```. Titik yang dituliskan pada akhir perintah dimaksudkan agar proyek dibuat tepat di direktori di mana saya sedang bekerja tanpa membuat sebuah folder untuk proyek tersebut.

#### b. Membuat aplikasi dengan nama main pada proyek tersebut
Sama seperti yang sebelumnya dilakukan saat membuat sebuah proyek Django baru, virtual environment pada direktori terkait, dalam hal ini direktori ```librory```, harus diaktifkan terlebih dahulu. Setelah itu, saya **membuat aplikasi dengan nama ```main```** dengan menjalankan perintah **```python manage.py startapp main```**. Perintah tersebut akan membuat aplikasi baru bernama ```main``` di dalam proyek Django terkait dan aplikasi akan berada dalam konteks dan pengaturan yang sama dengan proyek. Akan tetapi, meskipun aplikasi ```main``` telah berhasil dibuat, aplikasi belum terdaftar ke dalam proyek, maka dari itu saya **menambahkan aplikasi ```main``` ke dalam list ```INSTALLED_APPS``` yang berada di berkas ```settings.py```**.

#### c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main
Untuk melakukan routing, saya **membuat berkas ```urls.py``` di dalam direktori ```main```** dan **mengimport ```path``` dari ```django.urls```** untuk mendefinisikan pola URL. Berkas ```urls.py``` yang dibuat di dalam direktori ```main``` ditujukan untuk mengatur rute URL pada aplikasi ```main```. Sebelumnya, pada berkas ```views.py```, saya telah menambahkan fungsi ```show_main``` sebagai tampilan, maka dari itu saya **meng-import fungsi ```show_main```** untuk kemudian ditampilkan ketika URL terkait diakses. Saya juga **menambahkan variabel bernama ```app_name```** yang kemudian digunakan untuk memberikan nama unik pada pola URL dalam aplikasi. 

#### d. Membuat model pada aplikasi main dengan nama Item dan memiliki atribut:
1. ```name``` dengan tipe CharField: judul buku
2. ```amount``` dengan tipe IntegerField: jumlah buku
3. ```rented``` dengan tipe IntegerField: jumlah buku yang disewa
4. ```category``` dengan tipe CharField: kategori buku
5. ```description``` dengan tipe TextField: deskripsi/sinopsis buku

Untuk membuat model pada aplikasi ```main``` sesuai dengan class dan atribut yang saya inginkan, saya terlebih dahulu **meng-import modul ```models``` dari modul ```django.db```**. Setelah itu, saya **membuat class dengan nama ```Item``` yang menerima parameter ```models.Model```**, parameter tersebut merupakan kelas dasar yang akan digunakan untuk mendefinisikan model dalam Django. Di dalam class ```Item```, saya **menambahkan atribut ```name``` dengan tipe CharField** yang hanya menerika karakter dengan panjang maksimal 255 karakter, **atribut ```amount``` dengan tipe IntegerField**, **atribut ```rented``` dengan tipe IntegerField**, **atribut ```category``` dengan tipe CharField** yang hanya menerika karakter dengan panjang maksimal 255 karakter, dan **atribut ```description``` dengan tipe TextField**.

#### e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi, nama, dan kelas
Sebelum saya membuat fungsi pada berkas ```views.py```, saya terlebih dahulu **meng-import ```render``` dari modul ```django.shortcuts```** untuk me-render tampilan HTML dengan data yang akan diintegrasikan melalui fungsi. Setelah itu, saya **membuat fungsi dengan nama ```show_main``` pada berkas ```views.py```** sebagai data acuan yang kemudian akan ditampilkan pada tampilan ```HTML```. 

Saya **membuat sebuah dictionary dengan nama ```context```** yang berisi **key ```app_name``` dengan value ```librory```**, **key ```name``` dengan value ```Michelle Elizabeth Amanda Hutasoit```**, dan **key ```class``` dengan value ```PBP C```**. **Fungsi ```show_main``` akan me-return ```render(request, "main.html", context)```** di mana fungsi ```render``` akan me-render tampilan berdasarkan request/objek HTTP yang dikirim oleh pengguna pada berkas template ```main.html```, dengan dictionary ```context``` yang berisi data yang akan digunakan dan ditampilkan dalam tampilan dinamis.

Setelah selesai melakukan set up pada berkas ```views.py```, saya kemudian memodifikasi template pada berkas ```main.html``` agar data pada dictionary ```context``` dapat digunakan. Saya **menambahkan ```{{ app_name }}```, ```{{ name }}```, dan ```{{ class }}```** pada template sesuai dengan posisi yang diinginkan untuk menampilkan value dari variabel yang telah didefinisikan dalam dictionary ```context```.

#### f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
Setelah berhasil melakukan set up pada aplikasi ```main```, saya mengonfigurasi routing URL pada proyek ```librory```. Jika berkas ```urls.py``` pada aplikasi ```main``` ditujukan untuk mengatur rute URL pada aplikasi ```main```, maka berkas ```urls.py``` pada proyek ```librory``` ditujukan untuk mengatur rute URL pada tingkat proyek. Pada direktori ```librory```, telah terdapat berkas ```urls.py``` sehingga saya tidak perlu membuat berkas tersebut kembali. Pada berkas tersebut, saya **meng-import fungsi ```include```** untuk mengimpor rute URL dari aplikasi ```main``` **ke dalam berkas ```urls.py``` proyek ```librory```**. Saya juga **menambahkan ```path('main/', include('main.urls'))```** pada list urlpatterns agar path url ```main/``` akan diarahkan ke rute yang didefinisikan dalam berkas ```urls.py``` pada aplikasi ```main```.

#### g. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat
Untuk melakukan deployment ke Adaptable, saya terlebih dahulu **melakukan add, push, dan commit perubahan pada direktori kepada repositori**. Hal ini dilakukan karena deployment akan dihubungkan dengan akun GitHub serta repositori yang berkaitan. Setelah selesai menambahkan perubahan pada repositori, saya **membuat akun Adaptable.io** menggunakan akun GitHub dan **menekan tombol ```New App```**. Saya **memilih opsi ```Connect an Existing Repository```** dan **memilih repositori ```librory```** karena saya ingin men-deploy aplikasi tersebut. Saya **memilih branch ```main```** sebagai deployment branch, kemudian saya **memilih ```Python App Template```** sebagai template deployment, serta **```PostgreSQL```** sebagai tipe basis data yang akan digunakan. Setelah itu, saya **memilih versi ```Python 3.10```** sesuai versi Python yang saya install dan **memasukkan perintah ```python manage.py migrate && gunicorn librory.wsgi```** pada bagian Start Command. Setelah itu, saya **memasukkan ```librory``` sebagai nama aplikasi**, **mencentang bagian ```HTTP Listener on PORT```**, dan men-deploy aplikasi dengan **menekan tombol ```Deploy App```**. Apabila terdapat perubahan/pembaruan pada repositori, saya akan menekan tombol dengan tiga titik dan me-redeploy aplikasi.

### Tugas 3
#### h. Membuat input form untuk menambahkan objek model pada app sebelumnya.
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


#### i. Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID
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

#### j. Membuat routing URL untuk masing-masing views yang telah ditambahkan
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
