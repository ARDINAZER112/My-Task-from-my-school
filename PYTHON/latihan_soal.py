pj = int(input("ketik panjang : "))
lb = int(input("ketik lebar : "))
L = pj * lb
K = 2 * (pj + lb)
print("\n---nilai akhir---")
print("Luas Persegi Panjang :",L, "cm")
print("Keliling Persegi Panjang :",K, "cm")








UT = int(input("Ketik Nilai Ujian Teori : "))
UP = int(input("Ketik Nilai Ujian Praktek : "))

#Lulus Jika Nilai Uijian Teori >= 70 dan Nilai Ujian Praktek >= 75
print("Status :",(UT >= 70) and (UP >= 75))





#meminta input angka dari pengguna
angka = float(input("masukkan angka : "))
#menghitung kuadrat
Kuadrat = angka ** 2
#menampilkan kuadrat
print(f"Kuadrat dari {angka} adalah {Kuadrat}")
#memriksa apakah angka lebih besar dari 50
if angka > 50:
    print(f"{angka} lebih besar dari 50")
else:
    print(f"{angka} tidak lebih besar dari 50")

