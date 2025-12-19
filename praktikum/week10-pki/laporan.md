# Laporan Praktikum Kriptografi
Minggu ke-: 10  
Topik: [Public Key Infrastructure (PKI & Certificate Authority)]  
Nama: [Sofyan Muzaki]  
NIM: [230202820]  
Kelas: [5IKRA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Membuat sertifikat digital sederhana.  
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.  
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).  
---

## 2. Dasar Teori
Public Key Infrastructure (PKI) adalah kerangka kerja yang digunakan untuk mengelola kunci kriptografi asimetris (public key dan private key) agar komunikasi digital dapat berlangsung secara aman. PKI menyediakan mekanisme untuk pembuatan, distribusi, penyimpanan, penggunaan, dan pencabutan sertifikat digital. Sertifikat digital ini berfungsi sebagai identitas elektronik yang mengaitkan sebuah public key dengan identitas pemiliknya (individu, server, atau organisasi), sehingga pihak lain dapat mempercayai bahwa kunci publik tersebut benar milik entitas yang dimaksud. Tanpa PKI, penggunaan kriptografi kunci publik akan rentan terhadap penyamaran identitas dan serangan man-in-the-middle.

Certificate Authority (CA) merupakan komponen utama dalam PKI yang berperan sebagai pihak tepercaya untuk menerbitkan dan memverifikasi sertifikat digital. CA melakukan proses validasi identitas sebelum mengeluarkan sertifikat, lalu menandatanganinya secara digital menggunakan private key milik CA. Tanda tangan ini memungkinkan siapa pun untuk memverifikasi keaslian sertifikat menggunakan public key CA. Dengan mekanisme ini, CA membangun chain of trust, di mana kepercayaan terhadap sertifikat pengguna bergantung pada kepercayaan terhadap CA atau root CA yang diakui secara luas.

Dalam praktiknya, PKI dan CA digunakan secara luas pada berbagai layanan digital, seperti HTTPS pada web, tanda tangan digital, email terenkripsi, dan autentikasi sistem. Keberadaan PKI memastikan tiga aspek utama keamanan informasi, yaitu otentikasi (identitas pihak dapat diverifikasi), integritas (data tidak diubah selama transmisi), dan non-repudiation (pihak tidak dapat menyangkal telah melakukan suatu transaksi digital). Oleh karena itu, PKI dan CA menjadi fondasi penting dalam membangun kepercayaan dan keamanan pada sistem komunikasi modern.

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
1. Membuat file `pki_cert.py` di folder `praktikum/week10-pki/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python pki_cert.py`.)

---

## 5. Source Code
### Langkah 1 — Membuat Sertifikat Digital Sederhana
Contoh dengan Python `cryptography`:
```python
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# Generate key pair
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Buat subject & issuer (CA sederhana = self-signed)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
])

# Buat sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
)

# Simpan sertifikat
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat digital berhasil dibuat: cert.pem")
```

---

### Langkah 2 — Memverifikasi Sertifikat
- Gunakan public key untuk memverifikasi tanda tangan sertifikat.  
- Jelaskan bagaimana CA digunakan untuk menjamin keaslian sertifikat.  

---

### Langkah 3 — Analisis PKI
Diskusikan kasus nyata:  
- Bagaimana browser memverifikasi sertifikat HTTPS?  
- Apa yang terjadi jika CA palsu menerbitkan sertifikat?  
- Mengapa PKI penting dalam komunikasi aman (misalnya transaksi online)?  


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
