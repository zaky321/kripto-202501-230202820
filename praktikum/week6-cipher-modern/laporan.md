# Laporan Praktikum Kriptografi
Minggu ke-: 6  
Topik: [Cipher Modern (DES, AES, RSA)]  
Nama: [Sofyan Muzaki]  
NIM: [230202820]  
Kelas: [5IKRA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Mengimplementasikan algoritma **DES** untuk blok data sederhana.  
2. Menerapkan algoritma **AES** dengan panjang kunci 128 bit.  
3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma **RSA**.  

---

## 2. Dasar Teori
Cipher modern pada dasarnya dibangun di atas prinsip kriptografi kuat yang mengatasi kelemahan cipher klasik, seperti pola yang mudah ditebak atau ruang kunci kecil. Data Encryption Standard (DES) adalah salah satu algoritma simetris awal yang sangat berpengaruh, memanfaatkan struktur Feistel network dengan blok 64-bit dan kunci efektif 56-bit. Meskipun mekanismenya elegan, kekuatan DES runtuh seiring meningkatnya kemampuan komputasi brute-force terhadap 56-bit kini dianggap trivial. Ini menunjukkan prinsip penting: keamanan cipher bergantung pada ukuran kunci dan ketahanan terhadap eksploitasi struktural (differential dan linear cryptanalysis).

Sebagai penerus, Advanced Encryption Standard (AES) mengadopsi desain berbasis substitution–permutation network dengan ukuran kunci 128/192/256-bit. AES tidak hanya memperbesar ruang kunci, tetapi juga memperbaiki struktur internal sehingga tahan terhadap serangan analitis mutakhir. Transformasi seperti SubBytes, ShiftRows, MixColumns, dan AddRoundKey menghasilkan difusi dan konfusi yang jauh lebih kuat dibanding DES. Karena efisiensi dan keamanannya, AES menjadi standar global untuk enkripsi simetris, baik di perangkat kecil maupun aplikasi cloud.

Berbeda dari DES/AES, RSA bekerja dengan paradigma asymmetric cryptography. Keamanannya tidak bergantung pada kerahasiaan algoritma, tetapi pada kesulitan faktorisasi bilangan besar (prime factorization). RSA menggunakan pasangan kunci publik–privat serta operasi matematika modular eksponensial. Namun, kekuatan RSA bukan semata-mata soal panjang kunci (misalnya 2048 atau 4096 bit), melainkan juga implementasi aman: pemilihan prime yang benar, padding yang kuat (OAEP), dan perlindungan terhadap side-channel attacks. RSA memberi fondasi bagi tanda tangan digital dan distribusi kunci, tetapi sering dipasangkan dengan AES dalam protokol modern karena sifatnya yang lebih lambat untuk enkripsi data besar.

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
1. Membuat file `Cipher Modern.py` di folder ` praktikum/week6-cipher-modern/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python Cipher Modern.py`.)

---

## 5. Source Code
### Langkah 1 — Implementasi DES (Opsional, Simulasi)
```python
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)  # kunci 64 bit (8 byte)
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"ABCDEFGH"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)
```
---

### Langkah 2 — Implementasi AES-128
```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 128 bit key
cipher = AES.new(key, AES.MODE_EAX)

plaintext = b"Modern Cipher AES Example"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print("Ciphertext:", ciphertext)

# Dekripsi
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
```
---

### Langkah 3 — Implementasi RSA
```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Enkripsi dengan public key
cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"RSA Example"
ciphertext = cipher_rsa.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Dekripsi dengan private key
decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
```

---

## 6. Hasil dan Pembahasan
Hasil eksekusi program Cipher Modern:

![Hasil Eksekusi](screenshots/output.png)


---

## 7. Jawaban Pertanyaan

- Pertanyaan 1:   DES dan AES adalah algoritma simetris, memakai kunci yang sama untuk enkripsi–dekripsi, sedangkan RSA asimetris dengan pasangan kunci publik–privat. DES menggunakan kunci 56-bit yang kini mudah di-brute-                   force, sementara AES memiliki kunci 128/192/256-bit dengan struktur jauh lebih kuat. RSA tidak bergantung pada ukuran kunci simetris, tetapi pada sulitnya memfaktorkan bilangan besar, sehingga bentuk                       keamanannya berbasis masalah matematika, bukan ruang kunci semata.
- Pertanyaan 2:   AES lebih aman karena ukuran kuncinya jauh lebih besar dan desain internalnya tahan terhadap serangan modern, sedangkan DES tidak lagi layak karena kuncinya terlalu pendek. Selain itu, AES jauh lebih                       cepat dan efisien di perangkat modern, termasuk prosesor yang memiliki instruksi hardware khusus AES.
- Pertanyaan 3:   RSA disebut asimetris karena memakai dua kunci berbeda: kunci publik untuk enkripsi/validasi dan kunci privat untuk dekripsi/tanda tangan digital. Kunci RSA dihasilkan dengan memilih dua bilangan prima                     besar p dan q, menghitung n = p×q, menentukan φ(n), memilih eksponen publik e, lalu menghitung eksponen privat d yang merupakan invers modular dari e terhadap φ(n). Publikasi (e, n) menjadi kunci publik,                   sedangkan (d, n) disimpan sebagai kunci privat.

---

## 8. Kesimpulan
Percobaan menunjukkan bahwa DES tidak lagi mampu memberikan keamanan memadai karena ukuran kuncinya terlalu kecil, sedangkan AES terbukti jauh lebih kuat dan efisien untuk kebutuhan enkripsi modern. RSA bekerja efektif sebagai algoritma asimetris karena proses pembangkitan kuncinya berbasis masalah faktorisasi bilangan besar yang sangat sulit dipecahkan. Kombinasi AES dan RSA memberikan perlindungan yang lebih andal untuk sistem keamanan masa kini.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Meko, D. A. (2018). *Perbandingan Algoritma DES, AES, IDEA Dan Blowfish dalam Enkripsi dan Dekripsi Data.* Jurnal Teknologi Terpadu, 4(1)..  
- Dalia, D., Anwar, B., & Setiawan, D. (2021). *Implementasi Algoritma Rsa Untuk Keamanan Data Mutasi Pada PT. SSSS Kuala Tanjung.* Jurnal Cyber Tech, 4(6).
- Simbolon, I. A. R., Gunawan, I., Kirana, I. O., Dewi, R., & Solikhun, S. (2020). *Penerapan Algoritma AES 128-Bit dalam Pengamanan Data Kependudukan pada Dinas Dukcapil Kota Pematangsiantar.* Journal of Computer System and Informatics (JoSYC), 1(2), 54-60.

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Sofyan Muzaki <sofyan.muzaqi@gmail.com>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
