daftar_siswa = [
    {"nama": "Meca", "kelas":"X RPL", "absen":11},
    {"nama": "Latif", "kelas":"X RPL", "absen":12},
    {"nama": "Darel", "kelas":"X RPL", "absen":13}
]

print("NAMA\tKELAS\tABSEN")
print("========================================================")
for siswa in daftar_siswa:
    print(f"{siswa['nama']}\t{siswa['kelas']}\t{siswa['absen']}")

for siswa in daftar_siswa:
    print(f"nama:\t{siswa['nama']}")
    print(f"kelas:\t{siswa['kelas']}")
    print(f"absen:\t{siswa['absen']}")
    print("===============================")
    print(f"nama:\t{siswa['nama']}")
    print(f"kelas:\t{siswa['kelas']}")
    print(f"absen:\t{siswa['absen']}")
    print("===============================")
    print(f"nama:\t{siswa['nama']}")
    print(f"kelas:\t{siswa['kelas']}")
    print(f"absen:\t{siswa['absen']}")