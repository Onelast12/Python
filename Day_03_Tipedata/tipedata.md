# Day 3 -> integer, float, bool, dan string
# list, tuple, dictionary, dan set akan dibahas di day berikutnya

## Tipe Data
**Tipe data Python adalah jenis nilai yang dapat disimpan dalam variabel**

**Tipe Data**
- int : integer bilangan bulat
  x = 5, -3, 0
- float : bilangan decimal(.)
  x = 2.4, -4.1 0. atau 2.
- str : String adalah kumpulan karakter yg diapit tanda kutip tunggal ('--') atau kutip ganda("--")
  nama = "Roronoa zoro"
- bool : boolean menyimpan nilai logika True/False
  yz = True

- list : koleksi elemen yg terurut dan dapat diubah, bisa berisi tipe data berbeda.
  nama = [1, 2, 4]
- tuple : koleksi elemen yg terurut tetapi tidak bisa berubah(immutable).
  nama = (10, 20)
- dict : dictionary koleksi pasangan kunci-nilai (key-value), tidak terurut.
  data = {nama : Budi, umur : 21}
- set : koleksi elemen unik yg tidak terurut dan tanpa duplikat. 
  angka = {1, 2}
- NoneType: Nilai kosong atau tanpa nilai, diwakili oleh None.
  data = None
- kompleks, dengan bagian riil dan imajiner.
  Contoh: z = 3 + 4j

### Casting integer ke float, boolean dan string
Mengapa tipe data penting:
1. Pengelolaan Memori: Tipe data menentukan bagaimana nilai variabel disimpan dalam memori.
2. Operasi yang Tersedia: Jenis operasi yang dapat dilakukan pada variabel tergantung pada tipe datanya. Misalnya, operasi aritmatika dapat dilakukan pada angka, tetapi tidak pada string.
3. Validasi dan Konversi: Python memungkinkan kamu untuk memeriksa tipe data menggunakan fungsi type() dan mengubah tipe data menggunakan fungsi seperti int(), str(), atau float().