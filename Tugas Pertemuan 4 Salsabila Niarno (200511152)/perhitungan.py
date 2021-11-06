import math

def luasPersegi(panjang, lebar):
    luas = panjang * lebar
    return luas

def kelilingPersegi(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    return keliling

def luasKelilingpersegi(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print("Luas Persegi Panjang sebesar: ", luas, "cm^2")
    print("Keliling Persegi Panjang sebesar: ", keliling, "cm^2")

def luasSegitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi #rumus luas Segitiga
    return luas

def kelilingSegitiga(sisi1, sisi2, sisi3):
    keliling = sisi1 + sisi2 + sisi3 #rumus keliling Segitiga
    return keliling
    
def lingkaran(jari):
    luas = math.pi*(jari**2)
    keliling = 2 * math.pi *jari
    print("Luas lingkaran sebesar: ", luas, "cm^2")
    print("Keliling lingkaran sebesar: ", keliling, "cm")

def volBalok(tinggi, panjang, lebar):
    volume_balok = panjang * lebar * tinggi
    return volume_balok

def luasBalok(tinggi, panjang, lebar):
    luas_balok = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    return luas_balok

def vKerucut(r,t):
    volume_kerucut = (1/3) * math.pi * (r**2) * t
    return volume_kerucut

def lpKerucut(r, s):
    luasAlas = math.pi * (r**2)
    luasSelimut = math.pi * r * s
    luas_kerucut = luasAlas + luasSelimut
    return luas_kerucut

def volumeBola(r):
    vbola = (4/3) * math.pi *(r**3)
    return vbola

def luasbola(r):
    luasbola = 4 * math.pi * (r**2)
    return luasbola

def volumeTabung(r, t):
    luas_alas = math.pi * (r**2)
    volume_tabung = luas_alas * t
    return volume_tabung

def luasTabung(r,t):
    luas_alas = math.pi * (r**2) #luas alas (luas lingkaran)
    keliling_alas = 2 * math.pi * r #keliling alas tabung
    luas_tabung = (2 * luas_alas) +  (keliling_alas * t)
    return luas_tabung