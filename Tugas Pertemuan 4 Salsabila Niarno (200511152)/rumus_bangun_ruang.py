from perhitungan import *
from perhitungan_dua import *

# Rumus-rumus bangun ruang
# Memilih rumus mana yang akan dijalankan
def opsi():
    print("a. balok")
    print("b. kerucut")
    print("c. bola")
    print("d. tabung")
    print("-"*50)

def pilihan():
    print("1. volume")
    print("2. luas")
    print("3. volume dan luas")

def bangunRuang():
    print("Program menghitung volume dan luas permukaan bangun ruang".center(70,"-"))
    opsi()
    ruang = input("Masukkan Opsi: ")
    print("Anda ingin menghitung: ", ruang)
    #Perhitungan untuk balok
    if ruang == "a":
        pilihan()
        pilih = input("Apa yang ingin Anda Cari? ")
        print("-"*50)
        if pilih == "1":
            print("Volume balok sebesar: ", volBalok(int(input("Masukkan tinggi: ")),int(input("Masukkan panjang: ")), int(input("Masukkan lebar: "))), "cm^3")
        elif pilih == "2":
            print("Luas permukaan balok sebesar: ", luasBalok(int(input("Masukkan tinggi: ")), int(input("Masukkan panjang: ")), int(input("Masukkan lebar: "))), "cm^2")
        else:
            volLuasBalok(float(input("Masukkan panjang: ")), float(input("Masukkan lebar: ")), float(input("Masukkan tinggi: ")))

    #Perhitungan untuk kerucut
    elif ruang == "b":
        pilihan()
        pilih = input("Apa yang ingin Anda cari? ")
        print("-"*50)
        if pilih == "1":
            print("Volume kerucut sebesar: ", vKerucut(int(input("Masukkan jari-jari alas: ")),
            int(input("Masukkan tinggi kerucut: "))), "cm^3")
        elif pilih == "2":
            print("Luas permukaan kerucut sebesar: ", lpKerucut(int(input("Masukkan jari-jari alas kerucut: ")),
            int(input("Masukkan garis pelukis: "))), "cm^2")
        else:
            volLuasKerucut(float(input("Masukkan jari-jari alas: ")), float(input("Masukkan tinggi: ")), float(input("Masukkan panjang garis pelukis: ")))

    #Perhitungan untuk bola
    elif ruang == "c":
        pilihan()
        pilih = input("Apa yang ingin dihitung? ")
        print("-"*50)
        if pilih == "1":
            print("Volume bola sebesar: ", volumeBola(float(input("Masukkan jari-jari bola: "))), "cm^3")
        elif pilih == "2":
            print("Luas permukaan bola sebesar: ", luasbola(float(input("Masukkan jari-jari bola: "))), "cm^2")
        else:
            volLuasBola(float(input("Masukkan jari-jari bola: ")))

    #Perhitungan untuk tabung
    elif ruang == "d":
        pilihan()
        pilih = input("Apa yang ingin dihitung? ")
        print("-"*50)
        if pilih == "1":
            print("Volume tabung sebesar: ", volumeTabung(float(input("Masukkan jari-jari alas: ")),
            float(input("Masukkan tinggi tabung: "))), "cm^3")
        elif pilih == "2":
            print("Luas Permukaan tabung sebesar: ", volumeTabung(float(input("Masukkan jari-jari alas: ")),
            float(input("Masukkan tinggi tabung: "))), "cm^3")
        else:
            volLuasTabung(float(input("Masukkan jari-jari alas tabung: ")), float(input("Maukkan tinggi Tabung: ")))
    else:
        print("Maaf, Kami Belum mengetahui rumusnya.")
    return ruang

bangunRuang()
while True:
    lanjut = input("Apakah Lanjut?")
    if lanjut == "yes":
        bangunRuang()
        continue
    if lanjut == "no":
        break
print("Selesai!")

