#Struktur Fungsi
#print("Struktur Fungsi")
#def nama_fungsi(parameter1, parameter2):
    # blok kode
#   return hasil

#Praktek
print("Fungsi Tanpa Parameter")
def salam():
    print("HELLO, WELCOME TO CLASS X RPL")

salam()

#Fungsi Dengan Parameter

print("================Fungsi Dengan Parameter======================")
nama = ["Latif", "Darel", "Rengga"]

def salam_nama(nama):
    print(f"Halo {nama}, \tSelamat belajar Python!")

for n in nama:
    salam_nama(n)

#Fungsi Return
print("=========================Return==============================")
def kali(a,b):
    return a * b

def tambah(a,b):
    hasil = a + b
    return hasil

hasil = kali(4, 5)
print("Hasil Perkalian:", hasil)

print("Hasil Penjumplahan:", tambah(12,10))

#Fungsi untuk menghitung luar lingkaran
print("=======================Import=====================================")
import math
def luas_lingkaran(r):
    return math.pi * r * r

def volume_kubus(s):
    return s ** 3

def volume_kerucut(r,t):
    return (1/3) * math.pi * r * r * t

jari = 12
print("Luas lingkaran:", luas_lingkaran(jari))

sisi = 21
print("Volume Kubus:", volume_kubus(sisi))

jari = 13
tinggi = 14
print("Volume Kerucut:", volume_kerucut(jari, tinggi))

