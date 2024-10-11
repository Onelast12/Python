
# if digunakan untuk mengambil keputusan (True)
umur = 20
if umur > 17:
    print("Anda sudah dewasa") # Output: Anda sudah dewasa
# if else
# else akan dieksekusi jika kondisi if tidak terpenuhi(False)
umur = 15
if umur > 17: # -> Kondisi True
    print("Anda sudah dewasa")
else: # -> Kondisi False
    print("Anda belum desawa") # Output: Anda belum dewasa

# if dengan string menggunakan operator perbandingan (==, !=)
text = "Python"
if text == "Python":
    print("Kata yg dimasukan benar")
else:
    print("Kata yg dimasukan salah")

text = "Java"
if text != "Python":
    print("False")

# if dengan string dan operator in, not in
# in
kalimat = "Belajar python"
if "python" in kalimat:
    print("python ada dalam kalimat")

# not in
kalimat = "Sedang belajar java"
if "python" not in kalimat:
    print("python tidak ada dalam kalimat")

# if dengan nilai kosong
str = ""
if str == "":
    print("string kosong")
else:
    print("string berisi sesuatu")

# if dengan input pengguna
x = int(input("Masukan Angka : "))

if x > 5:
    print(f"{x} lebih dari 5")
else:
    print(f"{x} kurang dari 5")