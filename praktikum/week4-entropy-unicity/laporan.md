# Laporan Praktikum Kriptografi
Minggu ke-: 4  
Topik: [Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)]  
Nama: [Sofyan Muzaki]  
NIM: [230202820]  
Kelas: [5IKRA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Menyelesaikan perhitungan sederhana terkait entropi kunci.
2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.
3. Menghitung unicity distance untuk ciphertext tertentu.
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

---

## 2. Dasar Teori

Entropy dalam konteks kriptografi menggambarkan tingkat ketidakpastian atau keacakan dalam suatu sistem kunci. Entropy diukur dalam satuan bit dan menunjukkan seberapa sulit kunci tersebut ditebak oleh pihak yang tidak berwenang. Semakin tinggi nilai entropinya, semakin besar jumlah kemungkinan kombinasi kunci yang harus diuji dalam serangan brute force. Entropy dihitung dengan rumus 
𝐻=−∑𝑝𝑖log⁡2𝑝𝑖​, di mana 𝑝𝑖 adalah probabilitas kemunculan setiap kemungkinan kunci. Dalam praktiknya, kunci dengan entropi rendah-misalnya karena pola yang mudah ditebak-akan sangat rentan terhadap serangan karena mengurangi ruang pencarian efektif bagi penyerang.

Unicity Distance adalah ukuran teoretis yang menggambarkan jumlah minimum ciphertext yang dibutuhkan untuk secara unik menentukan kunci enkripsi secara matematis. Konsep ini dikembangkan oleh Claude Shannon untuk menilai kekuatan sistem kriptografi terhadap analisis statistik. Semakin besar unicity distance suatu sistem, semakin sulit bagi penyerang untuk menemukan kunci tunggal yang valid, karena data ciphertext yang sedikit belum cukup memberikan informasi yang cukup untuk menebak kunci secara pasti. Dengan demikian, unicity distance menjadi indikator seberapa “aman” suatu algoritma dari serangan berbasis analisis frekuensi dan statistik.

Hubungan antara entropy dan unicity distance sangat erat dalam mengevaluasi kekuatan kunci terhadap serangan brute force. Entropy menunjukkan keragaman dan keacakan kunci, sedangkan unicity distance menilai kuantitas data yang diperlukan untuk menembus enkripsi. Dalam sistem dengan entropi tinggi, unicity distance biasanya juga tinggi, sehingga serangan brute force menjadi tidak efisien secara komputasional. Oleh karena itu, dalam perancangan sistem keamanan modern, kedua konsep ini digunakan bersama untuk mengukur sejauh mana algoritma kriptografi mampu bertahan terhadap eksploitasi berbasis pencarian menyeluruh (brute force attack) maupun analisis probabilistik.

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
1. Membuat file `entropy_unicity.py` di folder `praktikum/week4-entropy-unicity/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python entropy_unicity.py`.)

---

## 5. Source Code
### Langkah 1 — Perhitungan Entropi
 
\[
H(K) = \log_2 |K|
\]  
dengan \(|K|\) adalah ukuran ruang kunci.  

Contoh implementasi Python:  
```python
import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")
```

### Langkah 2 — Menghitung Unicity Distance

\[
U = \frac{H(K)}{R \cdot \log_2 |A|}
\]  
dengan:  
- \(H(K)\): entropi kunci,  
- \(R\): redundansi bahasa (misal bahasa Inggris \(R \approx 0.75\)),  
- \(|A|\): ukuran alfabet (26 untuk A–Z).  

Contoh implementasi Python:  
```python
def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))
```

### Langkah 3 — Analisis Brute Force
Simulasikan waktu brute force dengan asumsi kecepatan komputer tertentu.

```python
def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
```

---

## 6. Hasil dan Pembahasan

Hasil eksekusi program Entropy unicity:

![Hasil Eksekusi](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  )
- Pertanyaan 1:Nilai entropy mencerminkan tingkat keacakan dan ketidakpastian dalam sistem kunci. Dalam kriptografi, semakin tinggi entropinya (biasanya diukur dalam bit), semakin besar jumlah kemungkinan kunci yang harus                dicoba oleh penyerang untuk menebak kunci yang benar.Misalnya, kunci 128-bit memiliki entropi maksimum 128 bit artinya ada 2^128 kemungkinan kunci. Jika pengguna memilih kata sandi yang mudah ditebak                       (misalnya nama atau tanggal lahir), entropi nyata bisa turun jauh di bawah nilai teoritis, sehingga ruang pencarian efektif bagi penyerang menjadi jauh lebih kecil.
- Pertanyaan 2:Unicity distance menunjukkan berapa banyak ciphertext yang diperlukan untuk secara matematis menentukan satu kunci yang benar. Jika unicity distance suatu sistem besar, artinya dibutuhkan banyak data                       terenkripsi untuk menemukan kunci yang unik; sistem ini relatif lebih aman terhadap analisis statistik.Sebaliknya, cipher dengan unicity distance kecil (misalnya pada algoritma klasik seperti Vigenère                      dengan panjang kunci pendek) bisa dipecahkan hanya dengan sedikit ciphertext.
- Pertanyaan 3:Meskipun algoritma modern seperti AES dan RSA memiliki kompleksitas matematis yang sangat tinggi, serangan brute force tetap relevan karena kelemahan manusia yang sering menggunakan kunci berentropi rendah,                kesalahan sistemik dalam implementasi atau pengelolaan kunci, serta kemajuan komputasi paralel, GPU, dan Quantum Computing yang mempercepat proses penelusuran kombinasi kunci, sehingga meskipun algoritmanya                kuat secara teoretis, ancaman brute force tetap nyata apabila disiplin keamanan dan manajemen kunci tidak diterapkan dengan baik.

---

## 8. Kesimpulan
Berdasarkan percobaan, dapat disimpulkan bahwa nilai entropy berperan penting dalam menentukan tingkat keacakan dan kekuatan kunci, di mana semakin tinggi entropinya maka semakin sulit kunci tersebut ditebak melalui brute force. Nilai unicity distance menunjukkan seberapa banyak ciphertext yang dibutuhkan untuk menemukan kunci secara unik, sehingga semakin besar nilainya, semakin aman sistem dari analisis kriptografi. Dengan demikian, kombinasi antara entropi tinggi dan unicity distance besar menjadi indikator utama keandalan algoritma terhadap serangan brute force maupun analisis statistik.

---

## 9. Daftar Pustaka
  
- Pramudya, F. A., & Suhardi, S. (2025). *Analisis Keamanan Komparatif Caesar Cipher DES dalam Konteks Teknik Kriptografi Modern*. Cosmic Jurnal Teknik, 2(3), 96-105..  
- Rihartanto, R., Ningsih, R. K., Gaffar, A. F. O., & Utomo, D. S. B. (2020). *Implementasi vigenere cipher 128 dan rotasi bujursangkar untuk pengamanan teks*. Jurnal Teknologi dan Sistem Komputer, 8(3), 201-209..  )

---

## 10. Commit Log

```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
