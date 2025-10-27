# Laporan Praktikum Kriptografi
Minggu ke-: 3 
Topik: Modular Math
Nama: Sofyan Muzaki
NIM: 230202820
Kelas: 5IKRA

---

## 1. Tujuan

Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:
1. Menyelesaikan operasi aritmetika modular.
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.

---

## 2. Dasar Teori
Aritmetika modular adalah salah satu cabang penting dalam matematika yang membahas operasi bilangan berdasarkan sisa hasil bagi terhadap suatu bilangan tertentu yang disebut modulus. Dua bilangan dikatakan kongruen jika memiliki sisa yang sama saat dibagi dengan modulus yang sama, ditulis sebagai 𝑎≡𝑏(mod𝑛). Konsep ini banyak digunakan dalam bidang ilmu komputer, terutama pada kriptografi, karena mampu membatasi operasi bilangan dalam ruang nilai tertentu sehingga perhitungannya lebih efisien dan aman.

Konsep lain yang erat kaitannya adalah Greatest Common Divisor (GCD) atau faktor persekutuan terbesar, yaitu bilangan terbesar yang dapat membagi dua bilangan tanpa meninggalkan sisa. Perhitungan GCD biasanya dilakukan dengan algoritma Euclidean dan menjadi dasar dalam menentukan invers modular, yang penting dalam proses enkripsi dan dekripsi data. Selain itu, bilangan prima juga berperan besar karena sifatnya yang unik—hanya dapat dibagi oleh 1 dan dirinya sendiri—membuatnya sangat berguna dalam sistem keamanan digital seperti algoritma RSA.

Sementara itu, logaritma diskrit merupakan kebalikan dari operasi perpangkatan dalam aritmetika modular, yaitu mencari nilai 𝑥 yang memenuhi 𝑔x≡𝑦(mod𝑝). Masalah logaritma diskrit terkenal sulit diselesaikan dalam waktu singkat, sehingga digunakan sebagai dasar keamanan berbagai sistem kriptografi modern, seperti Diffie-Hellman Key Exchange dan ElGamal. Secara keseluruhan, keterkaitan antara aritmetika modular, GCD, bilangan prima, dan logaritma diskrit membentuk dasar teori yang sangat penting dalam dunia keamanan informasi dan teknologi kriptografi masa kini.

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
1. Aritmetika Modular

        def mod_add(a, b, n): return (a + b) % n
        def mod_sub(a, b, n): return (a - b) % n
        def mod_mul(a, b, n): return (a * b) % n
        def mod_exp(base, exp, n): return pow(base, exp, n)  # eksponensiasi modular

        print("7 + 5 mod 12 =", mod_add(7, 5, 12))
        print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
        print("7^128 mod 13 =", mod_exp(7, 128, 13))

2. GCD & Algoritma Euclidean

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        print("gcd(54, 24) =", gcd(54, 24))
   
3. Extended Euclidean Algorithm

        def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x1, y1 = egcd(b % a, a)
        return g, y1 - (b // a) * x1, x1

        def modinv(a, n):
            g, x, _ = egcd(a, n)
            if g != 1:
                return None
            return x % n

        print("Invers 3 mod 11 =", modinv(3, 11))  # hasil: 4

4. Logaritma Diskrit (Discrete Log)

        def discrete_log(a, b, n):
            for x in range(n):
                if pow(a, x, n) == b:
                    return x
            return None

        print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))  # hasil: 4

---


## 6. Hasil dan Pembahasan
Dari keempat potongan kode yang telah dibuat — meliputi operasi aritmetika modular, GCD (Greatest Common Divisor), invers modular, serta logaritma diskrit — dapat dipahami bahwa seluruhnya saling berhubungan dan menjadi fondasi utama dalam sistem kriptografi modern. Kode pertama menggambarkan bagaimana operasi dasar seperti penjumlahan, pengurangan, perkalian, dan perpangkatan dapat dilakukan secara efisien di dalam sistem modular. Prinsip ini menjadi dasar bagi proses enkripsi dan dekripsi pada algoritma seperti RSA.

Kode kedua dan ketiga, yaitu perhitungan GCD dan pencarian invers modular, memiliki peran penting dalam memastikan keterkaitan antarbilangan. Fungsi GCD digunakan untuk menentukan apakah dua bilangan bersifat saling prima, sedangkan invers modular memungkinkan proses kebalikan antara enkripsi dan dekripsi dalam sistem kunci publik. Tanpa adanya invers modular, pesan terenkripsi tidak dapat dikembalikan ke bentuk aslinya.

Sementara itu, kode keempat yang berkaitan dengan logaritma diskrit menunjukkan tingkat kesulitan dalam menemukan nilai eksponen 𝑥 pada persamaan 𝑎𝑥≡𝑏(mod𝑛). Kompleksitas perhitungan inilah yang menjadi dasar keamanan algoritma seperti Diffie–Hellman. Secara keseluruhan, keempat kode tersebut menegaskan bahwa konsep-konsep matematika seperti aritmetika modular, GCD, invers modular, dan logaritma diskrit memiliki keterkaitan erat dan berperan besar dalam menjaga keamanan informasi pada sistem kriptografi masa kini.

Hasil eksekusi program modular math:

![Hasil Eksekusi](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan

- Pertanyaan 1:
  Aritmetika modular menjadi dasar kriptografi modern karena memungkinkan operasi matematika seperti penjumlahan, perkalian, dan perpangkatan dilakukan dalam ruang bilangan terbatas. Sistem seperti RSA dan Diffie–Hellman    menggunakan operasi modular agar proses enkripsi dan dekripsi efisien serta aman, meskipun melibatkan bilangan yang sangat besar.
- Pertanyaan 2:
  Invers modular digunakan untuk menemukan kunci privat (𝑑) dari kunci publik (𝑒) pada RSA, dengan syarat 𝑒⋅𝑑≡1(mod𝜑(𝑛)). Tanpa invers modular, pesan terenkripsi tidak dapat dikembalikan ke bentuk aslinya, sehingga proses   dekripsi tidak mungkin dilakukan.
- Pertanyaan 3:
  Masalah logaritma diskrit sulit diselesaikan karena tidak ada algoritma cepat untuk mencari 𝑥 dari 𝑔𝑥≡ℎ(mod𝑝).jika 𝑝p sangat besar. Kompleksitasnya meningkat eksponensial, sehingga menjadi dasar keamanan algoritma         seperti Diffie–Hellman dan ElGamal.

---

## 8. Kesimpulan
Berdasarkan hasil percobaan yang telah dilakukan, dapat disimpulkan bahwa aritmetika modular, GCD, invers modular, dan logaritma diskrit memiliki keterkaitan yang sangat erat dalam membangun dasar sistem kriptografi modern. Melalui percobaan ini, terlihat bahwa aritmetika modular mampu menjaga hasil operasi matematika tetap efisien dan berada dalam batas tertentu, sehingga cocok digunakan pada proses enkripsi dan dekripsi data. GCD berperan penting dalam menentukan apakah dua bilangan memiliki hubungan saling prima, yang menjadi dasar pembentukan kunci pada algoritma kriptografi.

Selain itu, invers modular terbukti sangat penting karena berfungsi untuk mengembalikan pesan yang telah dienkripsi agar dapat dibaca kembali dalam bentuk aslinya. Sedangkan logaritma diskrit menunjukkan tingkat kesulitan yang tinggi untuk dipecahkan, terutama jika modulusnya besar — hal ini justru menjadi kekuatan utama dalam menjaga keamanan sistem seperti RSA dan Diffie–Hellman. Secara keseluruhan, percobaan ini menunjukkan bagaimana konsep matematika sederhana dapat diimplementasikan menjadi pondasi utama dalam menjaga keamanan data digital di era modern.

---

## 9. Daftar Pustaka
  
- Putrodjojo, G., Purba, J. H., & Candra, J. (2017). *Aplikasi Algoritma Des (Data Encryption Standard) Untuk Pengaman Data. Creative Communication and Innovative Technology Journal*, 10(1), 62-74..  
- Zeng, Z. (2021). *The numerical greatest common divisor of univariate polynomials. arXiv preprint arXiv:2103.04196.*  
  

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit 23c9150a3ab3aecf36aa72101a9cda941f298292
Author: zaky321 <sofyan.muzaqi@gmail.com>
Date:   Mon Oct 27 21:36:51 2025 +0700

    week3-modmath-gdc: implementasi modular arithmetic & GCD dan laporan )
```
