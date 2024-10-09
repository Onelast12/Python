# Casting 
dataInt = 5 # Integer bilangan bulat
dataFloat = 5.0 # Float bilangan desimal
dfloat = 2. # --. 2.0 atau .4 --. 0.4
dataStr = 2 # String Kumpulan karakter yg diapit tanda kutip tunggal mau double
dataBool = True # Boolean menyatakan nilai benar dan salah.

# fungsi type() untun mengetahui tipe data pada sebuah variabel

print(type(dataInt))
print(type(dataFloat))
print(type(dataStr))
print(type(dataBool))

print("\nINTEGER CASTING --> FLOAT, STR, DAN BOOLEAN")
dfloat = float(dataInt) 
print(type(dfloat))
dStr = str(dataInt)
print(type(dStr))
dBool = bool(dataInt) # Mengubah boolean ke integer(True=1, False=0)
print(type(dBool))

print("\nFLOAT CASTING --> INTEGER, STR, DAN BOOLEAN")
dInt = int(dataFloat) # float ke int akan menjadi bilangan bulat
print(type(dInt))
dStr = str(dataFloat) 
print(type(dStr))
dBool = bool(dataFloat)
print(type(dBool))

print("\nFLOAT STRING --> INTEGER, FLOAT, DAN BOOLEAN")
dInt = int(dataStr) # string ke integer wajib angka
print(type(dInt))
dFloat = float(dataStr) # string ke float wajib angka
print(type(dFloat))
dBool = bool(dataStr) #string ke boolean(jika string kosong akan-> False,jika tidak kosong ->True)
print(type(dBool))
# note : jika str dicasting ke int, float wajib angka!!

print("\nFLOAT BOOLEAN --> INTEGER, FLOAT, DAN STRING")
dInt = int(dBool) # jika 0 = False, jika 1 = True
print(type(dInt))
dFloat = float(dBool) # jika 0.0 = False, jika 0.1 > = True
print(type(dFloat))
dstr = str(dBool) 
print(type(dstr))
