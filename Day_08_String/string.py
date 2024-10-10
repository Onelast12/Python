data = "ini adalah string"
print(data)
print(type(data))

# 1.Cara membuat string
"""
    1. Menggunakan single qoute '...'
    2. Menggunakan double qoute "..."
"""

text1 = 'Saya tidak memilih single qoute'
text2 = "Saya memilih Double qoute"
print(text1)
print(text2)

# 2. Panjang string menggunakan len()
kata = "Halo, apa kabar"
print(len(kata)) # 15

# 3. Index dalam string
kata = "Kamu sehat"
print(kata[0]) # Output: K -> index 0 elemen awal
print(kata[2]) # Output: m
print(kata[-1]) # Output: t -> index -1 dari elemen akhir

# 4. Slicing
kata = "Kamu sehat"
print(kata[0:4]) #Output: Kamu (karakter dari index 0 hingga 4)
print(kata[2:]) #Output: amu (karakter dari index 2 hingga akhir)
print(kata[:-1]) #Output: tanes umaK (dimulai dari elemen akhir)
print(kata[:2:-1]) #Output: tanes u (dimulai dari elemen akhir hingga index 3)

# 5. Menggabungkan string(concatenate)
nama1 = "Halo"
nama2 = "apa kabar"
gabungan = nama1 + ", " + nama2 + "?"  # Output: 'Halo,apa kabar?'
print(gabungan)

# 6. Mengulang string
ungkapan = "Hai " * 3  # Output: 'Hai! Hai! Hai! '
print(ungkapan)

# 7. Memunculkan tanda kutip tunggal dan ganda pada output
print('"Hallo, apa kabar?"') 
print("'Hallo, apa kabar?'")
print("Shalat di hari jum'at") 

# 8. Menggunakan tanda kutip tunggal(') dengan single qoute' memakai tanda(\)
# Menggunakan tanda ' menjadi string
print('Mari shalat jum\'at') # Memakai single qoute
print('sekarang jum\'at. mari shalat jum\'at')

# 9. Menggunakan backlash untuk memunculkan \ 
print("C:\\user\\nama folder")

# 10. tab(\t) memberikan tab pada output
print("Teman\t\t\tjauh, semakin jauh") #Output: Teman   jauh. semakin jauh

# 11. backspace menghapus per karakter 
print("Temen \bdeket, jadi deketan") #Output: Temendeket, jadi deketan

# 12. newline(\n) memberikan enter pada output
print("line 1.\nline 2") # LF -> Line feed -> linux, macos ,unix 
print("line 2.\rline 2") # CR -> Carriage return -> commodere
print("line 3.\r\nline 3") # CRLF ->  Windows

# 13. String Literal atau raw
print("C:\new folder") # karakter \ akan dianggap karakter khusus

# 14. menggunakan raw(r)
print(r"C:\new folder") # Semua akan dianggap string

# 15. Multiline literal string ->
multiline = """
|_____|
|     |
"""
print(multiline) # akan diprint sesuai apa yg diketik