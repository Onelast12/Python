# Day 13
# Belajar tentang if bersarang (nested if statements) di Python adalah langkah penting untuk memahami alur kontrol yang lebih kompleks.
# Nested if adalah kondisi if yang diletakkan di dalam blok kode if atau kondisi lainnya.

*Syntax dasar*
```
if kondisi1:
    if kondisi2:
        # blok kode jika kedua kondisi benar
```
Contoh
```
score = 85
if score >= 50:
    print("Anda lulus.")
    if score >= 90:
        print("Anda mendapat nilai A.")
else:
    print("Anda tidak lulus.")
```
*Contoh Menggunakan else di nested if*
```
nilai = 85
if nilai >= 50:
    print("Anda lulus.")
    if nilai >= 90:
        print("Anda mendapat nilai A.")
    else:
        print("Nilai Anda tidak cukup untuk A.")
else:
    print("Anda tidak lulus.")
```
*Contoh menggunakan else if(elif) di nested if*
```
nilai = 85
if nilai >= 50:
    print("Anda lulus.")
    if nilai >= 90:
        print("Anda mendapat nilai A.")
    elif nilai >= 70:
        print("Anda mendapat nilai B.")
    else:
        print("Nilai Anda tidak cukup untuk A.")
else:
    print("Anda tidak lulus.")
```
