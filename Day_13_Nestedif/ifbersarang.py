
nilai = 70

if nilai >= 60:
    print(f"Dengan nilai {nilai} anda lulus")
    if nilai >= 80:
        print(f"{nilai} lulus dengan nilai predikat")
else:
    print("Maaf anda tidak lulus")

# if menggunakan input pengguna
angka = int("Masukan angka : ")

if angka >= 0:
    print("Bilangan positif")
    if angka % 2 == 0:
        print("Bilangan genap")
    else:
        print("Bilangan ganjil")
else:
    print("Bilangan negatif")