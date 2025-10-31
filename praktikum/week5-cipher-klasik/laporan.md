# Laporan Praktikum Kriptografi
Minggu ke-: 5  
Topik: [Cipher Klasik (Caesar, Vigenère, Transposisi)]  
Nama: [Sofyan Muzaki]  
NIM: [230202820]  
Kelas: [5IKRA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menerapkan algoritma **Caesar Cipher** untuk enkripsi dan dekripsi teks.  
2. Menerapkan algoritma **Vigenère Cipher** dengan variasi kunci.  
3. Mengimplementasikan algoritma transposisi sederhana.  
4. Menjelaskan kelemahan algoritma kriptografi klasik.  
---

## 2. Dasar Teori

Kriptografi klasik berperan sebagai fondasi utama dalam perkembangan keamanan informasi modern. Prinsip dasarnya adalah mengubah teks asli (plaintext) menjadi bentuk terenkripsi (ciphertext) agar isi pesan tidak mudah dipahami oleh pihak yang tidak berhak. Salah satu bentuk paling sederhana adalah Cipher Caesar, yang diperkenalkan oleh Julius Caesar. Teknik ini bekerja dengan cara menggeser setiap huruf sejumlah langkah tertentu dalam alfabet—misalnya, pergeseran tiga huruf akan mengubah A menjadi D, B menjadi E, dan seterusnya. Meskipun sederhana dan cepat diterapkan, cipher ini mudah dipecahkan melalui analisis frekuensi karena jumlah kemungkinan kuncinya terbatas.

Berbeda dengan Caesar, Cipher Vigenère menggunakan pendekatan yang lebih kompleks melalui kunci berupa kata atau frasa. Setiap huruf pada plaintext dienkripsi menggunakan huruf yang berbeda sesuai dengan posisi huruf kunci, menjadikannya bagian dari polyalphabetic cipher. Misalnya, dengan kunci “DATA”, huruf pertama dienkripsi dengan ‘D’, huruf kedua dengan ‘A’, dan seterusnya. Pendekatan ini menghasilkan pola yang lebih acak dan sulit ditebak. Namun, dengan teknik analisis seperti Kasiski examination, cipher ini tetap dapat dipecahkan jika teksnya cukup panjang.

Sementara itu, Cipher Transposisi tidak mengganti huruf dengan simbol lain, melainkan mengubah urutannya sesuai pola tertentu. Misalnya, huruf-huruf dalam pesan disusun ulang dalam bentuk kolom atau pola zig-zag sebelum dibaca kembali dalam urutan berbeda. Hasilnya adalah ciphertext yang berisi huruf sama seperti plaintext, tetapi dalam susunan yang membingungkan. Meski relatif sederhana, metode transposisi ini menjadi dasar bagi banyak algoritma enkripsi berikutnya, terutama ketika dikombinasikan dengan teknik substitusi untuk menciptakan tingkat keamanan yang lebih tinggi.

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
### Langkah 1 — Implementasi Caesar Cipher
```python
def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

# Contoh uji
msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```

---

### Langkah 2 — Implementasi Vigenère Cipher
```python
def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

# Contoh uji
msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```

---

### Langkah 3 — Implementasi Transposisi Sederhana
```python
def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# Contoh uji
msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```


---

## 6. Hasil dan Pembahasan

Hasil eksekusi program Cipher Klasik:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan

- Pertanyaan 1:Caesar Cipher lemah karena hanya memiliki 25 kemungkinan kunci dan mudah dipecahkan dengan brute force atau analisis frekuensi. Vigenère Cipher memang lebih kuat, tapi tetap rentan jika kunci terlalu pendek                karena pola huruf berulang bisa dianalisis dengan metode Kasiski atau Friedman.
- Pertanyaan 2:Cipher klasik tetap mempertahankan pola statistik bahasa asli. Huruf yang sering muncul di plaintext juga sering muncul di ciphertext, sehingga analisis frekuensi dapat digunakan untuk menebak kunci dan                    huruf yang disubstitusi.
- Pertanyaan 3:Substitusi mengganti huruf, sedangkan transposisi hanya menukar urutannya. Substitusi mudah dipecahkan dengan analisis huruf, sedangkan transposisi lebih sulit tetapi masih bisa ditebak jika polanya                        sederhana. Kombinasi keduanya memberi keamanan lebih kuat.

---

## 8. Kesimpulan

Dari percobaan terhadap Cipher Klasik (Caesar, Vigenère, dan Transposisi), dapat disimpulkan bahwa setiap metode memiliki pola enkripsi berbeda namun tetap bergantung pada kunci dan struktur bahasa. Cipher Caesar paling sederhana namun mudah dipecahkan, sedangkan Vigenère dan Transposisi menawarkan keamanan lebih tinggi bila digunakan dengan kunci yang cukup panjang dan pola acak. Secara keseluruhan, cipher klasik efektif untuk pembelajaran konsep dasar kriptografi, tetapi kurang aman untuk penerapan modern.

---

## 9. Daftar Pustaka

- Irawan, M. D. (2017). *Implementasi kriptografi Vigenere cipher dengan php*. Jurnal Teknologi Informasi, 1(1), 11-21.
- Chafid, N., & Soffiana, H. (2022). *Impelementasi Algoritma Kriptografi Klasik Caesar Untuk Rancang Bangun Aplikasi E-Voting Berbasis Web (Studi Kasus: Sman 10 Tangerang)*. Jurnal Ilmiah Sains dan Teknologi, 6(2), 133-145.
---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

   week5-cipher-klasik
```
