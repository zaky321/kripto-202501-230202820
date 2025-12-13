# Laporan Praktikum Kriptografi
Minggu ke-: 9  
Topik: [Digital Signature (RSA/DSA)]  
Nama: [Sofyan Muzaki]  
NIM: [230202820]  
Kelas: [5IKRA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.  
2. Memverifikasi keaslian tanda tangan digital.  
3. Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.  

---

## 2. Dasar Teori

Tanda tangan digital adalah mekanisme kriptografi yang bertujuan memastikan keaslian (authenticity), integritas, dan non-repudiation suatu pesan. Secara konsep, tanda tangan digital bekerja kebalikan dari enkripsi: pengirim menandatangani pesan dengan private key, lalu penerima memverifikasi tanda tangan tersebut dengan public key. Jika verifikasi berhasil, berarti pesan benar berasal dari pemilik private key dan belum mengalami perubahan.

Dalam skema RSA, proses tanda tangan menggunakan prinsip perpangkatan modular pada pasangan kunci yang sama dengan enkripsi, hanya alurnya dibalik: hash pesan di-sign menggunakan private key, lalu penerima memeriksa dengan public key. Keamanan RSA bergantung pada sulitnya memfaktorkan bilangan besar. Sementara itu DSA (Digital Signature Algorithm) bekerja memakai konsep logaritma diskrit dan random per-signature nonce 
𝑘.DSA tidak melakukan enkripsi-dekripsi langsung seperti RSA, melainkan menghasilkan dua nilai tanda tangan (𝑟,𝑠) yang diverifikasi menggunakan public key dan hash pesan.

Meskipun keduanya berbeda secara matematis, prinsip dasarnya sama: tanda tangan digital mengikat identitas kunci privat ke hash pesan, sehingga setiap perubahan sekecil apa pun pada isi pesan akan membuat verifikasi gagal. Hasilnya adalah mekanisme yang kuat untuk menjamin integritas dan memastikan bahwa pengirim tidak bisa menyangkal pesan yang ia tanda tangani.

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
1. Membuat file `signature.py` di folder `praktikum/week9-digital-signature/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python signature.py`.)

---

## 5. Source Code
### Langkah 1 — Generate Key dan Buat Tanda Tangan
```python
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan yang akan ditandatangani
message = b"Hello, ini pesan penting."
h = SHA256.new(message)

# Buat tanda tangan dengan private key
signature = pkcs1_15.new(private_key).sign(h)
print("Signature:", signature.hex())
```

---

### Langkah 2 — Verifikasi Tanda Tangan
```python
try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")
```

---

### Langkah 3 — Uji Modifikasi Pesan
```python
# Modifikasi pesan
fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")
```
---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Signature.py:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan

- Pertanyaan 1: Perbedaan dasarnya ada pada tujuan dan arah penggunaan kuncinya. Pada enkripsi RSA, pengirim memakai public key milik penerima supaya hanya penerima yang bisa membuka pesan dengan private key-nya. Fokusnya                 adalah menjaga kerahasiaan data. Sementara itu, pada tanda tangan digital RSA, pengirim justru memakai private key-nya untuk menandatangani hash pesan, lalu orang lain bisa mengecek keasliannya pakai                       public key. Jadi, tanda tangan digital dipakai untuk membuktikan bahwa pesan memang berasal dari pengirim dan tidak diubah. Secara singkat: enkripsi melindungi isi pesan, tanda tangan digital melindungi                    identitas pengirim dan integritas pesan.
- Pertanyaan 2: Tanda tangan digital bisa menjaga integritas karena pesan selalu di-hash dulu. Hash ini sifatnya sangat sensitif—ubah satu karakter saja, hasilnya langsung beda jauh. Saat penerima memverifikasi, ia                        menghitung ulang hash pesan. Kalau hash tidak cocok dengan yang ditandatangani, berarti isi pesan sudah berubah. Untuk otentikasi, tanda tangan hanya bisa dibuat dengan private key yang seharusnya cuma                     dimiliki satu orang. Kalau verifikasi berhasil menggunakan public key, itu bukti kuat bahwa tanda tangan tersebut memang dibuat oleh pemilik private key, bukan orang lain.
- Pertanyaan 3:CA berfungsi sebagai pihak ketiga yang memastikan bahwa public key benar-benar milik orang atau organisasi yang mengklaimnya. Mereka memeriksa identitas pemilik kunci, lalu mengeluarkan sertifikat digital                  yang sudah ditandatangani oleh CA. Dengan begitu, pengguna tidak perlu ragu apakah public key yang dipakai untuk memverifikasi tanda tangan itu asli atau sudah diganti penyerang. Tanpa CA, sistem tanda                     tangan digital tetap berjalan, tapi kita tidak punya jaminan kalau identitas pemilik kunci benar. CA inilah yang membuat sistem tanda tangan digital aman dipakai di dunia nyata, seperti pada HTTPS, email,                  dan berbagai aplikasi keamanan lainnya.

---

## 8. Kesimpulan

Secara keseluruhan, tanda tangan digital merupakan mekanisme penting dalam keamanan informasi karena mampu memastikan bahwa sebuah pesan benar-benar berasal dari pengirim yang sah dan tidak mengalami perubahan. Berbeda dengan enkripsi RSA yang bertujuan menjaga kerahasiaan pesan, tanda tangan digital RSA menggunakan private key untuk membuktikan identitas pengirim dan menjaga integritas melalui proses hashing. Sistem ini menjadi lebih terpercaya ketika public key yang digunakan untuk verifikasi memiliki jaminan identitas, dan di sinilah peran Certificate Authority (CA) menjadi penting. CA memastikan bahwa public key yang digunakan memang milik pihak yang benar sehingga mencegah pemalsuan identitas maupun serangan man-in-the-middle. Dengan kombinasi konsep kriptografi dan validasi identitas ini, tanda tangan digital menjadi fondasi penting dalam komunikasi digital modern.

---

## 9. Daftar Pustaka

- Anshori, Y., Dodu, A. E., & Wedananta, D. M. P. (2019). Implementasi Algoritma Kriptografi Rivest Shamir Adleman (RSA) pada Tanda Tangan Digital. Techno. Com, 18(2), 110-121.  
- Gafrun, G., & Supit, Y. (2024). ALGORITMA TANDA TANGAN DIGITAL UNTUK MENINGKATKAN KEAMANAN PESAN. Simtek: jurnal sistem informasi dan teknik komputer, 9(2), 198-204.

---

## 10. Commit Log

Contoh:
```
commit 0819e28e0a023ffdaaf24f7a03bbcd451d714987 (HEAD -> main, origin/main, origin/HEAD)
Author: zaky321 <141202616+zaky321@users.noreply.github.com>
Date:   Sat Dec 13 22:19:23 2025 +0700

    week9-digital-signature 
```
