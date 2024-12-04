import math

def volume_kubus(sisi):
    return math.pow(sisi, 3)

def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def volume_tabung(jari_jari, tinggi):
    return math.pi * math.pow(jari_jari, 2) * tinggi

def volume_limas(alas, tinggi_alas, tinggi_limas):
    luas_alas = 0.5 * alas * tinggi_alas
    return (1/3) * luas_alas * tinggi_limas

def volume_prisma(alas, tinggi_alas, tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi_alas
    return luas_alas * tinggi_prisma