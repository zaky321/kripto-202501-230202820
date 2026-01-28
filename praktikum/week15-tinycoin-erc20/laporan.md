# Laporan Praktikum Kriptografi
Minggu ke-: 15  
Topik: [Proyek Kelompok – TinyCoin ERC20]  
Nama: [Sofyan Muzaki]  
NIM: [230202820]  
Kelas: [5IKRA]  

---

## 1. Tujuan

- Mengembangkan proyek sederhana berbasis algoritma kriptografi.
- Mendokumentasikan proses implementasi proyek ke dalam repository Git.
- Menyusun laporan teknis hasil proyek akhir.

---

## 2. Dasar Teori
TinyCoin ERC-20 adalah proyek kelompok yang bertujuan untuk merancang dan mengimplementasikan sebuah token kripto sederhana berbasis standar ERC-20 pada jaringan blockchain Ethereum. Proyek ini berfokus pada pemahaman konsep dasar smart contract, mulai dari struktur kontrak, fungsi utama seperti transfer, approve, dan transferFrom, hingga mekanisme pencatatan saldo dan total suplai token. Dengan menggunakan bahasa pemrograman Solidity serta tools pendukung seperti Remix atau Hardhat, TinyCoin dikembangkan sebagai simulasi token digital yang dapat dipertukarkan antar pengguna secara terdesentralisasi tanpa perantara.
Namun, ada asumsi implisit yang perlu diuji: proyek ERC-20 sering dianggap “mudah” karena mengikuti standar. Padahal, standar hanya mendefinisikan interface, bukan menjamin keamanan implementasi. Seorang skeptis akan menyoroti potensi celah seperti kesalahan pengelolaan allowance, kurangnya mekanisme access control pada fungsi tertentu, atau absennya fitur mitigasi risiko seperti pause dan mint/burn control. Oleh karena itu, TinyCoin tidak hanya menjadi latihan teknis membuat token, tetapi juga sarana untuk memahami pentingnya desain kontrak yang aman, pengujian menyeluruh, dan kesadaran terhadap risiko keamanan dalam ekosistem blockchain.
Dari perspektif alternatif, TinyCoin bisa dipandang bukan sekadar token digital, melainkan studi kasus tentang bagaimana standar industri memengaruhi interoperabilitas dan adopsi teknologi. Dengan mematuhi ERC-20, token ini dapat dengan mudah diintegrasikan ke dompet kripto dan aplikasi terdesentralisasi (dApps). Dengan demikian, proyek ini memberikan pengalaman praktis tentang bagaimana teori blockchain diterjemahkan ke implementasi nyata, sekaligus menanamkan pola pikir kritis bahwa keberhasilan sebuah token tidak hanya ditentukan oleh fungsionalitas, tetapi juga oleh keamanan, transparansi, dan konteks penggunaannya.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub    )

---

## 4. Langkah Percobaan


---

## 5. Source Code


---

## 6. Hasil dan Pembahasan


---

## 7. Jawaban Pertanyaan
- ERC-20 merupakan standar token yang berfungsi sebagai fondasi utama dalam ekosistem blockchain Ethereum karena menyediakan aturan baku dalam pembuatan dan pengelolaan token digital. Dengan adanya standar ini, setiap token ERC-20 dapat dengan mudah digunakan dan dikenali oleh berbagai wallet, exchange, serta aplikasi terdesentralisasi (dApp) tanpa perlu penyesuaian khusus. Hal ini menjadikan ERC-20 sangat penting dalam mendukung interoperabilitas antar aplikasi blockchain dan mendorong pertumbuhan ekonomi Web3, seperti penggunaan token untuk pembayaran, governance, reward, hingga stablecoin.

- Mekanisme transfer token pada kontrak ERC-20 bekerja melalui perubahan data (state) pada smart contract, bukan dengan memindahkan koin secara fisik seperti ETH. Ketika fungsi transfer dipanggil, kontrak akan memeriksa saldo pengirim, menguranginya sesuai jumlah token yang dikirim, lalu menambahkan saldo penerima dan mencatat peristiwa tersebut dalam event Transfer. Selain itu, ERC-20 juga menyediakan mekanisme approve dan transferFrom yang memungkinkan pihak ketiga, seperti decentralized exchange, untuk melakukan transfer token atas izin pemilik saldo. Seluruh proses ini berlangsung secara transparan, tercatat permanen di blockchain, dan tidak dapat diubah.

- Dalam implementasinya, smart contract ERC-20 memiliki beberapa risiko utama, seperti kesalahan logika program, celah keamanan reentrancy, overflow atau underflow nilai, serta lemahnya kontrol akses terhadap fungsi penting. Risiko-risiko ini dapat menyebabkan kehilangan aset atau penyalahgunaan kontrak. Oleh karena itu, mitigasi sangat diperlukan, antara lain dengan melakukan pengujian menyeluruh, audit keamanan, penggunaan library tepercaya seperti OpenZeppelin, penerapan pola pemrograman yang aman, serta perencanaan mekanisme upgrade kontrak sebelum dideploy ke jaringan utama. Dengan langkah-langkah tersebut, keamanan dan keandalan smart contract dapat ditingkatkan secara signifikan.

---

## 8. Kesimpulan
Proyek kelompok TinyCoin ERC-20 menunjukkan bahwa pembuatan token kripto berbasis standar ERC-20 tidak hanya berfungsi sebagai latihan teknis pemrograman smart contract, tetapi juga sebagai sarana memahami prinsip dasar blockchain Ethereum secara menyeluruh. Melalui implementasi fungsi-fungsi inti ERC-20, proyek ini membuktikan bahwa standar tersebut memudahkan interoperabilitas dan integrasi token dengan ekosistem Ethereum.

Namun, anggapan bahwa mengikuti standar ERC-20 sudah cukup untuk menjamin kualitas dan keamanan token merupakan asumsi yang lemah. Standar hanya mengatur antarmuka, bukan ketepatan logika maupun keamanan implementasi. Oleh karena itu, TinyCoin menegaskan pentingnya pengujian, audit kode, dan kesadaran terhadap potensi celah keamanan dalam smart contract. Dengan demikian, proyek ini tidak hanya menghasilkan sebuah token sederhana, tetapi juga membangun pemahaman kritis bahwa keberhasilan sebuah proyek blockchain ditentukan oleh kombinasi antara kepatuhan standar, desain yang aman, dan tujuan penggunaan yang jelas.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Buterin, V. *Ethereum: A Next-Generation Smart Contract and Decentralized Application Platform.*.  
- Szabo, N. *Formalizing and Securing Relationships on Public Networks.*.  )

---

## 10. Commit Log

```
commit 90779d34d9214f8ba53df516bc4ec630568b785b
Author: zaky321 <141202616+zaky321@users.noreply.github.com>
Date:   Wed Jan 28 23:26:20 2026 +0700

    week15-tinycoin-erc20: implementasi TinyCoin.sol dan laporan )
```
