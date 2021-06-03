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
        if jenis_rawat == "1":
            input("\nNama: ")
            print("Pilihan Poli: ")
            print(" 1. Poli Umum")
            print(" 2. Poli Anak")
            print(" 3. Poli Syaraf")
            print(" 4. Poli Orthopedi")
            menupoli = ["Poli Umum", "Poli Anak", "Poli Syaraf", "Poli Jantung"]

            pilpoli = input("Masukkan Poli yang diinginkan (1/2/3/4): ")
            if pilpoli == "1":
                poli = menupoli[0]
                print("\nDaftar Dokter Poli Umum")
                print(" 1. dr. Surya")
                print(" 2. dr. Hera")
                print(" 3. dr. Dani")
                dafdok = ["dr. Surya", "dr. Hera", "dr. Dani"]
                pildok = input("Silahkan pilih dokter (1/2/3) : ")
                jam = ["12:00", "14:00", "16:00"]
                if pildok == "1":
                    dokter = dafdok[0]
                elif pildok == "2":
                    dokter = dafdok[1]
                elif pildok == "3":
                    dokter = dafdok[2]
                else:
                    print("Pilihan dokter tidak tersedia")

            elif pilpoli == "2":
                poli = menupoli[1]
                print("\nDaftar Dokter Poli Anak")
                print(" 1. dr. Santi")
                print(" 2. dr. Ara")
                print(" 3. dr. Angel")
                dafdok = ["dr. Santi", "dr. Ara", "dr. Angel"]
                pildok = input("Silahkan pilih dokter (1/2/3) : ")
                jam = ["13:00", "14:40", "17:00"]
                if pildok == "1":
                    dokter = dafdok[0]
                elif pildok == "2":
                    dokter = dafdok[1]
                elif pildok == "3":
                    dokter = dafdok[2]
                else:
                    print("Pilihan dokter tidak tersedia")
                    
            elif pilpoli == "3":
                poli = menupoli[2]
                print("\nDaftar Dokter Poli Syaraf")
                print(" 1. dr. Mutiara")
                print(" 2. dr. Richard")
                print(" 3. dr. Naufal")
                dafdok = ["dr. Mutiara", "dr. Richard", "dr. Naufal"]
                pildok = input("Silahkan pilih dokter (1/2/3) : ")
                jam = ["14:10", "16:40", "19:00"]
                if pildok == "1":
                    dokter = dafdok[0]
                elif pildok == "2":
                    dokter = dafdok[1]
                elif pildok == "3":
                    dokter = dafdok[2]
                else:
                    print("Pilihan dokter tidak tersedia")

            elif pilpoli == "4":
                poli = menupoli[3]
                print("\nDaftar Dokter Poli Orthopedi")
                print(" 1. dr. Adib")
                print(" 2. dr. Tejo")
                print(" 3. dr. Alif")
                dafdok = ["dr. Adib", "dr. Tejo", "dr. Alif"]
                pildok = input("Silahkan pilih dokter (1/2/3) : ")
                jam = ["12:30", "15:15", "17:50"]
                if pildok == "1":
                    dokter = dafdok[0]
                elif pildok == "2":
                    dokter = dafdok[1]
                elif pildok == "3":
                    dokter = dafdok[2]
                else:
                    print("Pilihan dokter tidak tersedia")

            else:
                print("Pilihan Poli Tidak Tersedia")
                sys.exit()

            def strukrawat():
                print()
                print("-----------------------------------")
                print("     Rumah Sakit Pasti Sembuh")
                print(" Jl.Bahagia No.76, Jakarta 12930")
                print("-----------------------------------")
                print()
                print("           No Antrian")
                print("              ", random.randint(1, 50))
                print("          ", poli)
                print("          ",  dokter)
                print("          Pukul", random.choice(jam))
                print("  Terima Kasih Atas Kunjungan Anda")
                print("        Semoga Lekas Sembuh")
                print()
                sys.exit()
            print(strukrawat())


        elif jenis_rawat == "2":
            kamar()
