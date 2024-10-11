# if digunakan untuk membuat kondisi
# elif digunakan untuk membuat kondisi jika if tidak terpenuhi
# else dieksekusi ketika if dan elif tidak terpenuhi


a = 25

if a > 50:
    print("Nilai a lebih dari 50") 
elif a == 50:
    print("Nilai a sama dengan 50")
else:
    print("Nilai a kurang dari 30")

# Kalkulator
x = int(input("Masukan angka : "))
y = int(input("Masukan angka : "))
operator = input("masukan (+,-,/,*) : ")

if operator == "+":
    print(f"{x} + {y} = {x + y}")
elif operator == "-":
    print(f"{x} - {y} = {x - y}")
elif operator == "+":
    print(f"{x} / {y} = {x / y}")
elif operator == "*":
    print(f"{x} * {y} = {x * y}")
else:
    print("Error")