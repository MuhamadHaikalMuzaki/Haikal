from aritmatika_modul import tambah, kurang, kali, bagi, pangkat  # Importing functions correctly

def hitungan_aritmatika():
    print("Pilih operasi aritmatika yang ingin dilakukan:")
    print("1. Penambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")
    
    pilihan = int(input("\nMasukkan nomor operasi aritmatika yang dipilih (1-5): "))
    
    if pilihan == 1:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil penambahan:", tambah(a, b))
        
    elif pilihan == 2:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil pengurangan:", kurang(a, b))
        
    elif pilihan == 3:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil perkalian:", kali(a, b))
        
    elif pilihan == 4:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil pembagian:", bagi(a, b))
        
    elif pilihan == 5:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan eksponen (angka pangkat): "))
        print("Hasil pangkat:", pangkat(a, b))
        
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1 sampai 5.")

# Example function call to test
hitungan_aritmatika()
