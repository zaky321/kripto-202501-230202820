# Laporan Praktikum Kriptografi
Minggu ke-: 1

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

def enkripsi_caesar(text, shift):
    hasil = ""
    for char in text:
        if char.isalpha(): 
            base = ord('A') if char.isupper() else ord('a')
            hasil += chr((ord(char) - base + shift) % 26 + base)
        else:
            hasil += char 
    return hasil

def dekripsi_caesar(text, shift):
    return enkripsi_caesar(text, -shift)

if __name__ == "__main__":
    print("=== Program Caesar Cipher ===")
    pesan = input("Masukkan teks: ")
    kunci = int(input("Masukkan nilai pergeseran (shift): "))

    terenkripsi = enkripsi_caesar(pesan, kunci)
    print(f"\nHasil Enkripsi : {terenkripsi}")

    terdekripsi = dekripsi_caesar(terenkripsi, kunci)
    print(f"Hasil Dekripsi : {terdekripsi}")


## 6. Hasil dan Pembahasan

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)


---

## 7. Jawaban Pertanyaan 
- Pertanyaan 1: Claude E. Shannon
- Pertanyaan 2:RSA (Rivest–Shamir–Adleman) → digunakan untuk enkripsi data dan tanda tangan digital.
              >>Diffie–Hellman → digunakan untuk pertukaran kunci secara aman di jaringan publik.
                >>Elliptic Curve Cryptography (ECC) → menawarkan keamanan tinggi dengan ukuran kunci yang lebih kecil, banyak digunakan pada perangkat mobile dan IoT.
                    >>DSA (Digital Signature Algorithm) → digunakan khusus untuk tanda tangan digital.
- Pertanyaan 3:Kriptografi klasik merupakan sistem penyandian yang umumnya menggunakan metode sederhana seperti penggantian huruf (substitution) atau penyusunan ulang huruf (transposition), contohnya pada Caesar Cipher dan Vigenère Cipher. Sistem ini menggunakan satu kunci yang sama untuk proses enkripsi dan dekripsi, sehingga termasuk dalam kategori symmetric key cryptography.
Berbeda dengan itu, kriptografi modern menggunakan pendekatan matematis dan teori bilangan yang jauh lebih kompleks. Sistem ini mampu mengolah berbagai jenis data digital, seperti teks, gambar, suara, dan file, serta memungkinkan penggunaan dua kunci berbeda — yaitu kunci publik dan kunci privat — seperti pada algoritma RSA dan ECC. Dari sisi keamanan, kriptografi modern jauh lebih kuat karena sulit dipecahkan tanpa kunci yang valid, bahkan oleh komputer dengan kemampuan tinggi sekalipun.
---

## 8. Kesimpulan
Kesimpulan Percobaan Teknik Caesar Cipher – Kriptografi Klasik: Dari percobaan menggunakan teknik Caesar Cipher, dapat disimpulkan bahwa metode ini merupakan bentuk kriptografi klasik yang sangat sederhana. Proses enkripsi dilakukan dengan menggeser huruf dalam teks asli sejumlah nilai tertentu, sedangkan dekripsi dilakukan dengan menggeser huruf ke arah sebaliknya.

Meskipun mudah dipahami dan diterapkan, Caesar Cipher memiliki tingkat keamanan yang rendah, karena pola pergeserannya mudah ditebak dan dapat dipecahkan dengan percobaan sederhana (brute force). Namun demikian, percobaan ini memberikan pemahaman dasar tentang prinsip kerja enkripsi dan dekripsi, yang menjadi fondasi bagi pengembangan kriptografi modern yang lebih kompleks dan aman.

## 9. Daftar Pustaka   
- Munir, R. (2006). Pengantar Kriptografi. ITB, Bandung. 
- DELPHI, B., & FAIRUZABADI, M. IMPLEMENTASI KRIPTOGRAFI KLASIK MENGGUNAKAN.
- Nanda, N. A., Sari, M., & Gunawan, I. (2023). Kriptografi dan Penerapannya Dalam Sistem Keamanan Data. Jurnal Media Informatika, 4(2), 90-93.

---

## 10. Commit Log
```
commit abc12345
Author: Sofyan muzaki <sofyan.muzaqi@gmail.com>
Date:   2025-10-06

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
