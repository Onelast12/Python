## Day 7 Input dan Konversi Tipedata

# input() digunakan untuk mengambil input dari pengguna melalui keayboard.
# 1. Nilai yg dimasukan pengguna akan selalu dianggap sebagai string.
*Example*
```
nama = input("Masukan nama anda: ")
print("Hallo", nama)
```
 1. Program meminta pengguna memasukkan nama.
 2. input() menerima input dari pengguna dalam bentuk string.
 3. Nilai input kemudian ditampilkan menggunakan print().

# 2. Konversi Tipe Data (Type Casting)
* input() akan selalu dianggap string. namun bisa dicasting menjadi int(),float(),boolean()

 *Cara 1*
```
nomor = input("Masukan angka: ")
print(type(nama)) # <class 'str'>
nomor = int(nomor) # ini dicasting ke integer
print(type(nama)) # <class 'int'>
```
```
 *Cara 2*
nomor = int(input("Masukan nama: "))
print(type(nomor)) # <class 'int'>
print(nomor) 
```
# 3. Mengambil Beberapa Input
 * Kita bisa mengambil beberapa input sekaligus menggunakan metode split().
```
x, y = input("Enter two numbers separated by space: ").split()
print("First number:", x)
print("Second number:", y)
```
* Note: Menggunakan metode string.split() akan dibahas dihari berikutnya.

