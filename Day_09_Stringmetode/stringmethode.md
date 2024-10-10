# Metode string di Python adalah fungsi bawaan yang dapat digunakan untuk memanipulasi dan memproses data string.
# str.stringmetode

*list method string*
# 1. Metode Manipulasi karakter
 *capitalize, title, upper, lower, swapcase*
 - capitalize() -> merubah huruf pertama dari string menjadi huruf besar
 - title() -> merubah huruf pertama dari setiap kata menjadi huruf besar
 - lower() -> merubah semua huruf string menjadi huruf kecil.
 - upper() -> merubah semua huruf string menjadi huruf besar.
 - swapcase() -> merubah huruf besar menjadi huruf kecil dan sebaliknya

# 2. Metode Pengecekan(Checking Methods)
 *isascii, isalnum, isalpha, isdecimal, isdigit, isnumeric, islower, istitle, isupper, dan isspace*
 - isalpha(): Memeriksa apakah semua string hanya berisi huruf.
 - isdigit(): Memeriksa apakah semua string hanya berisi angka.
 - isalnum(): Memeriksa apakah semua string hanya berisi huruf dan angka.
 - isspace()-> memeriksa apakah string hanya berisi spasi
 - istitle() -> memeriksa apakah semua huruf dalam format judul
 - isupper() -> memeriksa apakah semua huruf dalam string huruf besar
 - islower() -> memeriksa apakah semua huruf dalam string huruf kecil

# 3. Metode Pemeriksaan Awal dan Akhir String
 *endswith, startswith*
 - startswith(prefix): Memeriksa apakah string dimulai dengan prefix.
 - endswith(suffix): Memeriksa apakah string diakhiri dengan suffix.

# 4. Metode Penggantian dan Penghapusan
 *replace, strip, lstrip, rstrip*
 - replace(old, new, count) -> mengganti old dengan new.sebanyak count
 - strip() -> menghapus karakter diawal dan diakhir string
 - lstrip() -> menghapus karakter diawal string
 - rstrip() -> menghapus karakter diakhir string

# 5. Metode Pencarian dan Pengecekan Substring
 *find, rfind, index, rindex*
 - find(substring, start, end) -> Mencari posisi pertama substring, jika tidak ditemukan mengembalikan -1.
 - rfind(substring, start, end) -> Mencari posisi terakhir substring, jika tidak ditemukan mengembalikan -1.
 - index(substring, start, end) -> Sama seperti .find(), tetapi menghasilkan error jika substring tidak ditemukan.
 - rindex(substring, start, end) -> Sama seperti .rfind(), tetapi menghasilkan error jika substring tidak ditemukan.

# 6. Metode Penyesuaian Lebar String
 *center, ljust, rjust*
 **width -> Digunakan untuk menentukan lebar karakter**
 **fillchar -> Digunakan untuk mengisi ruang kosong yg tersedia**
 **note: jika fillchar tidak disertakan maka karakter yg digunakan adalah spasi**
 - center(width, fillchar) -> Mengatur string di tengah dengan lebar tertentu dan mengisi ruang kosong dengan karakter tertentu.
 - ljust(width, fillchar) -> Mengatur string di sebelah kiri dengan lebar tertentu dan mengisi ruang kosong di kanan dengan karakter tertentu.
 - rjust(width, fillchar) -> Mengatur string di sebelah kanan dengan lebar tertentu dan mengisi ruang kosong di kiri dengan karakter tertentu.


# 7. Metode Pemisahan dan Penggabungan
 *split, rsplit, splitlines, join(iterable)*
 - split(separator, maxsplit): Memisahkan string menjadi list berdasarkan pemisah (separator).
 - rsplit(separator, maxsplit): Sama dengan .split() tetapi mulai memisahkan dari kanan.
 - splitlines(): Memisahkan string berdasarkan baris baru (newline).
 - join(iterable): Menggabungkan elemen dari iterable menjadi satu string dengan separator.

# Kenapa Metode String Penting?
Mempermudah pemrograman: Banyak tugas manipulasi string, seperti mengubah huruf atau mencari substring, bisa dilakukan dengan satu baris kode.
Mengurangi kompleksitas: Anda tidak perlu menulis algoritma yang kompleks untuk tugas-tugas umum karena Python sudah menyediakan metode-metode ini.
Konsistensi: Dengan memahami metode string, Anda akan dapat memanipulasi data teks dengan cara yang konsisten dan dapat diprediksi di berbagai proyek.