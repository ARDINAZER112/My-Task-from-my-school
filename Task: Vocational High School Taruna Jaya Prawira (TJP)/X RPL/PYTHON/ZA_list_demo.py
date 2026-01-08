print("=========================== LIST ============================")
# LIST 
buah = ["apel", "jeruk", "mangga"]

print("Daftar buah:")
for b in buah:
    print("-", b)

buah.append("pisang")
print("Setelah ditambah:", buah)

buah.remove("jeruk")
print("Setelah dihapus:", buah)

buah.append("semangka")
print("Setelah ditambahkan:", buah)





print("                                                         ")
print("                                                          ")
print("==================================== TUPLE ===============================")
# TUPLE 
warna = ("merah", "hijau", "biru")

print("warna kedua adalah", warna[1])

# Akan eror karena tuple tidak bisa diubah




print("                                         ")
print("                                         ")
print("=================================== DICTIONARY ============================")
# DICTIONARY 
siswa = {"nama": "Budi", "umur": 16}

print("Nama siswa:", siswa["nama"])
siswa["kelas"] = "X RPL"
siswa["Alamat"] = "Jl. Pramuka 23 Tuban"
siswa["No HP"] = "087618312"

for key, value in siswa.items():
    print(key, ":", value)



print("                                ")
print("                                              ")
print("================================= GABUNGAN ==========================")
# Gabungan
daftar_siswa = [
    {"nama": "Budi", "umur": 16},
    {"nama": "Latif", "umur": 20139}
]

for siswa in daftar_siswa:
    print(siswa["nama"], "-", siswa["umur"], "tahun")
