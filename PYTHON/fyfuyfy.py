try:
    nilai = float(input("Masukkan nilai siswa: "))
    if nilai >= 90:
        print("Sangat Baik")
    elif nilai >= 75:
        print("Baik")
    else:
        print("Perlu Ditingkatkan")
except ValueError:
    print("Error: Masukkan angka yang valid!")