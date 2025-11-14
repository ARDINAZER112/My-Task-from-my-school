nama = input("Masukkan Nama :")
nilai = input("Masukkan Nilai :")
daftar_siswa = [
    {"nama": nama, "nilai": nilai}
]
print("NAMA\tNILAI")
for siswa in daftar_siswa:
    print(f"{siswa['nama']}\t{siswa['nilai']}")


