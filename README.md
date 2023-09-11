###### Nama aplikasi:
# 📖 librory 📚
###### Nama: Michelle Elizabeth Amanda Hutasoit
###### Kelas: PBP C

###### Aplikasi Adaptable yang sudah di-deploy: [link](https://librory.adaptable.app)

## 1. Cara mengimplementasikan checklist:
#### a. Membuat sebuah proyek Django baru
Untuk dapat membuat sebuah proyek Django baru, dibutuhkan sebuah direktori yang telah terhubung ke suatu repositori Git. Maka dari itu, saya **membuat direktori dengan nama ```librory``` yang terhubung dengan repositori Git yang bernama ```librory```** juga. Setelah itu, saya membuat dan **mengaktifkan virtual environment** pada direktori ```librory``` agar package dan dependencies dari aplikasi tidak bertabrakan dengan versi lain yang ada di komputer saya.

Setelah berhasil melakukan set up, saya membuat berkas yang berisi dependencies yang akan saya butuhkan dalam mengembangkan aplikasi, yaitu **django, gunicorn, whinoise, psycopg2-binary, requests, dan urllib3**. Melalui berkas tersebut, saya **meng-install dependencies** yang telah dispesifikasikan dan **membuat proyek Django dengan nama ```librory```**. Proses tersebut saya lakukan dengan menjalankan perintah **```django-admin startproject librory .```**, perintah tersebut akan membuat proyek Django baru dengan nama ```librory```. Titik yang dituliskan pada akhir perintah dimaksudkan agar proyek dibuat tepat di direktori di mana saya sedang bekerja tanpa membuat sebuah folder untuk proyek tersebut.

#### b. Membuat aplikasi dengan nama main pada proyek tersebut
Sama seperti yang sebelumnya dilakukan saat membuat sebuah proyek Django baru, virtual environment pada direktori terkait, dalam hal ini direktori ```librory```, harus diaktifkan terlebih dahulu. Setelah itu, saya **membuat aplikasi dengan nama ```main```** dengan menjalankan perintah **```python manage.py startapp main```**. Perintah tersebut akan membuat aplikasi baru bernama ```main``` di dalam proyek Django terkait dan aplikasi akan berada dalam konteks dan pengaturan yang sama dengan proyek. Akan tetapi, meskipun aplikasi ```main``` telah berhasil dibuat, aplikasi belum terdaftar ke dalam proyek, maka dari itu saya **menambahkan aplikasi ```main``` ke dalam list ```INSTALLED_APPS``` yang berada di berkas ```settings.py```**.

#### c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main
Untuk melakukan routing, saya **membuat berkas ```urls.py``` di dalam direktori ```main```** dan **mengimport ```path``` dari ```django.urls```** untuk mendefinisikan pola URL. Berkas ```urls.py``` yang dibuat di dalam direktori ```main``` ditujukan untuk mengatur rute URL pada aplikasi ```main```. Sebelumnya, pada berkas ```views.py```, saya telah menambahkan fungsi ```show_main``` sebagai tampilan, maka dari itu saya **meng-import fungsi ```show_main```** untuk kemudian ditampilkan ketika URL terkait diakses. Saya juga **menambahkan variabel bernama ```app_name```** yang kemudian digunakan untuk memberikan nama unik pada pola URL dalam aplikasi. 

#### d. Membuat model pada aplikasi main dengan nama Item dan memiliki atribut:
1. name dengan tipe CharField
2. amount dengan tipe IntegerField
3. type dengan tipe TextField 
4. description dengan tipe TextField

Untuk membuat model pada aplikasi ```main``` sesuai dengan class dan atribut yang saya inginkan, saya terlebih dahulu **meng-import modul ```models``` dari modul ```django.db```**. Setelah itu, saya **membuat class dengan nama ```Item``` yang menerima parameter ```models.Model```**, parameter tersebut merupakan kelas dasar yang akan digunakan untuk mendefinisikan model dalam Django. Di dalam class ```Item```, saya **menambahkan atribut ```name``` dengan tipe CharField** yang hanya menerika karakter dengan panjang maksimal 255 karakter, **atribut ```amount``` dengan tipe IntegerField**, **atribut ```type``` dengan tipe TextField**, dan **atribut ```description``` dengan tipe TextField**.

#### e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi, nama, dan kelas
Sebelum saya membuat fungsi pada berkas ```views.py```, saya terlebih dahulu **meng-import ```render``` dari modul ```django.shortcuts```** untuk me-render tampilan HTML dengan data yang akan diintegrasikan melalui fungsi. Setelah itu, saya **membuat fungsi dengan nama ```show_main``` pada berkas ```views.py```** sebagai data acuan yang kemudian akan ditampilkan pada tampilan ```HTML```. 

Saya **membuat sebuah dictionary dengan nama ```context```** yang berisi **key ```app_name``` dengan value ```librory```**, **key ```name``` dengan value ```Michelle Elizabeth Amanda Hutasoit```**, dan **key ```class``` dengan value ```PBP C```**. **Fungsi ```show_main``` akan me-return ```render(request, "main.html", context)```** di mana fungsi ```render``` akan me-render tampilan berdasarkan request/objek HTTP yang dikirim oleh pengguna pada berkas template ```main.html```, dengan dictionary ```context``` yang berisi data yang akan digunakan dan ditampilkan dalam tampilan dinamis.

Setelah selesai melakukan set up pada berkas ```views.py```, saya kemudian memodifikasi template pada berkas ```main.html``` agar data pada dictionary ```context``` dapat digunakan. Saya **menambahkan ```{{ app_name }}```, ```{{ name }}```, dan ```{{ class }}```** pada template sesuai dengan posisi yang diinginkan untuk menampilkan value dari variabel yang telah didefinisikan dalam dictionary ```context```.

#### f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
Setelah berhasil melakukan set up pada aplikasi ```main```, saya mengonfigurasi routing URL pada proyek ```librory```. Jika berkas ```urls.py``` pada aplikasi ```main``` ditujukan untuk mengatur rute URL pada aplikasi ```main```, maka berkas ```urls.py``` pada proyek ```librory``` ditujukan untuk mengatur rute URL pada tingkat proyek. Pada direktori ```librory```, telah terdapat berkas ```urls.py``` sehingga saya tidak perlu membuat berkas tersebut kembali. Pada berkas tersebut, saya **meng-import fungsi ```include```** untuk mengimpor rute URL dari aplikasi ```main``` **ke dalam berkas ```urls.py``` proyek ```librory```**. Saya juga **menambahkan ```path('main/', include('main.urls'))```** pada list urlpatterns agar path url ```main/``` akan diarahkan ke rute yang didefinisikan dalam berkas ```urls.py``` pada aplikasi ```main```.

#### g. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat
Untuk melakukan deployment ke Adaptable, saya terlebih dahulu **melakukan add, push, dan commit perubahan pada direktori kepada repositori**. Hal ini dilakukan karena deployment akan dihubungkan dengan akun GitHub serta repositori yang berkaitan. Setelah selesai menambahkan perubahan pada repositori, saya **membuat akun Adaptable.io** menggunakan akun GitHub dan **menekan tombol ```New App```**. Saya **memilih opsi ```Connect an Existing Repository```** dan **memilih repositori ```librory```** karena saya ingin men-deploy aplikasi tersebut. Saya **memilih branch ```main```** sebagai deployment branch, kemudian saya **memilih ```Python App Template```** sebagai template deployment, serta **```PostgreSQL```** sebagai tipe basis data yang akan digunakan. Setelah itu, saya **memilih versi ```Python 3.10```** sesuai versi Python yang saya install dan **memasukkan perintah ```python manage.py migrate && gunicorn librory.wsgi```** pada bagian Start Command. Setelah itu, saya **memasukkan ```librory``` sebagai nama aplikasi**, **mencentang bagian ```HTTP Listener on PORT```**, dan men-deploy aplikasi dengan **menekan tombol ```Deploy App```**. Apabila terdapat perubahan/pembaruan pada repositori, saya akan menekan tombol dengan tiga titik dan me-redeploy aplikasi.

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
