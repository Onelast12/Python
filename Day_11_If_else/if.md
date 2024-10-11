## Day 11

# 1. if di gunakan untuk mengambil keputusan
```
if kondisi:
    # blok kode jika kondisi True
```
# 2. else dieksekusi jika kondisi dalam if tidak terpenuhi.
```
if kondisi:
    # blok kode jika kondisi True
else:
    # blok kode jika kondisi False
```
# 3. indentasi (spasi atau tab) untuk mengelompokkan kode yang tergabung dalam blok yang sama.**
 - Indetasi untuk menandai awal dan akhir blok kode.
 - Jika tidak menggunakan indentasi dengan benar, Python akan mengeluarkan error IndentationError.
 - Note: Biasanya indentasi menggunakan 4 spasi atau 1 tab.


```Contoh indentasi dengan benar
umur = 16
if umur >= 18:
    print("Anda sudah dewasa.")  # Baris ini diindentasi
    print("Selamat datang.")     # Baris ini juga diindentasi
else:
    print("Anda masih di bawah umur.")  # Baris ini juga diindentasi
 ```
```Contoh indentasi salah
umur = 16
if umur >= 18:
    print("Anda sudah dewasa.")  # Baris ini diindentasi
     print("Selamat datang.")     # Baris ini juga diindentasi
else:
    print("Anda masih di bawah umur.")  # Baris ini juga diindentasi
 ```
