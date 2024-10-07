# Variabel dalam python

namaDepan = "One"
namaBelakang = "Last"
negara = "Indonesia"
umur = 23

# print 
print("Nama Depan : ", namaDepan)
print("Jumlah Nama Depan: ", len(namaDepan))
print("Nama Belakang : ", namaBelakang)
print("Jumlah nama Belakang : ", len(namaBelakang))
print("Negara : ", negara)
print("Umur : ", umur)

# Penulisan camelCase
userName = "nama"

x = "Banana"
print("x")

# Banyak nilai ke beberapa variabel
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# catatan : Pastikan Jumlah variabel sesuai dengan jumlah nilai

# Satu Nilai kebeberapa variabel
x = y = x = "Si kuprit"
print(x)
print(y)
print(z)

# Unpack a collection
# mengektrak nilai kedalam variabel
fruits = "Manggo", "Banana", "Watermelon"
x, y, z = fruits
print(x)
print(y)
print(z)

# Tipe NoneType menyatakan jenis objek yg tidak memiliki nilai.
# dalam python objek tanpa nilai ditandai dengan None.
s = None
print(s)
print("tipe s = ", type(s))
# None sering digunakan sebagai nilai default untuk variabel yang belum diinisialisasi.


