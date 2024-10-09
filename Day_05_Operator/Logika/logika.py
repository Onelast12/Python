# Logika digunakan untuk menggabungkan pernyataan logika.

a = True
b = False

print("AND")
print("True and True   = ", a and a) # True
print("True and False  = ", a and b) # False
print("False and True  = ", b and a) # False
print("False and False = ", b and b) # False
# and-> akan True jika keduanya True

print("OR")
print("True or True   = ", a or a) # True
print("True or False  = ", a or b) # True
print("False or True  = ", b or a) # True
print("False or False = ", b or b) # False
# or-> akan True jika salah satunya True

print("NOT")
print("not True  : ", not a) # False
print("not False : ", not b) # True
# not-> membalikan nilai kebalikan
