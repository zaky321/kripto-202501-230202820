# Laporan Praktikum Kriptografi
Minggu ke-: 7  
Topik: [Diffie-Hellman Key Exchange]  
Nama: [Sofyan Muzaki]  
NIM: [230202820]  
Kelas: [5IKRA]  

---

## 1. Tujuan
1. Melakukan simulasi protokol **Diffie-Hellman** untuk pertukaran kunci publik.  
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.  
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan **Man-in-the-Middle / MITM**).  

---

## 2. Dasar Teori
Diffie–Hellman pada dasarnya adalah cara dua orang untuk membuat kunci rahasia bersama meskipun mereka berkomunikasi lewat jaringan yang bisa saja disadap. Mekanismenya mengandalkan konsep matematika modular exponentiation dan kesulitan memecahkan discrete logarithm, sehingga orang lain yang mengintip prosesnya tetap tidak bisa mengetahui kunci akhirnya.

Prosesnya sederhana: kedua pihak sepakat dulu pada dua nilai publik, yaitu bilangan prima besar 𝑝 dan generator 𝑔. Setelah itu masing-masing membuat private key sendiri, lalu menghitung public key dengan rumus 𝑔𝑎mod𝑝. Nilai publik ini boleh dikirim secara terbuka. Nantinya, ketika masing-masing menghitung (𝑔𝑏)𝑎mod𝑝 atau sebaliknya, keduanya akan mendapatkan kunci rahasia yang sama tanpa pernah bertukar kuncinya secara langsung.

Keamanan metode ini muncul karena hampir tidak mungkin menebak private key hanya dari public key. Namun, Diffie–Hellman tetap punya kelemahan: ia tidak menyediakan autentikasi. Jadi tanpa mekanisme tambahan, komunikasi bisa disusupi man-in-the-middle. Karena itu, di praktik modern Diffie–Hellman biasanya dipasangkan dengan protokol lain untuk memastikan identitas masing-masing pihak.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
### Langkah 1 — Simulasi Diffie-Hellman
```python
import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)
```

Ekspektasi hasil: nilai `shared_secret_A` dan `shared_secret_B` harus sama.

---

## 6. Hasil dan Pembahasan
Hasil eksekusi program Deffie Hellman:
Berdasarkan hasil percobaan, mekanisme Diffie–Hellman terbukti mampu menghasilkan kunci rahasia yang sama pada kedua pihak tanpa harus bertukar kunci tersebut secara langsung. Proses ini bekerja karena sifat matematika perpangkatan modular yang membuat pihak ketiga hampir mustahil menebak private key hanya dari informasi publik.

Namun, simulasi serangan man-in-the-middle menunjukkan bahwa Diffie–Hellman memiliki kelemahan serius ketika tidak dilengkapi mekanisme autentikasi. Eve dapat mencegat dan mengganti public key sehingga Alice dan Bob akhirnya membentuk kunci berbeda dan komunikasi mereka sepenuhnya dapat dibaca atau dimanipulasi. Hal ini menegaskan bahwa Diffie–Hellman hanya aman bila dipadukan dengan sistem autentikasi tambahan, seperti sertifikat digital atau tanda tangan kriptografi, agar identitas masing-masing pihak benar-benar terverifikasi.

## Hasil Simulasi MITM
Hasil eksekusi program pada skenario MITM menunjukkan bahwa ketika Eve mencegat dan mengganti public key milik Alice dan Bob, proses pembentukan kunci tidak lagi berjalan sebagaimana mestinya. Alice menghitung kunci menggunakan public key palsu dari Eve, begitu juga Bob. Akibatnya, kunci yang dihasilkan Alice dan Bob berbeda, sehingga mereka sebenarnya tidak pernah berbagi kunci rahasia yang sama.

Sebaliknya, Eve justru mampu menghasilkan dua kunci yang valid: satu kunci yang identik dengan kunci yang dihitung Alice, dan satu lagi identik dengan kunci yang dihitung Bob. Ini berarti Eve berada tepat di tengah—dia dapat membaca, memodifikasi, atau meneruskan pesan seolah-olah komunikasi berlangsung normal. Secara keseluruhan, hasil simulasi memperlihatkan bahwa Diffie–Hellman tanpa autentikasi sangat rentan terhadap serangan MITM karena tidak ada mekanisme untuk memverifikasi keaslian public key yang dipertukarkan.


---

## 7. Jawaban Pertanyaan
 
- Pertanyaan 1: Diffie–Hellman memungkinkan dua pihak menyepakati kunci rahasia meskipun lewat saluran publik karena prosesnya hanya membutuhkan pertukaran public key, sementara nilai rahasianya tetap disimpan masing-                     masing. Keamanannya bertumpu pada kesulitan memecahkan discrete logarithm problem. Jadi meskipun seseorang mengintip semua informasi publik yang dikirim, ia tidak dapat menebak private key atau kunci                       rahasia yang terbentuk.
- Pertanyaan 2: Kelemahan terbesarnya adalah tidak ada autentikasi. Protokol asli hanya mengatur cara membuat kunci bersama, tetapi tidak memverifikasi siapa pemilik public key tersebut. Akibatnya, pihak ketiga bisa                       menyamar sebagai salah satu pihak dan mengganti public key tanpa terdeteksi. Celah inilah yang memungkinkan serangan man-in-the-middle.
- Pertanyaan 3: Cara utama mencegah MITM adalah menambahkan mekanisme autentikasi pada public key yang dipertukarkan. Beberapa metode yang umum digunakan:
                1.Sertifikat digital (PKI/SSL/TLS) → memastikan public key benar-benar milik pihak yang sah.
                2.Digital signature → public key ditandatangani menggunakan private key pemiliknya.
                3.Authenticated Diffie–Hellman → seperti dalam protokol TLS, SSH, atau Signal.
                Dengan autentikasi tersebut, penyerang tidak bisa lagi mengganti public key tanpa ketahuan, sehingga serangan MITM dapat dicegah.

---

## 8. Kesimpulan
Berdasarkan percobaan, Diffie–Hellman terbukti mampu menghasilkan kunci rahasia yang sama di kedua pihak meskipun pertukaran dilakukan melalui saluran publik. Namun, simulasi MITM menunjukkan bahwa tanpa autentikasi, protokol ini dapat dengan mudah disusupi karena penyerang dapat mengganti public key tanpa terdeteksi. Hal ini menegaskan bahwa Diffie–Hellman hanya aman jika dipadukan dengan mekanisme autentikasi tambahan.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Nasution, M. K., & Aulia, R. (2025). *IMPLEMENTASI ALGORITMA DIFFIE-HELLMAN KEY EXCHANGE (DHE) DAN AES DALAM ENKRIPSI PESAN END-TO-END. Jurnal Riset Multidisiplin Edukasi*, 2(10), 181-198.
- Gunawan, H., Budi, A. S., & Primananda, R. (2022). *Penerapan Algoritma Diffie Hellman Key Exchange dalam Komunikasi Data Antarnode pada Wireless Sensor Network. Jurnal Pengembangan Teknologi Informasi Dan Ilmu Komputer*, 6(1), 197-203.
---

## 10. Commit Log

```
commit abc12345
Author: Sofyan Muzaki  <sofyan.muzaqi@gmail.com>
Date:   2025-09-20

    week7-diffie-hellman 
```
