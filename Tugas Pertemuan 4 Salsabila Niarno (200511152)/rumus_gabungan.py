from rumus_bangun_datar import *
from rumus_bangun_ruang import *
from perhitungan_bmi import bodyMassIndex

def abc():
    print("a. Luas dan Keliling bangun datar")
    print("b. volume dan luas permukaan bangun ruang")
    print("c. Menghitung BMI")

print("Program Perhitungan menggunakan fungsi".center(50,"="))
abc()
a = bangunDatar()
b = bangunRuang()
c = bodyMassIndex(int(input("Masukkan berat badan Anda: ")), int(input("Masukkan tinggi badan Anda:")))
pilihanmu = input("Masukkan Opsi: ")
if pilihanmu == "a":
    print(a)
elif pilihanmu == "b":
    print(b)
elif pilihanmu == "c":
    print(c)
else:
    print("Maaf, tidak ada opsi tersebut")
    
    






