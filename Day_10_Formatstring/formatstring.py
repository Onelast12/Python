nama = "Ahmad"
umur = 23
print("nama :", nama, "umur dan saya :", umur)

# Menggunakan formatstring literal
gabungan = f"nama : {nama} dan umur saya : {umur}"
print(gabungan)
print(f"nama : {nama} dan umur saya : {umur}")

# format presisi angka desimal menggunakan f-string
pi = 3.14159
print(f"Nilai pi adalah {pi:.2f}") # Output: 3.14
# menampilkan leading zero
print(f"Nilai pi adalah {pi:010.2f}") # Output: 3.14

# bilangan dengan ordo
harga = 5000000
print(f"jutaan = {harga:_}") # Output: 5_000_000

# menentukan lebar kolom dengan format
nilai = 123
print(f"Nilai rata kanan dengan lebar 5: {nilai:}")

nilai = 92.678
print(f"Nilai ujian saya adalah {nilai:.1f} dan rata kanan {nilai:10.2f}")

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}" 
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)