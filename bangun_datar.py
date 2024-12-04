from bangun_datar_modul import (
    luas_lingkaran,
    luas_persegi,
    luas_segitiga,
    luas_persegi_panjang,
    luas_jajar_genjang
)

def hitung_luas():
    print("Pilih bangun datar yang ingin dihitung luasnya:")
    print("1. Lingkaran")
    print("2. Persegi")
    print("3. Segitiga")
    print("4. Persegi Panjang")
    print("5. Jajar Genjang")
    
    pilihan = int(input("\nMasukkan nomor pilihan (1-5): "))
    
    if pilihan == 1:
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        print("Luas Lingkaran:", luas_lingkaran(jari_jari))
        
    elif pilihan == 2:
        sisi = float(input("Masukkan panjang sisi persegi: "))
        print("Luas Persegi:", luas_persegi(sisi))
        
    elif pilihan == 3:
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        print("Luas Segitiga:", luas_segitiga(alas, tinggi))
        
    elif pilihan == 4:
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        print("Luas Persegi Panjang:", luas_persegi_panjang(panjang, lebar))
        
    elif pilihan == 5:
        alas = float(input("Masukkan panjang alas jajar genjang: "))
        tinggi = float(input("Masukkan tinggi jajar genjang: "))
        print("Luas Jajar Genjang:", luas_jajar_genjang(alas, tinggi))
        
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1 sampai 5.")

# Example function call to test
hitung_luas()