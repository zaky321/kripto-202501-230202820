# Laporan Praktikum Kriptografi
Minggu ke-: 14  
Topik: [Analisis Serangan Kriptografi]  
Nama: [Sofyan Muzaki]  
NIM: [230202820]  
Kelas: [5IKRA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Mengidentifikasi jenis serangan pada sistem informasi nyata.  
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.  
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.  

---

## 2. Dasar Teori
Serangan kriptografi merupakan upaya mengeksploitasi kelemahan pada algoritma, implementasi, atau manajemen kunci dalam sistem informasi untuk memperoleh data rahasia secara tidak sah. Dalam sistem nyata, serangan ini tidak selalu menargetkan algoritma matematisnya secara langsung, melainkan sering memanfaatkan kesalahan konfigurasi, penggunaan protokol usang, atau pengelolaan kunci yang buruk. Contohnya adalah penggunaan algoritma enkripsi lemah, kunci pendek, atau komunikasi tanpa perlindungan transport layer yang memadai, sehingga data dapat disadap atau dimodifikasi.

Jenis serangan kriptografi yang umum meliputi brute force attack, man-in-the-middle, replay attack, dan cryptographic downgrade attack. Pada brute force, penyerang mencoba semua kemungkinan kunci hingga menemukan yang benar, yang biasanya berhasil jika panjang kunci tidak cukup kuat. Man-in-the-middle terjadi ketika penyerang menyisipkan diri di antara dua pihak yang berkomunikasi, sehingga dapat membaca atau mengubah pesan yang dienkripsi jika mekanisme autentikasi tidak kuat. Sementara itu, replay attack memanfaatkan pengiriman ulang pesan terenkripsi yang valid untuk menipu sistem.

Analisis serangan kriptografi pada sistem informasi nyata menuntut evaluasi menyeluruh, tidak hanya pada algoritma yang digunakan tetapi juga pada implementasinya. Sistem yang secara teori aman tetap dapat ditembus jika pengembang mengabaikan praktik keamanan seperti rotasi kunci, validasi sertifikat, atau penggunaan secure random generator. Oleh karena itu, keamanan kriptografi harus dipandang sebagai kombinasi antara kekuatan algoritma, ketepatan implementasi, dan disiplin operasional dalam pengelolaan sistem.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## Panduan Langkah demi Langkah

### Langkah 1 — Identifikasi Serangan
Kasus serangan kriptografi: Serangan brute force dan dictionary attack pada hash MD5 yang digunakan untuk penyimpanan password.

Vektor serangan: Penyerang memperoleh database yang berisi hash MD5 (misalnya melalui kebocoran data atau SQL Injection), lalu melakukan serangan offline menggunakan brute force, dictionary attack, atau rainbow table untuk menebak password asli. Serangan ini efektif karena MD5 dapat dihitung sangat cepat sehingga memungkinkan percobaan dalam jumlah besar dalam waktu singkat.

Penyebab kelemahan: MD5 merupakan algoritma hash yang sudah usang dan tidak dirancang untuk pengamanan password. Kelemahannya diperparah oleh tidak digunakannya salt dan mekanisme key stretching, sehingga hash yang sama dapat dengan mudah dicocokkan dengan tabel hash yang telah tersedia. Akibatnya, sistem autentikasi menjadi rentan meskipun password disimpan dalam bentuk hash.

---

### Langkah 2 — Evaluasi Kelemahan
Kelemahan utama terdapat pada algoritma kriptografi MD5 itu sendiri. MD5 tidak lagi aman karena tidak tahan terhadap collision dan memiliki proses hashing yang sangat cepat, sehingga memudahkan serangan brute force dan dictionary attack. Algoritma ini memang tidak dirancang untuk pengamanan password, melainkan untuk verifikasi integritas data.

Namun, kerentanan menjadi jauh lebih parah akibat kesalahan implementasi dan konfigurasi sistem. Banyak sistem menggunakan MD5 tanpa salt dan tanpa key stretching, sehingga hash password yang sama dapat dengan mudah dicocokkan menggunakan rainbow table. Selain itu, penyimpanan hash secara statis tanpa mekanisme pengamanan tambahan memperbesar risiko ketika terjadi kebocoran database.

---

### Langkah 3 — Rekomendasi Solusi
Usulan algoritma/mekanisme yang lebih aman:
Untuk penyimpanan password, algoritma MD5 sebaiknya diganti dengan bcrypt, scrypt, atau Argon2. Untuk fungsi hash umum, MD5 dapat digantikan oleh SHA-256, sedangkan pada sistem kriptografi kunci publik, RSA lama dapat diganti dengan Elliptic Curve Cryptography (ECC).

Alasan pemilihan algoritma:
bcrypt, scrypt, dan Argon2 dirancang khusus untuk pengamanan password karena bersifat slow hashing dan mendukung salt serta key stretching, sehingga serangan brute force dan dictionary attack menjadi sangat mahal secara komputasi. SHA-256 lebih aman dibanding MD5 karena memiliki panjang hash lebih besar dan tahan terhadap collision yang dikenal. ECC dipilih karena menawarkan tingkat keamanan setara RSA dengan ukuran kunci yang lebih kecil dan efisiensi yang lebih tinggi.

Dampak terhadap keamanan sistem:
Penggunaan algoritma yang lebih kuat secara signifikan meningkatkan ketahanan sistem terhadap kebocoran data, serangan offline, dan pemalsuan kunci. Walaupun berdampak pada peningkatan beban komputasi, trade-off ini sebanding karena sistem menjadi lebih sulit ditembus dan lebih selaras dengan standar keamanan modern.


---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan

- Pertanyaan 1:Karena banyak sistem lama dibangun dengan asumsi ancaman yang sudah usang. Dahulu, keterbatasan komputasi membuat hash cepat seperti MD5 atau SHA-1 dianggap “cukup aman”. Saat ini, GPU dan cloud                            memungkinkan percobaan miliaran hash per detik, sehingga password dari ruang kemungkinan kecil dapat ditebak dengan sangat cepat. Selain itu, sistem lama sering menyimpan hash tanpa salt, tanpa key                         stretching, dan jarang diperbarui karena alasan kompatibilitas, biaya migrasi, atau risiko downtime. Akibatnya, ketika database bocor, serangan offline menjadi sangat efektif.
- Pertanyaan 2:Kelemahan algoritma adalah masalah intrinsik pada desain kriptografinya. Contohnya, MD5 tidak tahan collision dan terlalu cepat untuk pengamanan password. Bahkan jika diimplementasikan “benar”, algoritma                    ini tetap tidak memenuhi standar keamanan modern.
                Kelemahan implementasi muncul ketika algoritma yang sebenarnya kuat digunakan secara keliru atau tidak lengkap. Misalnya, menggunakan SHA-256 untuk password tetapi tanpa salt, tanpa iterasi, atau menyimpan                 kunci secara hard-coded. Dalam praktik, sistem sering gagal bukan karena algoritmanya salah, melainkan karena cara penerapannya yang mengabaikan threat model nyata.
- Pertanyaan 3: Organisasi harus memperlakukan kriptografi sebagai proses berkelanjutan, bukan keputusan sekali pakai. Ini mencakup penggunaan algoritma modern yang tepat guna (misalnya password hashing khusus),                           penerapan best practices (salt, key stretching, rotasi kunci), serta audit dan pembaruan berkala mengikuti standar terbaru. Selain itu, penting membangun crypto agility—kemampuan sistem untuk mengganti                     algoritma tanpa merombak total aplikasi—agar tetap adaptif terhadap perkembangan serangan dan kemajuan komputasi.

---

## 8. Kesimpulan
Berdasarkan percobaan brute force dan dictionary attack terhadap hash MD5, terbukti bahwa algoritma hash yang cepat dan tanpa mekanisme pengamanan tambahan sangat rentan terhadap serangan offline. Password atau PIN dengan ruang kemungkinan kecil dapat ditemukan dalam waktu singkat. Oleh karena itu, sistem informasi modern harus menggunakan algoritma khusus pengamanan password seperti bcrypt atau Argon2 untuk meningkatkan ketahanan keamanan.

---

## 9. Daftar Pustaka
- Putra, D. M. J., Anantra, I. N. N. Y., Pratama, P. D. J., Saskara, G. A. J., & Listartha, I. M. E. (2022). Analisis Perbandingan Serangan Hydra, Medusa dan Ncrack pada Password Attack. Jurnal Informatika Teknologi dan Sains (Jinteks), 4(4), 461-466.
- Fachri, F. (2023). Optimasi Keamanan Web Server Terhadap Serangan Brute-Force Menggunakan Penetration Testing. Jurnal Teknologi Informasi dan Ilmu Komputer (JTIIK), 10(1), 51-58.
- Al Azhar, R. D., & Widiati, I. S. (2025, July). Evaluasi Keamanan Penyimpanan Password Menggunakan Algoritma Hash: MD5, SHA-1, dan Bcrypt. In Prosiding Seminar Nasional Teknologi Informasi dan Bisnis (pp. 1302-1305).

---

## 10. Commit Log

```
commit abc12345
Author: Sofyan Muzaki  <sofyan.muzaqi@gmail.com>
Date:   2025-09-20

   week14-analisis-serangan
```
