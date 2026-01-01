# Laporan Praktikum Kriptografi
Minggu ke-: 11  
Topik: [Secret Sharing (Shamir’s Secret Sharing)]  
Nama: [Sofyan Muzaki]  
NIM: [230202820]  
Kelas: [5IKRA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menjelaskan konsep **Shamir Secret Sharing** (SSS).  
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.  
3. Menganalisis keamanan skema distribusi rahasia.  
---

## 2. Dasar Teori
Shamir’s Secret Sharing (SSS) adalah skema kriptografi yang digunakan untuk membagi sebuah rahasia (misalnya kunci kriptografi) menjadi beberapa bagian (shares) dan mendistribusikannya kepada sejumlah pihak. Skema ini bersifat (k, n)-threshold, artinya rahasia hanya dapat direkonstruksi jika minimal k dari n bagian digabungkan, sementara kurang dari k bagian tidak memberikan informasi berarti tentang rahasia. Konsep ini pertama kali diperkenalkan oleh Adi Shamir pada tahun 1979 sebagai solusi untuk mengurangi risiko kegagalan tunggal (single point of failure) dalam penyimpanan rahasia.

Secara matematis, Shamir’s Secret Sharing memanfaatkan polinomial berderajat (k−1) di atas aritmetika modulo bilangan prima. Nilai rahasia ditempatkan sebagai konstanta polinomial, lalu setiap share merupakan titik berbeda pada kurva polinomial tersebut. Karena secara teori diperlukan minimal k titik untuk merekonstruksi polinomial berderajat (k−1), maka hanya dengan k share atau lebih rahasia dapat dihitung kembali menggunakan interpolasi Lagrange. Kurang dari k share tidak cukup untuk menentukan polinomial, sehingga kerahasiaan tetap terjaga secara informasi-teoretis.

Dalam praktik, Shamir’s Secret Sharing banyak digunakan pada sistem keamanan modern seperti manajemen kunci kriptografi, backup kunci enkripsi, dan kontrol akses terdistribusi. Keunggulan utamanya adalah keamanan yang kuat tanpa asumsi komputasi (tidak bergantung pada kesulitan masalah matematika tertentu), serta fleksibilitas dalam menentukan ambang batas peserta. Namun, skema ini tidak secara otomatis menyediakan mekanisme verifikasi keaslian share, sehingga pada implementasi nyata sering dikombinasikan dengan teknik kriptografi tambahan.

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
### Langkah 1 — Implementasi Shamir Secret Sharing
Contoh sederhana dengan library `secretsharing`:

```python
from secretsharing import SecretSharer

# Rahasia yang ingin dibagi
secret = "KriptografiUPB2025"

# Bagi menjadi 5 shares, ambang batas 3 (minimal 3 shares untuk rekonstruksi)
shares = SecretSharer.split_secret(secret, 3, 5)
print("Shares:", shares)

# Rekonstruksi rahasia dari 3 shares
recovered = SecretSharer.recover_secret(shares[:3])
print("Recovered secret:", recovered)
```

---

### Langkah 2 — Simulasi Manual (Tanpa Library)
Mahasiswa juga dapat mencoba membuat implementasi manual berbasis **polinomial modulo p** untuk memahami konsep matematis.  
- Pilih bilangan prima p yang cukup besar.  
- Bangun polinomial f(x) = a0 + a1x + … + ak-1x^(k-1) mod p, dengan a0 = secret.  
- Bagikan (x, f(x)) sebagai share.  
- Rekonstruksi menggunakan **Lagrange Interpolation**.  

---

### Langkah 3 — Analisis Keamanan
Diskusikan:
- Mengapa skema (k, n) aman meskipun sebagian share bocor?  
- Apa risiko jika threshold k terlalu kecil atau terlalu besar?  
- Bagaimana penerapan SSS di dunia nyata (contoh: manajemen kunci cryptocurrency, recovery password)?  


---

## 6. Hasil dan Pembahasan

Hasil eksekusi program secret-sharing:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan

- Pertanyaan 1:Keuntungan utama Shamir’s Secret Sharing (SSS) dibandingkan membagikan salinan kunci secara langsung adalah kemampuannya menghilangkan risiko single point of failure. Jika kunci dibagikan dalam bentuk                      salinan utuh, kebocoran satu salinan saja sudah cukup untuk membahayakan seluruh sistem. Pada Shamir’s Secret Sharing yang diperkenalkan oleh Adi Shamir, setiap pihak hanya memegang sebagian kunci (share)                  yang tidak memiliki arti apa pun jika berdiri sendiri. Selama jumlah share yang dikumpulkan kurang dari ambang batas yang ditentukan, rahasia tetap aman secara matematis dan tidak bisa ditebak.
- Pertanyaan 2:Threshold (k) berperan sebagai penentu utama tingkat keamanan dalam secret sharing. Nilai k menunjukkan jumlah minimum share yang harus digabungkan untuk merekonstruksi rahasia. Jika jumlah share yang                      tersedia kurang dari k, maka tidak ada informasi berarti tentang rahasia yang dapat diperoleh. Sebaliknya, jika jumlah share mencapai atau melebihi k, rahasia dapat dipulihkan sepenuhnya. Dengan demikian,                  threshold k mengatur keseimbangan antara keamanan dan ketersediaan, sehingga harus ditentukan sesuai kebutuhan dan tingkat kepercayaan antar pihak.
- Pertanyaan 3: Contoh penerapan nyata Shamir’s Secret Sharing dapat ditemukan pada penyimpanan kunci master enkripsi database perusahaan. Kunci utama dibagi menjadi beberapa share dan didistribusikan ke beberapa pejabat                  penting, misalnya manajer IT dan kepala keamanan. Dengan skema ini, kunci hanya bisa digunakan jika kedua pihak bekerja sama, sehingga mencegah penyalahgunaan oleh satu orang sekaligus meningkatkan                         keamanan sistem. Pendekatan ini banyak digunakan dalam sistem keamanan modern karena efektif dalam menjaga kerahasiaan dan kontrol akses.

---

## 8. Kesimpulan
Berdasarkan percobaan yang dilakukan, terlihat bahwa rahasia hanya bisa dibuka ketika jumlah share yang digabungkan sudah memenuhi nilai threshold (k). Jika share yang tersedia kurang dari k, maka rahasia tidak bisa diketahui sama sekali. Hal ini menunjukkan bahwa Shamir’s Secret Sharing efektif untuk menjaga keamanan kunci dan mencegah ketergantungan pada satu pihak saja.

---

## 9. Daftar Pustaka

- Sinaga, R., Purba, S., & Siburian, R. M. (2023). APLIKASI PEMAHAMAN DAN PENERAPAN FAST (k, n) THRESHOLD SECRET SHARING SCHEME. Jurnal Teknologi, Informasi dan Industri, 3(1), 76-83.
- Nanda, N. A., Sari, M., & Gunawan, I. (2023). Kriptografi dan Penerapannya Dalam Sistem Keamanan Data. Jurnal Media Informatika, 4(2), 90-93.
---

## 10. Commit Log


```
commit abc12345
Author: Sofyan Muzaki <sofyan.muzaqi@gmail.com>
Date:   2025-09-20

   week11-secret-sharing
```
