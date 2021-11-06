import math

def luasKelilingpersegi(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print("Luas Persegi Panjang sebesar: ", luas, "cm^2")
    print("Keliling Persegi Panjang sebesar: ", keliling, "cm")

def luasKelilingSegitiga(alas,tinggi,sisi1,sisi2,sisi3):
    luas = 0.5 * alas * tinggi
    keliling = sisi1 + sisi2 + sisi3
    print("Luas Segitiga sebesar: ", luas, "cm^2")
    print("Keliling Segitiga sebesar: ", keliling, "cm")

def volLuasBalok(panjang, lebar, tinggi):
    volume_balok = panjang * lebar * tinggi
    luas_balok = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    print("Volume Balok: ", volume_balok, "cm^3")
    print("Volume Balok: ", luas_balok, "cm^2")

def volLuasKerucut(r,t,s):
    volume_kerucut = (1/3) * math.pi * (r**2) * t
    luasAlas = math.pi * (r**2)
    luasSelimut = math.pi * r * s
    luas_kerucut = luasAlas + luasSelimut
    print("Volume kerucut: ", volume_kerucut, "cm^3")
    print("Luas permukaan kerucut: ", luas_kerucut, "cm^2")

def volLuasBola(r):
    vbola = (4/3) * math.pi *(r**3)
    luasbola = 4 * math.pi * (r**2)
    print("Volume Bola: ", vbola, "cm^3")
    print("Luas permukaan kerucut: ", luasbola, "cm^2")

def volLuasTabung(r, t):
    luas_alas = math.pi * (r**2)
    volume_tabung = luas_alas * t
    luas_alas = math.pi * (r**2) #luas alas (luas lingkaran)
    keliling_alas = 2 * math.pi * r #keliling alas tabung
    luas_tabung = (2 * luas_alas) +  (keliling_alas * t)
    print("Volume tabung: ", volume_tabung, "cm^3")
    print("Luas permukaan kerucut: ", luas_tabung, "cm^2")