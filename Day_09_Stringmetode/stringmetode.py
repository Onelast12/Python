
# 1. Metode manipulasi karakter
# capitalize(), lower(), upper(), title(), dan swapcase()
txt = "pemrograman python"
print("capitalize :", txt.capitalize()) # Output: Pemrograman python
txt = "pemrograman python"
print("title :", txt.title()) # Output: Pemrograman Python
txt = "pemrograman python"
print("upper :", txt.upper()) # Output: PEMROGRAMAN PYTHON
txt = "PYTHON"
print("lower :", txt.lower()) # Output: python
txt = "PemRogRaman pYtHoN"
print("swapcase :", txt.swapcase()) # Output: pEMrOGrAMAN PyThOn

# 2. Metode Pengecekan
# isalpha(), isalnum(), isdigit(), isspace(), islower(), istitle(), isupper()

alphabet = "Python"
print(alphabet.isalpha()) # Output: True
angkaNomor = "K3"
print(angkaNomor.isalnum()) # Output: True, Note: Wajib angka atau huruf
digit = "1"
print(digit.isdigit()) # Output: True
space = " "
print(space.isspace()) # Ouput: True
lower = "belajar python"
print(lower.islower()) # Output: True
upper = "BELAJAR PYTHON"
print(upper.isupper()) # Output: True
title = "Belajar Python"
print(title.istitle()) # Output: True

# 3. Metode Pemeriksaan Awal dan Akhir String
# endswith(), startswith()

# startswith(substring, start, index)
text = "Belajar python"
print(text)
print(text.startswith("Belajar")) # Output: True
print(text.startswith("python"))  # Output: False
print(text.startswith("python", 8))  # Output: True, Karena huruf P ada di index 8
print(text.startswith("python", 7))  # Output: False, huruf P bukan di index 7

# endswith(substring, start, index)
text = "Belajar python"
print(text.endswith("python"))  # Output: True
print(text.endswith("Belajar"))  # Output: False
print(text.endswith("Belajar", 0, 7))  # Output: True
print(text.endswith("Belajar", 0, 6))  # Output: False, Karena "Belajar" ada di index 0 sampai 7

# 4. Metode Penggantian dan Penghapusan
# replace, strip, lstrip, rstrip*
# replace(old, new, count)
text = "Hello, world"
print(text.replace("Hello", "What")) # Output: What, world
text2 = "##Hello, world##"
# strip()
print(text2.strip("#")) # Output: Hello, world
# lstrip()
print(text2.lstrip("#")) # Output: Hello, world##
# rstrip()
print(text2.rstrip("#")) # Output: ##Hello, world

# 5. Metode Pencarian dan Pengecekan Substring. (find, rfind, index, rindex)
# find(str, start, end) mulai pencarian dari index 0
text = "Python Pip"
print(text.find("P")) # Output: 0
print(text.find("r")) # Output: -1 -> karna tidak ada nilai text
# rfind  mulai pencarian dari kanan kekiri
print(text.rfind("P")) # Output: 7
print(text.rfind("u")) # Output: -1 -> karna tidak ada nilai text
# index
text = "Java"
print(text.index("J")) # Output: 0
"""
print(text.index("P")) # akan Vallueerror jika tidak ingin error menggunakan str.find()
"""
# rindex
text = "Pemrograman Python"
print(text.rindex("o")) # Output: 16

# 6. Metode Penyesuaian Lebar String -> center(), ljust(), rjust()
# center(width, fillchar)
text = "Python"
print(text.center(10, "#")) # Output: ##Python## 
print(text.center(12, "#")) # Output: ###Python###
print("width kurang dari panjang string")
print(text.center(5, "#")) # Output: Python
# Tidak ada error, tetapi hasilnya tetap akan mencetak string "Python"/
# tanpa ada perubahan, karena panjang string asli sudah lebih besar dari 5.
# Note: pastikan parameter width jangan kurang dari jumlah karakter

text = "R".center(4, "#")
print(text) # Output: #R##  Note: Jika total menjadi ganjil akan diutamakan kekiri.

# ljust(width, fillchar)
text = "Java"
print(text.ljust(10, "$")) # Output: Java$$$$$$
print(text.ljust(7, "*")) # Output: java***
print("width lebih besar dari panjang string")
print(text.ljust(5, "#")) # Output: Java#

# rjust(width, fillchar)
text = "JavaScript"
print(text.rjust(15, "-")) # Output: -----JavaScript
print(text.rjust(12, "8")) # Output: 88JavaScript
print("width lebih besar dari panjang string")
print(text.rjust(11, ">")) # Output: >JavaScript

## note: Jika fillchar tidak disertakan maka karakter yg digunakan adalah spasi

txt = "WHY".center(5, "!")
print(txt) # Output: !WHY!
print(txt.ljust(7, "%")) # Output: !WHY!%%

# tambahan count() menghitung jumlah karakter
txt = "Pemrograman python dan belajar python itu simple"
print(txt.count("P")) # Output: 1
print(txt.count("python")) # Output: 2
print(txt.count("o")) # Output: 3