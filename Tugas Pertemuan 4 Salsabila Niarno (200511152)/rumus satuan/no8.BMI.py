#Menghitung body mass index dengan metode BMI
from perhitungan_bmi import bodyMassIndex


print("===Menghitung Body Mass Index==")

#keterangan BMI
print("di bawah 18.5: berat badan kurang")
print("18.5 - 22.9: berat badan normal")
print("23 - 29.9: berat badan berlebih")
print("30 ke atas: obesitas")

bodyMassIndex(int(input("Masukkan berat badan Anda: ")), int(input("Masukkan tinggi badan Anda:")))