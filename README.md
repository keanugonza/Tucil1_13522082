#  Tugas Kecil 1 IF2211 Strategi Algoritma  

>  Tucil 1  Semester II tahun 2023/2024 -- Penyelesaian Cyberpunk 2077 Breach Protocol dengan Algoritma Brute Force


## Table of Contents
* [How to Use](#how-to-use)
* [General Info](#general-information)
* [Aturan Permainan](#aturan-permainan)
* [Features](#features)
* [Structure](#structure)
* [Contact](#contact)

## How to use
Pada Command Prompt:
 - Masuk ke folder src (cd src)
 - python main.py

## General Information
- Di dalam Tugas Kecil 1 ini, mencari solusi dari permainan Breach Protocol pada Cyberpunk 2077 menggunakan algoritma Brute Force.
- Cyberpunk 2077 Breach Protocol adalah minigame meretas pada permainan video Cyberpunk 2077.
 Minigame ini merupakan simulasi peretasan jaringan local dari ICE (Intrusion Countermeasures
 Electronics) pada permainan Cyberpunk 2077. Komponen pada permainan ini antara lain adalah:
   1. Token (terdiri dari dua karakter alfanumerik seperti E9, BD, dan 55.)
   2. Matriks (terdiri atas token-token yang akan dipilih untuk menyusun urutan kode.)
   3. Sekuens (sebuah rangkaian token (dua atau lebih) yang harus dicocokkan.)
   4. Buffer (jumlah maksimal token yang dapat disusun secara sekuensial.)


## Aturan Permainan
 1. Pemain bergerak dengan pola horizontal, vertikal, horizontal, vertikal (bergantian) hingga semua sekuens berhasil dicocokkan atau buffer penuh.
 2. Pemainmemulai dengan memilih satu token pada posisi baris paling atas dari matriks.
 3. Sekuens dicocokkan pada token-token yang berada di buffer.
 4. Satutoken pada buffer dapat digunakan pada lebih dari satu sekuens.
 5. Setiap sekuens memiliki bobot hadiah atau reward yang variatif.
 6. Sekuens memiliki panjang minimal berupa dua token.

## Features
Menemukan solusi dari permainan Breach Protocol yang paling optimal untuk
 setiap kombinasi matriks, sekuens,dan ukuran buffer dengan menggunakan algoritma brute force.
<table>
    <tr>
      <td><b>Poin</b></td>
      <td><b>Progress</b></td>
    </tr>
    <tr>
      <td>1. Program berhasil dikompilasi tanpa kesalahan</td>
      <td>Ya</td>
    </tr>
    <tr>
      <td> 2. Program berhasil dijalankan</td>
      <td>Ya</td>
    </tr>
    <tr>
      <td>3. Program dapat membacamasukan berkas .txt</td>
      <td>Ya</td>
    </tr>
    <tr>
      <td> 4. Program dapat menghasilkan masukan secara acak</td>
      <td>Ya</td>
    </tr>
    <tr>
      <td> 5. Solusi yang diberikan program optimal</td>
      <td>Ya</td>
    </tr>
    <tr>
      <td> 6. Program dapat menyimpan solusi dalam berkas .txt</td>
      <td>Ya</td>
    </tr>
    <tr>
      <td> 7. Program memiliki GUI</td>
      <td>Tidak</td>
    </tr>
</table>

## Structure
Tucil1_13522082 
 │ <br>
 ├── bin    <br>
 ├── doc    <br>
 │    └── Tucil1_K2_13522082_Keanu Amadius Gonza Wrahatno.pdf <br>
 ├── src    <br>
 │    ├── bruteforce.py <br>
 │    ├── main.py   <br>
 │    ├── readFile.py  <br>
 ├── test   <br>
 │    ├── solusi.txt <br>
 │    ├── test.txt <br>
 └── README.md  <br>


## Contact
Keanu Amadius Gonza Wrahatno	<br>
- (13522082@std.stei.itb.ac.id) <br>
- (13522082@mahasiswa.itb.ac.id) <br>