
# 1. assign(=)
# memberikan nilai ekspresi RHS ke operan LHS
a = 10 # = : assign
b = 20
c = a + b
print(c)

# 2. add and assign(+=)
x = 5
y = 10
x += 1 # --> x = x + 1 hasil 6
x += y # --> x = x + y
print(a) # hasil = 16

# 3. sub and assign(-=)
x -= y
print(x)

# 4. multiply and assign(*=)
x *= y
print(x)

# 5. division and assign(/=)
x /= y
print(x)

# 6. division floor and assign(//=)
x //= y
print(x)

# 7. modulus and assign(%=)
x %= y
print(x)

# 8. exponent and assign(**=)
x **= y
print(x)

# 9. Bitwise(AND) and assign(&=)
x = 10
y = 9
x &= y # x = x & y
print(x)

# 10. Bitwise(OR) and assign(|=)
x = 10
y = 9
x |= y
print(x)

# 11. Bitwise(XOR) and assign(^=)
x = 10
y = 9
x ^= y
print(x)

# 12. Bitwise Right shift and assign(>>=)
x = 10
print("biner 10\t=\t", bin(x))
y = 2
x >>= y
bin(x)
print(x)
print("biner", x, "\t=\t", bin(x))

# 13. Bitwise Right shift and assign(>>=)
x = 10
print("biner", x, "\t=\t", bin(x))
y = 2
x <<= y
bin(x)
print(x)
print("biner", x,"\t=\t", bin(x))