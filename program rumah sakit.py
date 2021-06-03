import sys
import os
import random

loop = True

print()
print("\t-------------------------------------------------------------------------------------------------------")
print("\t------------------------------------SELAMAT DATANG DI PROGRAM------------------------------------------")
print("\t-------------------------------------RUMAH SAKIT PASTI SEMBUH------------------------------------------")
print("\t---------------------------------Jl.Bahagia No.76, Jakarta 12930---------------------------------------")
print("\t-------------------------------------------------------------------------------------------------------")
print()
print()

def kamar():
    print("\nPilihan kelas kamar: ")
    print("\t1. Kelas 3")
    print("\t2. Kelas 2")
    print("\t3. Kelas 1")
    print("\t4. Kelas VIP")
    pilihan_kamar = input("Silahkan pilih jenis kamar: ")
    dafkam = ["Kelas 3", "Kelas 2", "Kelas 1", "Kelas VIP"]

    harga3 = 200000
    harga2 = 375000
    harga1 = 550000
    hargavip = 725000

    if pilihan_kamar == "1":
        print("Harga kamar kelas 3 : Rp", harga3)
    elif pilihan_kamar == "2":
        print("Harga kamar kelas 3 : Rp", harga2)
    elif pilihan_kamar == "3":
        print("Harga kamar kelas 3 : Rp", harga1)
    elif pilihan_kamar == "4":
        print("Harga kamar kelas 3 : Rp", hargavip)
    else:
        print("Pilihan kamar tidak tersedia")
        sys.exit()

print("Daftar menu:")
print("\t1. Pendataan pasien dan berkas")
print("\t2. Pendaftaran antrian")
print("\t3. Pilihan ambil dan antar obat")
print("\t4. Ketersediaan kamar pasien")

pilihan_fitur = str(input("Silahkan pilih fitur yang diinginkan [1/2/3/4] : "))
while loop:
    if pilihan_fitur == "1":
        print("\nSilahkan Masukkan data pasien")
        nama = input("Nama Pasien: ")
        jkelamin = input("Jenis Kelamin (l/p): ")
        usia = int(input("Usia: "))
        alamat = input("Alamat: ")
        ktp = int(input("No KTP: "))
        ttl = input("Tempat/Tanggal Lahir: ")
        konkerabat = input("Kontak kerabat: +62 ")
        if len(konkerabat) != 10 and len(konkerabat) != 11:
            os.system('cls')
            print('No Hp Anda tidak terdaftar')
            continue
        print("Data pasien telah tersimpan")
        sys.exit()

    elif pilihan_fitur == "2":
        print("\nJenis Rawat")
        print(" 1. Rawat Jalan")
        print(" 2. Rawat Inap")

        jenis_rawat = str(input("Silahkan pilih jenis rawat yang di inginkan [1/2] : "))
