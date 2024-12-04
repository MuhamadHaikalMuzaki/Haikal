import math

def luas_lingkaran(jari_jari):
    return math.pi * math.pow(jari_jari, 2)

def luas_persegi(sisi):
    return sisi * sisi

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi