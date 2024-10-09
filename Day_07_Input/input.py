

nama = input("Masukan nama : ")
print(nama)
print(type(nama)) # <class 'str'>
# Akan selalu dianggap string walaupun angka yg dimasukan

# Casting
angka = input("Masukan angka : ")
print(angka)
print(type(angka)) # <class 'str'>
angka = int(angka)
print(type(angka)) # <class 'int'>

# atau
angka1 = int(input("Masukan angka :"))
print(angka1)
print(type(angka1)) # <class 'int'>
# jauh lebih simpel
