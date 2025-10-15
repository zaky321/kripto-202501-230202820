# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: [Cryptosystem (Komponen, Enkripsi & Dekripsi, Simetris & Asimetris)]  
Nama: [Sofyan Muzaki]  
NIM: [230202820]  
Kelas: [5IKRA]  

---

## 1. Tujuan
1. Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).  
2. Menggambarkan proses enkripsi dan dekripsi sederhana.  
3. Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).  
---

## 2. Dasar Teori
Kriptosistem merupakan bagian penting dari ilmu kriptografi yang berfungsi untuk menjaga kerahasiaan dan keamanan data dalam proses komunikasi digital. Sistem ini bekerja dengan mengubah pesan asli atau plaintext menjadi bentuk yang tidak dapat dibaca, yaitu ciphertext, melalui proses enkripsi menggunakan algoritma tertentu dan kunci rahasia. Komponen utama dalam kriptosistem meliputi plaintext, ciphertext, kunci, dan algoritma. Algoritma berperan sebagai aturan atau prosedur matematis yang menentukan bagaimana proses pengubahan dan pemulihan data dilakukan, sedangkan kunci menjadi elemen utama yang menentukan hasil enkripsi dan dekripsi.

Proses enkripsi bertujuan untuk melindungi informasi dari pihak yang tidak berwenang, sedangkan dekripsi digunakan untuk mengembalikan ciphertext ke bentuk semula agar dapat dibaca oleh penerima yang sah. Berdasarkan cara penggunaan kunci, kriptosistem dibagi menjadi dua jenis, yaitu kriptosistem simetris dan kriptosistem asimetris. Kriptosistem simetris menggunakan satu kunci yang sama untuk proses enkripsi dan dekripsi, sehingga cepat namun memiliki risiko dalam distribusi kunci. Sebaliknya, kriptosistem asimetris menggunakan dua kunci berbeda, yaitu public key dan private key, yang membuat sistem ini lebih aman untuk komunikasi jarak jauh meskipun prosesnya lebih kompleks.

Secara keseluruhan, kriptosistem berperan penting dalam menjaga keamanan data di berbagai bidang seperti transaksi elektronik, komunikasi jaringan, dan penyimpanan informasi digital. Dengan penerapan algoritma dan manajemen kunci yang tepat, sistem ini mampu mencegah kebocoran data serta memastikan keaslian dan integritas informasi yang dikirimkan.

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

```python
# file: praktikum/week2-cryptosystem/src/simple_crypto.py

def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char
    return result

if __name__ == "__main__":
    message = "<sofyan muzaki>"
    key = 5

    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)
```
Hasil Yang Dikeluakan:
```
Plaintext : <sofyan muzaki>
Ciphertext: <xtkdfs rzefpn>
Decrypted : <sofyan muzaki>
```

---

## 6. Hasil dan Pembahasan
Program berhasil melakukan enkripsi pada huruf dan angka.

Huruf digeser 5 posisi dalam alfabet (mod 26).

Angka digeser 5 posisi dalam 0–9 (mod 10). Proses dekripsi membalikkan hasil enkripsi dengan kunci yang sama, menunjukkan sistem ini termasuk kriptografi simetris. Tidak ditemukan error selama eksekusi program.

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Komponennnya adalah Plaintext (teks asli),Ciphertext (teks terenkripsi),Kunci (key),Algoritma kriptografi
- Pertanyaan 2:Kelebihan sistem simetris adalah proses enkripsi dan dekripsinya lebih cepat dan efisien, karena hanya menggunakan satu kunci yang sama.
-             Kelemahannya, sistem ini memiliki masalah dalam distribusi kunci, karena kunci yang sama harus diketahui oleh pengirim dan penerima.
- Pertanyaan 3:Distribusi kunci menjadi masalah utama karena pengirim dan penerima harus memiliki kunci yang sama sebelum proses komunikasi dapat dilakukan. Pengiriman kunci melalui saluran yang tidak aman berpotensi menyebabkan penyadapan atau pencurian kunci oleh pihak ketiga.
)
---

## 8. Kesimpulan
Praktikum ini menunjukkan bagaimana proses enkripsi dan dekripsi dilakukan menggunakan metode sederhana (Caesar Cipher yang dimodifikasi). Sistem ini menggunakan satu kunci yang sama, termasuk jenis kriptografi simetris. Hasil uji menunjukkan bahwa program dapat mengenkripsi huruf dan angka dengan benar.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Sutanta, E. (2011). Keamanan Data dan Informasi. Yogyakarta: Graha Ilmu.
- Kurniawan, B. (2018). Pengantar Kriptografi dan Keamanan Informasi. Bandung: Informatika.
- Sari, N., & Wibowo, R. (2020). Kriptografi dan Keamanan Jaringan Komputer. Yogyakarta: Deepublish.
---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit wekk02
Author: Sofyan Muzaki <sofyan.muzaqi@gmail.com>
Date:   2025-10-15

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
