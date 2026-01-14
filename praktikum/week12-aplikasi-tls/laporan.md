# Laporan Praktikum Kriptografi
Minggu ke-: 12  
Topik: [Aplikasi TLS & E-commerce]  
Nama: [Sofyan Muzaki]  
NIM: [230202820]  
Kelas: [5IKRA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menganalisis penggunaan kriptografi pada **email** dan **SSL/TLS**.  
2. Menjelaskan enkripsi dalam transaksi **e-commerce**.  
3. Mengevaluasi isu **etika & privasi** dalam penggunaan kriptografi di kehidupan sehari-hari.  

---

## 2. Dasar Teori
Transport Layer Security (TLS) merupakan protokol keamanan yang berfungsi untuk melindungi komunikasi data pada jaringan internet melalui mekanisme enkripsi, autentikasi, dan integritas data. TLS bekerja dengan mengenkripsi data yang dikirim antara klien (misalnya browser pengguna) dan server sehingga informasi sensitif seperti username, password, dan data transaksi tidak dapat dibaca oleh pihak yang tidak berwenang. Selain itu, TLS menggunakan sertifikat digital berbasis kriptografi kunci publik untuk memastikan identitas server yang diakses adalah sah.

Dalam konteks e-commerce, TLS memiliki peran yang sangat krusial karena seluruh proses transaksi, mulai dari login pengguna, pengisian data pribadi, hingga pembayaran online, melibatkan pertukaran data yang bersifat rahasia. Penerapan TLS pada website e-commerce (ditandai dengan penggunaan HTTPS) membantu mencegah serangan seperti penyadapan (sniffing), man-in-the-middle, dan pemalsuan data transaksi, sehingga meningkatkan kepercayaan pengguna terhadap platform tersebut.

Dengan adanya TLS, sistem e-commerce dapat menjamin bahwa data transaksi dikirim secara aman dan tidak dimodifikasi selama proses transmisi. Hal ini tidak hanya melindungi pengguna, tetapi juga menjaga reputasi dan kredibilitas penyedia layanan e-commerce, karena keamanan komunikasi menjadi salah satu faktor utama dalam keberhasilan dan keberlanjutan bisnis digital.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
### Langkah 1 — Analisis SSL/TLS pada Email & Web
- Gunakan browser (Chrome/Firefox) untuk mengecek **sertifikat digital** pada website e-commerce (contoh: Tokopedia, Shopee, Bukalapak).  
- Catat informasi berikut:  
  - Issuer CA (Certificate Authority).  
  - Masa berlaku sertifikat.  
  - Algoritma enkripsi yang digunakan (RSA, AES, dll).  
- Bandingkan perbedaan antara website **dengan HTTPS** dan **tanpa HTTPS**.  

---

### Langkah 2 — Studi Kasus E-commerce
- Analisis bagaimana enkripsi digunakan untuk melindungi transaksi online (misalnya saat login atau melakukan pembayaran).
      Pada transaksi online seperti login dan pembayaran, enkripsi TLS bekerja dengan membentuk secure channel antara browser pengguna dan server. Saat koneksi HTTPS dibuat, terjadi proses TLS handshake di mana server           mengirimkan sertifikat digital (seperti pada contoh Shopee) untuk memverifikasi identitasnya. Setelah itu, kunci sesi simetris dibentuk dan digunakan untuk mengenkripsi seluruh data yang dikirim, termasuk username,        password, nomor kartu, dan detail transaksi. Dengan mekanisme ini, data yang melintas di jaringan hanya dapat dibaca oleh pihak yang memiliki kunci yang sah.

      Enkripsi TLS juga menjamin integritas data, artinya data tidak bisa diubah di tengah perjalanan tanpa terdeteksi. Jika ada upaya modifikasi, sistem akan menolak komunikasi tersebut. Dalam konteks e-commerce, hal ini       penting agar nilai transaksi, tujuan pembayaran, dan identitas penerima tidak dapat dimanipulasi oleh pihak ketiga. Selain itu, penggunaan sertifikat dari Certificate Authority (CA) terpercaya memastikan bahwa             pengguna benar-benar terhubung ke server resmi, bukan server palsu.
- Diskusikan potensi ancaman jika TLS tidak digunakan (contoh: serangan Man-in-the-Middle).
   Jika TLS tidak digunakan, komunikasi antara pengguna dan server akan dikirim dalam bentuk plaintext, sehingga sangat rentan terhadap serangan Man-in-the-Middle (MitM). Dalam skenario ini, penyerang yang berada di           jaringan yang sama (misalnya Wi-Fi publik) dapat menyadap lalu lintas data, mencuri kredensial login, atau bahkan mengubah isi transaksi tanpa disadari pengguna. Login dapat dibajak, dan pembayaran dapat dialihkan ke      rekening penyerang.

  Selain MitM, ketiadaan TLS juga membuka peluang credential theft, session hijacking, dan pemalsuan identitas server (spoofing). Pengguna tidak memiliki cara teknis untuk memastikan bahwa website yang diakses adalah        situs e-commerce asli. Secara logis, tanpa TLS, klaim keamanan transaksi online menjadi rapuh karena tidak ada jaminan kerahasiaan, keaslian, maupun integritas data—tiga pilar utama keamanan informasi.

---

### Langkah 3 — Analisis Etika & Privasi
- Identifikasi isu privasi dalam penggunaan email terenkripsi (PGP, S/MIME).
      PGP dan S/MIME melindungi isi email dengan enkripsi, tetapi privasi tidak otomatis sempurna karena metadata (pengirim–penerima, waktu, pola komunikasi, sering juga subjek) masih dapat terlihat dan dianalisis. Selain       itu, pada lingkungan organisasi, terutama S/MIME, pengelolaan sertifikat/kunci bisa melibatkan perusahaan sehingga ada risiko kontrol institusi (misalnya penyimpanan kunci cadangan) yang dapat mengurangi kendali           privasi individu.
  
- Diskusikan dilema etika:  
  - Apakah perusahaan boleh melakukan dekripsi email karyawan untuk audit?
    perusahaan bisa beralasan melakukan dekripsi email karyawan untuk audit keamanan, kepatuhan, atau investigasi insiden karena email kerja adalah sarana kerja. Namun, secara etis hal ini hanya dapat dibenarkan jika ada      kebijakan tertulis dan transparan, tujuan yang spesifik dan proporsional, serta dekripsi dilakukan sebagai upaya terakhir, bukan pemantauan rutin, agar tidak berubah menjadi pengawasan berlebihan.
    
  - Bagaimana kebijakan pemerintah dalam pengawasan komunikasi terenkripsi?
    pengawasan komunikasi terenkripsi sering dibenarkan untuk penegakan hukum dan keamanan nasional. Tetapi pelemahan enkripsi (misalnya backdoor/key escrow) berisiko membahayakan semua pengguna karena celah dapat             disalahgunakan dan mendorong pengawasan massal. Karena itu, jika ada akses, harus dibatasi oleh dasar hukum yang jelas, izin dan pengawasan independen, serta prinsip kebutuhan dan proporsionalitas.
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
  
- Pertanyaan 1:Perbedaan utama HTTP dan HTTPS terletak pada aspek keamanannya. HTTP mengirim data dalam bentuk plaintext sehingga mudah disadap atau dimodifikasi oleh pihak lain. Sebaliknya, HTTPS menggunakan TLS untuk                   mengenkripsi data, sehingga komunikasi antara klien dan server menjadi lebih aman, terlindungi dari penyadapan, dan memiliki jaminan integritas.
- Pertanyaan 2:Sertifikat digital penting dalam komunikasi TLS karena berfungsi untuk memverifikasi identitas server. Sertifikat ini dikeluarkan oleh Certificate Authority (CA) terpercaya dan memastikan bahwa pengguna                    benar-benar terhubung ke server yang sah, bukan server palsu. Selain itu, sertifikat digital memungkinkan pertukaran kunci enkripsi secara aman pada awal komunikasi.
- Pertanyaan 3: Kriptografi mendukung privasi dengan melindungi kerahasiaan dan integritas data komunikasi digital, sehingga hanya pihak yang berwenang yang dapat mengakses informasi tersebut. Namun, kriptografi juga                      menimbulkan tantangan hukum dan etika, karena enkripsi yang kuat dapat menghambat penegakan hukum dan mendorong perdebatan antara perlindungan privasi individu dan kebutuhan pengawasan oleh negara atau                     institusi.

---

## 8. Kesimpulan
Dari percobaan, enkripsi (misalnya HTTPS/TLS) bikin data login dan transaksi jadi aman karena isinya tidak gampang disadap atau diubah orang lain. Kalau tidak pakai enkripsi, komunikasi rawan banget kena serangan seperti Man-in-the-Middle yang bisa nyolong atau ngacak data. Jadi, TLS itu penting supaya transaksi online tetap aman dan pengguna lebih percaya.

---

## 9. Daftar Pustaka
- Sujarwo, S. (2016). PENGEMBANGAN SISTEM INFORMASI E-COMMERCE DENGAN SECURITY SSL PADA JANIS’S FOOTWEAR. Jurnal Surya Informatika, 2(1).
- Suliman, A. H. (2023). Analisis Keamanan Protokol Kriptografi SSL/TLS dengan Algoritma ECC pada Layanan Transaksi Online pada E-Commerce.
- Amelia, N., Ihwan, K., & Amin, M. (2025). Audit Keamanan Aplikasi Web Studi Kasus pada Website E-Commerce Warung Ayam Goreng Selimut Griya Cirebon. TEKNOFILE: Jurnal Sistem Informasi, 3(4), 244-249.
---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit 8fd940902e759818fd3d7b5935b458dd667bcc14
Author: Sofyan Muzaki <sofyan.muzaqi@gmail.com>
Date:    Wed Jan 14 22:38:55 2026 +0700

   week12-aplikasi-tls.
 )
```
