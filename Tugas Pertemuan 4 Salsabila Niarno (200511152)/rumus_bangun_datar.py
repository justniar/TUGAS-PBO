from perhitungan import *
from perhitungan_dua import*

# buat fungsi opsi
def opsidatar():
    print("A. persegi")
    print("B. segitiga")
    print("C. lingkaran")
    print("-"*50)

def rumus_rumus():
    print("a : luas")
    print("b : keliling")
    print("c : luas dan keliling")

# Memilih rumus mana yang akan dijalankan
def bangunDatar():
    print("Program menghitung luas dan keliling bangun datar".center(70,"-"))
    opsidatar()
    rumus = input("Bangun datar apa yang ingin Anda hitung?: ")
    if rumus == "a":
        rumus_rumus()
        pilih = input("ingin menghitung apa? ")
        if pilih == "a":
            print("Luas Persegi Panjang sebesar: ", luasPersegi(int(input("masukkan panjang: ")), int(input("masukkan lebar: "))), "cm^2")
        elif pilih == "b":
            print("Keliling Persegi Panjang sebesar: ", kelilingPersegi(int(input("masukkan panjang: ")), int(input("masukkan lebar: "))), "cm")
        elif pilih == "c":
            luasKelilingpersegi(int(input("masukkan panjang: ")), int(input("masukkan lebar: ")))
        else:
            print("coba ketikkan bukan dalam huruf kapital")

    elif rumus == "b":
        rumus_rumus()
        pilih = input("ingin menghitung apa?")
        if pilih == "a":
            print("Luas Segitiga sebesar: ", luasSegitiga(int(input("Masukkan alas: ")), int(input("Masukkan tinggi: "))), "cm^2")
        elif pilih == "b":
            print("Keliling Segitiga sebesar: ", kelilingSegitiga(int(input("Masukkan sisi 1: ")), int(input("Masukkan sisi 2: ")), int(input("Masukkan sisi 3: "))), "cm")
        elif pilih == "c":
            luasKelilingSegitiga(int(input("Masukkan Alas: ")), int(input("Masukkan tinggi: ")), int(input("Masukkan sisi 1: ")), int(input("Masukkan sisi 2: ")), int(input("Masukkan sisi 3: ")))
        else:
            print("coba ketikkan bukan dalam huruf kapital")

    elif rumus == "c":
        lingkaran(float(input("Masukkan Jari-jari: ")))
    else:
        print("Maaf, Kami Belum mengetahui rumusnya")
    return rumus

bangunDatar()
while True:
    line = input("Apakah Lanjut?")
    if line == "yes":
        bangunDatar()
        continue
    if line == "no":
        break
print("Selesai!")
