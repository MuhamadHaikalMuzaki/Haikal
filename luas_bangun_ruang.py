from luas_bangun_ruang_modul import (
    volume_kubus,
    volume_balok,
    volume_tabung,
    volume_limas,
    volume_prisma
)

def hitung_volume():
    print("Pilih bangun ruang yang ingin dihitung volumenya:")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Limas")
    print("5. Prisma")
    
    pilihan = int(input("\nMasukkan nomor pilihan (1-5): "))
    
    if pilihan == 1:
        sisi = float(input("Masukkan panjang sisi kubus: "))
        print("Volume Kubus:", volume_kubus(sisi))
        
    elif pilihan == 2:
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        print("Volume Balok:", volume_balok(panjang, lebar, tinggi))
        
    elif pilihan == 3:
        jari_jari = float(input("Masukkan jari-jari alas tabung: "))
        tinggi = float(input("Masukkan tinggi tabung: "))
        print("Volume Tabung:", volume_tabung(jari_jari, tinggi))
        
    elif pilihan == 4:
        alas = float(input("Masukkan panjang alas limas: "))
        tinggi_alas = float(input("Masukkan tinggi alas limas: "))
        tinggi_limas = float(input("Masukkan tinggi limas: "))
        print("Volume Limas:", volume_limas(alas, tinggi_alas, tinggi_limas))
        
    elif pilihan == 5:
        alas = float(input("Masukkan panjang alas prisma: "))
        tinggi_alas = float(input("Masukkan tinggi alas prisma: "))
        tinggi_prisma = float(input("Masukkan tinggi prisma: "))
        print("Volume Prisma:", volume_prisma(alas, tinggi_alas, tinggi_prisma))
        
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1 sampai 5.")

# Example function call to test
hitung_volume()