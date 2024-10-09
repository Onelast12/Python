# Day 6 
# 5. Bitwise digunakan untuk operasi bit-level.
 **Bitwise AND(and=&)**
 - Akan True jika keduanya True. True(1) and False(0)
 ```AND(&)
 -----------------------------------------
 0b1010   --> 10 dalam bentuk biner
 0b1000   --> 8 dalam bentuk biner
 -------(&)
 0b1000   --> 8
------------------------------------------
 1 & 1 = 1
 1 & 0 = 0
 0 & 1 = 0
 0 & 0 = 0
 ```
 **Bitwise OR(or=|)**
 - Menghasilkan 1 jika salah satu atau kedua bit adalah 1
```OR(|)
------------------------------------------
 0b1010   --> 10 dalam bentuk biner
 0b1000   --> 8 dalam bentuk biner
 -------(\)
 0b1010   --> 10
------------------------------------------
 1 | 1 = 1
 1 | 0 = 1
 0 | 1 = 1
 0 | 0 = 0
 ```

 **Bitwise NOT(not=~)**
 - membalikan nilai bit -(n+1)
```NOT(~)
 a = 7
 c = ~a
 print(c)
 Output : -8
 ``` 
 **Bitwise XOR(xor=^)**
 - Menghasilkan 1 jika hanya salah satu bit yang 1, tetapi bukan keduanya.
```XOR(^)
------------------------------------------
 0b1010   --> 10 dalam bentuk biner
 0b1000   --> 8 dalam bentuk biner
 -------(^)
 0b0010   --> 2
------------------------------------------
 1 ^ 1 = 0
 1 ^ 0 = 1
 0 ^ 1 = 1
 0 ^ 0 = 0
```

 **Bitwise Left Shift(<<)**
 - Berguna untuk menggeser bit ke arah kiri. Setiap bergeser ke keri akan dikali 2
```(<<)
a = 8 # --> 0b1000
b = a << 1 , # akan menggeser ke kiri 0b100000
print(b)
Output: 16
```

 **Bitwise Right Shift(>>)**
  - Berguna untuk menggeser bit ke arah kanan. Setiap bergeser ke kanan akan dikali 2
```(>>)
a = 8 , # --> 0b1000 
b = a >> 1 , # akan menggeser ke kanan 0b10
print(b)
Output: 4 
```

# 6. Keanggotaan digunakan untuk memeriksa apakah nilai ada dalam koleksi.
 - in untuk memeriksa apakah suatu nilai ada dalam koleksi.
 ```Dalam string
text = "Python"
print('P' in text)  # Output: True
print('z' in text)  # Output: False
 ```
 - not in memeriksa apakah suatu nilai tidak ada dalam koleksi.
```Dalam string
text = "Python"
print("Java" not in text)  # Output: True
print("Python" not in text)  # Output: False
 ```

# 7. Identitas digunakan untuk memeriksa apakah dua objek berada di lokasi memori yg sama.
- is: Mengembalikan True jika kedua variabel merujuk pada objek yang sama.
- is not: Mengembalikan True jika kedua variabel tidak merujuk pada objek yang sama.
