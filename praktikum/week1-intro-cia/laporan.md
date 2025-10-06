# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: Sejarah kriptografi dan Prinsip CIA
Nama: Sofyan Muzaki
NIM: 230202820  
Kelas: 5IKRA

---

## 1. Tujuan
1. Menjelaskan sejarah dan evolusi kriptografi dari masa klasik hingga modern.
2. Menyebutkan prinsip Confidentiality, Integrity, Availability (CIA) dengan benar.
3. Menyimpulkan peran kriptografi dalam sistem keamanan informasi modern.
4. Menyiapkan repositori GitHub sebagai media kerja praktikum.

---

## 2. Dasar Teori
Cipher klasik adalah salah satu bentuk awal dari teknik kriptografi yang digunakan untuk menyembunyikan pesan agar tidak mudah dibaca oleh orang lain. Cara kerjanya yaitu dengan mengganti atau menggeser huruf-huruf dalam teks asli (plaintext) menjadi teks sandi (ciphertext). Beberapa contoh cipher klasik yang cukup dikenal antara lain Caesar Cipher, Vigenère Cipher, dan Transposition Cipher. Walaupun sederhana, konsep cipher klasik ini menjadi dasar dari berbagai metode enkripsi yang digunakan dalam sistem keamanan modern.

Dalam proses enkripsi dan dekripsi pada cipher klasik, digunakan konsep aritmetika modular, yaitu operasi matematika yang menggunakan sisa hasil pembagian. Misalnya pada Caesar Cipher, setiap huruf digeser sejauh k posisi menggunakan rumus C = (P + k) mod 26, di mana P adalah huruf asli, k adalah kunci pergeseran, dan C adalah hasil enkripsi. Operasi ini memastikan pergeseran huruf tetap berada dalam rentang alfabet.

Meskipun cipher klasik sudah jarang digunakan karena mudah dipecahkan, konsep dasarnya tetap penting untuk dipahami. Prinsip seperti pergeseran huruf dan penggunaan modulus masih digunakan pada algoritma kriptografi yang lebih kompleks, seperti RSA dan Diffie-Hellman, yang berperan besar dalam menjaga keamanan data di era digital sekarang.


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
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
