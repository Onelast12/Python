

userName = input("Masukan nama : ")
email = userName.find("@")
nama = userName[email:]
nama2 = nama
print(nama2)

if nama2 == "@facebook.com":
    print("Selamat datang")
else:
    print("wajib memasukan alamat facebook")
