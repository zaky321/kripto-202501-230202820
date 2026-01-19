# Laporan Praktikum Kriptografi
Minggu ke-: 13  
Topik: [TinyChain – Proof of Work (PoW)]  
Nama: [Sofyan Muzaki]  
NIM: [Sofyan Muzaki]  
Kelas: [5IKRA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menjelaskan peran **hash function** dalam blockchain.  
2. Melakukan simulasi sederhana **Proof of Work (PoW)**.  
3. Menganalisis keamanan cryptocurrency berbasis kriptografi.  


---

## 2. Dasar Teori
TinyChain merupakan implementasi blockchain berskala kecil yang sering digunakan sebagai media pembelajaran untuk memahami konsep dasar teknologi blockchain. Salah satu mekanisme inti yang diterapkan pada TinyChain adalah Proof of Work (PoW), yaitu metode konsensus yang mengharuskan node (penambang) memecahkan persoalan kriptografi tertentu sebelum sebuah blok baru dapat ditambahkan ke dalam rantai. Tujuan utama PoW dalam TinyChain bukanlah efisiensi tinggi, melainkan memberikan gambaran nyata bagaimana proses validasi blok dan pembentukan konsensus terjadi secara terdesentralisasi.

Dalam skema PoW, setiap node berlomba mencari nilai nonce yang menghasilkan hash dengan kriteria tertentu (misalnya diawali sejumlah nol). Proses ini membutuhkan komputasi dan waktu, sehingga membuat manipulasi data menjadi mahal dan sulit. Pada TinyChain, tingkat kesulitan PoW biasanya disederhanakan agar proses penambangan dapat dijalankan pada komputer biasa, namun prinsip dasarnya tetap sama seperti pada blockchain besar: blok hanya dianggap sah jika memenuhi syarat PoW dan diverifikasi oleh node lain.

Dari sisi keamanan, PoW pada TinyChain menunjukkan bagaimana mekanisme ini mampu menjaga integritas data dan mencegah perubahan blok secara sepihak. Namun, TinyChain juga memperlihatkan keterbatasan PoW, seperti konsumsi sumber daya dan skalabilitas yang rendah jika diterapkan pada skala besar. Dengan demikian, TinyChain berbasis PoW berfungsi sebagai model konseptual yang efektif untuk memahami kekuatan dan kelemahan Proof of Work sebelum mempelajari blockchain yang lebih kompleks.

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
### Langkah 1 — Membuat Struktur Blok
```python
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")
```

---

### Langkah 2 — Membuat Blockchain
```python
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

# Uji coba blockchain
my_chain = Blockchain()
print("Mining block 1...")
my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))

print("Mining block 2...")
my_chain.add_block(Block(2, "", "Transaksi B → C: 5 Coin"))
```

---

### Langkah 3 — Analisis Proof of Work
- Perhatikan bahwa proses mining membutuhkan waktu (bergantung pada `difficulty`).  
- Analisis: semakin tinggi difficulty, semakin lama proses mining.  
- Diskusikan bagaimana hal ini menjamin keamanan blockchain.  

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

- Pertanyaan 1: Hash menjaga integritas data: perubahan sedikit saja pada transaksi/blok akan mengubah hash drastis. Hash juga mengikat blok lewat hash blok sebelumnya, sehingga riwayat sulit dimanipulasi. (Hash bukan                     enkripsi, tujuannya verifikasi keutuhan.)
- Pertanyaan 2:PoW membuat jaringan memilih satu riwayat transaksi (rantai terpanjang/terberat). Untuk membayar dua kali, penyerang harus mengulang PoW dan mengejar/menyalip rantai utama, yang butuh komputasi sangat besar—              kecuali jika punya mayoritas daya hash (risiko 51%).
- Pertanyaan 3:PoW boros energi karena banyak penambang menghitung nonstop, tetapi hanya satu yang menang tiap blok; kerja yang lain terbuang. Keamanan dibayar dengan konsumsi listrik tinggi dan skalabilitas kurang baik.

---

## 8. Kesimpulan
Dari percobaan TinyChain, kelihatan kalau hash itu jadi “penjaga” rantai: begitu data diubah sedikit, hash berubah besar dan rantainya langsung ketahuan tidak valid. PoW bikin nambah blok harus kerja komputasi dulu, jadi ngakal-ngakalin transaksi (double spending) jadi susah. Tapi konsekuensinya, makin tinggi difficulty, proses mining makin lama dan makin boros resource/energi.

---

## 9. Daftar Pustaka
- Hasan, S. A., Al-Zahra, W. N., Auralia, A. S., Maharani, D. A., & Hidayatullah, R. (2024). Implementasi teknologi blockchain dalam pengamanan sistem keuangan pada perguruan tinggi: Implementation of blockchain technology in securing financial systems in higher education. Jurnal MENTARI: Manajemen, Pendidikan dan Teknologi Informasi, 3(1), 11-18.
- Wikarsa, L., Suwanto, T., & Lengkey, C. (2022). Implementasi Algoritma Konsensus Proof-of-Work dalam Blockchain terhadap Rekam Medis. Jurnal Pekommas, 7(1), 41-52.
- Wijaya, I., Haryatmi, E., & Kurniawan, A. B. (2020). Implementasi Teknologi Blockchain pada Sistem Presensi Staff VM LePKom Berbasis Web. Jurnal Nasional Informatika Dan Teknologi Jaringan, 5(1), 162-169.

---

## 10. Commit Log

```
commit f1371eecaff102be954b7d1af5de27365a4d9791
Author: Sofayn muzaki <Sofyan.muzaqi@gmail.com>
Date:   Wed Jan 14 23:07:59 2026 +0700

   week13-tinychain
```
