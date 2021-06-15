import sys
import os
import random
import pandas as pd

loop = True


def pembayaran():
    print("\nForm Pembayaran")
    print("jenis Pembayaran")
    print(" 1. BPJS")
    print(" 2. Tunai")
    pilbayar = ["BPJS", "Tunai"]
    jbayar = input("Pilih jenis pembayaran (1/2): ")

    if jbayar == "1":
        print("\nIsikan data berikut")
        nama_pasien = input("Nama: ")
        no_bpjs = int(input("No BPJS: "))
        ttl_pasien = input("Tempat, Tanggal Lahir: ")
        nik = int(input("NIK: "))
        byr = pilbayar[0]
        jumlah_bayar = tagihan
        bayarnya = tagihan
        bayar_apa = pay
        Loop = 0
        kembalian = 0


    elif jbayar == "2":
        byr = pilbayar[1]
        jumlah_bayar = tagihan
        bayar_apa = pay
        nama_pasien = 0
        no_bpjs = 0
        ttl_pasien = 0
        nik = 0

        Loop = True

        while Loop == True:
            try:
                fee = print("Total Tagihan Anda adalah Rp", jumlah_bayar)
                bayarnya = int(input("Masukkan jumlah uang anda: "))
                kembalian = bayarnya - jumlah_bayar
                kembali = abs(kembalian)

            except:
                print("Maaf, Uang anda kurang sebesar Rp ", kembali)

            else:
                if kembalian > 0:
                    break
                elif kembalian == 0:
                    break
                elif kembalian < 0:
                    print("Maaf, Uang anda kurang sebesar Rp ", kembali)


    return bayarnya, byr, jumlah_bayar, kembalian, bayar_apa, nama_pasien, no_bpjs, ttl_pasien, nik, jbayar, Loop


def strukbyr(bayarnya, byr, jumlah_bayar, kembalian, bayar_apa, nama_pasien, no_bpjs, ttl_pasien, nik, jbayar):
    print()
    print("-----------------------------------")
    print("     Rumah Sakit Pasti Sembuh")
    print(" Jl.Bahagia No.76, Jakarta 12930")
    print("-----------------------------------")
    print()
    print("            Struk Pembayaran")
    print()
    print(" Pembayaran      : ", bayar_apa)
    print(" Jenis Bayar     : ", byr)
    if jbayar == "1":
        print(" Nama Pasien     : ", nama_pasien)
        print(" No BPJS         : ", no_bpjs)
        print(" TTL             : ", ttl_pasien)
        print(" NIK             : ", nik)
    print(" Total Tagihan   : ", jumlah_bayar)
    print()
    print(" Pembayaran      : ", bayarnya)
    print(" Kembali         : ", kembalian)
    print()
    print("  Terima Kasih Atas Kunjungan Anda")
    print("        Semoga Lekas Sembuh")
    print()
    
  

while loop:

    try:
        print()
        print(
            "\t-------------------------------------------------------------------------------------------------------")
        print(
            "\t------------------------------------SELAMAT DATANG DI PROGRAM------------------------------------------")
        print(
            "\t-------------------------------------RUMAH SAKIT PASTI SEMBUH------------------------------------------")
        print(
            "\t---------------------------------Jl.Bahagia No.76, Jakarta 12930---------------------------------------")
        print(
            "\t-------------------------------------------------------------------------------------------------------")
        print()
        print()

        print("Daftar Menu: ")
        print("\t1. Pendataan pasien dan berkas")
        print("\t2. Pendaftaran antrian")
        print("\t3. Pilihan ambil dan antar obat")
        print("\t4. Ketersediaan kamar pasien")
        pilihan_fitur = str(input("Silahkan pilih fitur yang diinginkan [1/2/3/4] : "))

    except:
        print("Pilihan Menu Tidak Tersedia")

    else:
        if pilihan_fitur == "1":
            os.system('cls')
            print("\nFitur Pendataan Pasien")
            file = "Data_Pasien.xlsx"
            Data_Pasien = pd.read_excel(file)
            df = pd.DataFrame(Data_Pasien)

            print("Silahkan Masukkan data pasien")
            nama = input("Nama Pasien: ")
            jkelamin = input("Jenis Kelamin (l/p): ")
            usia = int(input("Usia: "))
            alamat = input("Alamat: ")
            ktp = int(input("No KTP: "))
            ttl = input("Tempat, Tanggal Lahir: ")
            konkerabat = input("Kontak kerabat: +62 ")
            if len(konkerabat) != 10 and len(konkerabat) != 11:
                os.system('cls')
                print('No Hp Anda tidak terdaftar')
                continue

            df.loc[len(df.index)] = [len(df) + 1, nama, jkelamin, usia, alamat, ktp, ttl, konkerabat]
            export = pd.ExcelWriter(file)
            df.to_excel(export, index=False)
            export.save()
            print("Data pasien telah tersimpan")

            ulang = str(input("Apakah anda ingin keluar dari program (Y/T)"))
            if ulang.upper() == "Y":
                print("\nTerima Kasih sudah menggunakan jasa rumah sakit kami")
                print("Semoga Lekas Sembuh")
                sys.exit()
            else:
                continue


        elif pilihan_fitur == "2":
            os.system('cls')
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
                        sys.exit()

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
                        sys.exit()

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
                        sys.exit()

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
                        sys.exit()

                else:
                    print("Pilihan Poli Tidak Tersedia")
                    sys.exit()


                tagihan = 150000
                pay = "Rawat Jalan"
