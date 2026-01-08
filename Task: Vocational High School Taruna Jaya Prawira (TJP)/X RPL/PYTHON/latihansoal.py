#Buat Program yang meminta input nilai dan menampilkannya
print("========================= Cek Lulus =============================")
nilai = 72
nilai = int(input("Masukkan Nilai : "))

if nilai >= 75:
    print("Selamat Anda lulus")
else:
    print("Selamat Anda Tidak Lulus")


#Buat Program yang meminta input nilai dan menampilkkan penilaiannya
print("========================= Cek Nilai ===============================")
nilai=int(input("Masukkan NIlai :"))
Nilai = 80

if nilai >= 90:
    print("A")
elif nilai >= 80:
    print ("B")
elif nilai >= 70:
    print ("C")
elif nilai >= 60:
    print("D")
else:
    print("E")


#Buat Program yang meninta input umur dan status pekerjaannya
print("========================= Cek Umur ===============================")
nilai=int(input("Masukkan Umur :"))
Nilai = 18

if nilai >= 18:
    print("Dewasa Dan Bekerja")
elif nilai >= 18:
    print ("Dewasa Tapi Belum Bekerja")
else:
    print("Belum Dewasa")
