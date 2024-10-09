# Operator Keanggotaan digunakan untuk memeriksa apakah nilai ada dalam koleksi.
# memiliki in dan not in

# 1. in
# Dalam list
buah = ['apel', 'pisang', 'semangka']
print('apel' in buah)  # Output: True
print('jeruk' in buah)  # Output: False

# Dalam string
text = "Python"
print('P' in text)  # Output: True
print('z' in text)  # Output: False

# Dalam tuple
nomor = (1, 2, 3, 4)
print(3 in nomor)  # Output: True

# 2. not in
# Dalam list
buah = ['apel', 'pisang', 'semangka']
print('jeruk' not in buah)  # Output: True
print('pisang' not in buah)   # Output: False

# Dalam string
text = "Python"
print("Java" not in text)  # Output: True
print("Python" not in text) # Output: False

# Dalam set
vegetables = {'wortel', 'kentang', 'tomat'}
print('bawang' not in vegetables)  # Output: True
