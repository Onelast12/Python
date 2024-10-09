# Operator identitas dalam Python digunakan untuk membandingkan apakah dua objek adalah objek yang sama di memori. Python memiliki dua operator identitas, yaitu:

# is: Mengembalikan True jika kedua variabel merujuk pada objek yang sama.
# is not: Mengembalikan True jika kedua variabel tidak merujuk pada objek yang sama

a = 4
b = a
c = 6

print("id a =", id(a))
print("id b =", id(b))
print("id c =", id(c))

print("a is b = ", a is b) # True
print("a is c = ", a is c) # False

print("a is not b = ", a is not b) # False
print("a is not c = ", a is not c) # True