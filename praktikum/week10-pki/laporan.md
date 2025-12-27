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

Hasil eksekusi program PKI:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan

- Pertanyaan 1:Certificate Authority (CA) berfungsi sebagai pihak tepercaya yang memverifikasi identitas entitas (server, organisasi, atau individu) dan menerbitkan sertifikat digital yang mengaitkan identitas tersebut                   dengan public key. CA menandatangani sertifikat menggunakan private key miliknya sehingga keaslian dan integritas sertifikat dapat diverifikasi menggunakan public key CA yang telah dipercaya. Mekanisme ini                 membentuk chain of trust dalam Public Key Infrastructure (PKI), sebagaimana didefinisikan dalam standar X.509 (RFC 5280).
- Pertanyaan 2: Self-signed certificate tidak cukup untuk sistem produksi karena tidak melibatkan validasi identitas oleh pihak ketiga tepercaya. Pada sertifikat self-signed, issuer dan subject adalah entitas yang sama,                   sehingga klien tidak memiliki dasar objektif untuk mempercayai keaslian identitas pemilik sertifikat. Penelitian dan praktik industri menunjukkan bahwa sertifikat jenis ini rentan terhadap penyamaran dan                   umumnya ditolak secara default oleh browser dan sistem operasi, sehingga hanya cocok untuk kebutuhan pengujian atau pembelajaran.
- Pertanyaan 3: PKI mencegah serangan Man-in-the-Middle (MITM) dalam TLS/HTTPS dengan memastikan bahwa public key server benar-benar milik server yang sah. Saat proses handshake TLS, klien memverifikasi tanda tangan                       sertifikat server menggunakan public key CA tepercaya. Jika sertifikat palsu atau telah dimodifikasi, verifikasi akan gagal dan koneksi dibatalkan, sehingga penyerang tidak dapat menggantikan public key                    server tanpa terdeteksi.

---

## 8. Kesimpulan

Dari percobaan yang dilakukan, sertifikat digital berhasil dibuat dan ditandatangani, lalu tanda tangannya bisa diverifikasi menggunakan public key yang sesuai. Hasil ini menunjukkan bahwa isi sertifikat tidak berubah dan benar-benar berasal dari pihak yang menandatanganinya. Secara sederhana, percobaan ini membuktikan bagaimana PKI bekerja untuk menjaga kepercayaan dan keamanan komunikasi.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Arifin, S. Implementasi Public Key Infrastructure untuk Keamanan Sistem Pengiriman Data Pilkada Via Mobile.  
- Auliafitri, D., RizkiSuro, E., Malik, M. R. M., & Setiawan, A. (2024). Optimalisasi Pengujian Penetrasi: Penerapan Serangan MITM (Man in the Middle Attack) menggunakan Websploit. Journal of Internet and Software Engineering, 1(3), 12-12.
- Husaini, H., Ramadhan, T. H., & Ihsan, M. (2025). PENERAPAN HIERARKI CERTIFICATE AUTHORITY DAN PUBLIC KEY INFRASTRUCTURE UNTUK MEMPERKUAT KEAMANAN JARINGAN. Cyberspace: Jurnal Pendidikan Teknologi Informasi, 9(1), 63-74.
---

## 10. Commit Log

```
commit be5ef8b2429474299ff9e207a8809e98b60e7654
Author: zaky321 <141202616+zaky321@users.noreply.github.com>
Date:   Sat Dec 27 22:28:51 2025 +0700

    week10-pki 
```
