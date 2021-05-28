import sys
import os

loop = True

print()
print("\t-------------------------------------------------------------------------------------------------------")
print("\t------------------------------------SELAMAT DATANG DI PROGRAM------------------------------------------")
print("\t-------------------------------------RUMAH SAKIT PASTI SEMBUH------------------------------------------")
print("\t-------------------------------------------------------------------------------------------------------")
print()
print()

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