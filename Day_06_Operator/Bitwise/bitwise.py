a = 5
b = 7

print("Bitwise &")
# and (&) 
# True(1), False(0) -> akan true jika keduanya true
c = a & b
print(a, "-->", bin(a)) # 5 --> 0b101
print(b, "-->", bin(b)) # 7 --> 0b111
print("-" *12, "&")     # -----------&
print(c, "-->", bin(c)) # 5 --> 0b101

# or (|)
# True(1), False(0) -> akan true jika salah satunya true
print("Bitwise |")
c = a | b
print(a, "-->", bin(a)) # 5 --> 0b101 
print(b, "-->", bin(b)) # 7 --> 0b111
print("-" *12, "|")     # -----------|
print(c, "-->", bin(c)) # 7 --> 0b111

# xor (^)
# True(1), False(0) -> akan true jika salah satu saja, jika keduanya bernilai true atau keduanya bernilai false maka akan menghasilkan nilai false
print("Bitwise ^")
c = a ^ b
print(a, "-->", bin(a)) # 5 --> 0b101
print(b, "-->", bin(b)) # 7 --> 0b111
print("-" *12, "^")     # -----------^
print(c, "-->", bin(c)) # 2 -->  0b10

# not (~)
print("Bitwise ~")
# membalikan nilai bit -(n+1)
a = 10 # 0b1010 
print("Sebelum menggunakan bitwise not(~)")
print(a, "-->", bin(a) ) # 10 -->1010 0b
print("Sesudah menggunakan bitwise not(~)")
print(~a, "-->", bin(~a) ) # -11 --> 0b1011

# shift left(<<)
print("shift left(<<)")
a = 8  # 0b1000 
result = a << 1  # 0b10000 (16 dalam desimal)
print("-> =", result)  # Output: 16
print(bin(result))  # Output: 0b10000

result2 = a << 2 # 0b100000
print(result2)  # Output: 32
print(bin(result2))  # Output: 0b100000

# shift right(>>)
print("shift right(>>)")
a = 12 # 0b1100
result = a >> 1  # 0b0110 (6 dalam desimal)
print(result)  # Output: 6
print(bin(result))  # Output: 0b110

result = a >> 2  # 011 (6 dalam desimal)
print(result)  # Output: 3
print(bin(result))  # Output: 0b11

