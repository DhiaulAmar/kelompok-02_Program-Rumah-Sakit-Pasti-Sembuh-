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
                    print("          ", dokter)
                    print("          Pukul", random.choice(jam))
                    print("  Terima Kasih Atas Kunjungan Anda")
                    print("        Semoga Lekas Sembuh")
                    print()


                strukrawat()

                bayarnya, byr, jumlah_bayar, kembalian, bayar_apa, nama_pasien, no_bpjs, ttl_pasien, nik, jbayar, Loop = pembayaran()
                strukbyr(bayarnya, byr, jumlah_bayar, kembalian, bayar_apa, nama_pasien, no_bpjs, ttl_pasien, nik,
                         jbayar)


            elif jenis_rawat == "2":
                os.system('cls')
                print("\nPilihan kelas kamar: ")
                print("\t1. Kelas 3")
                print("\t2. Kelas 2")
                print("\t3. Kelas 1")
                print("\t4. Kelas VIP")
                pilihan_kamar = input("Silahkan pilih jenis kamar (1/2/3/4): ")
                dafkam = ["Kelas 3", "Kelas 2", "Kelas 1", "Kelas VIP"]
                harkam = [200000, 375000, 550000, 725000]

                if pilihan_kamar == "1":
                    harga_kamar = harkam[0]
                    print("\nKamar Tersedia")
                    print("Harga kamar kelas 3 : Rp", harkam[0])
                    print("Pembayaran hanya untuk DP awal")
                    print("Silahkan menuju loket untuk melakukan pembayaran awal")

                elif pilihan_kamar == "2":
                    harga_kamar = harkam[1]
                    print("\nKamar Tersedia")
                    print("Harga kamar kelas 2 : Rp", harkam[1])
                    print("Pembayaran hanya untuk DP awal")
                    print("Silahkan menuju loket untuk melakukan pembayaran awal")

                elif pilihan_kamar == "3":
                    harga_kamar = harkam[2]
                    print("\nKamar Tersedia")
                    print("Harga kamar kelas 1 : Rp", harkam[2])
                    print("Pembayaran hanya untuk DP awal")
                    print("Silahkan menuju loket untuk melakukan pembayaran awal")

                elif pilihan_kamar == "4":
                    harga_kamar = harkam[3]
                    print("\nKamar Tersedia")
                    print("Harga kamar kelas VIP : Rp", harkam[3])
                    print("Pembayaran hanya untuk DP awal")
                    print("Silahkan menuju loket untuk melakukan pembayaran awal")

                else:
                    print("Pilihan kamar tidak tersedia")
                    sys.exit()


                tagihan = harga_kamar
                pay = "Rawat Inap"

                bayarnya, byr, jumlah_bayar, kembalian, bayar_apa, nama_pasien, no_bpjs, ttl_pasien, nik, jbayar, Loop = pembayaran()
                strukbyr(bayarnya, byr, jumlah_bayar, kembalian, bayar_apa, nama_pasien, no_bpjs, ttl_pasien, nik,
                         jbayar)

            ulang = str(input("Apakah anda ingin keluar dari program (Y/T)"))
            if ulang.upper() == "Y":
                print("\nTerima Kasih sudah menggunakan jasa rumah sakit kami")
                print("Semoga Lekas Sembuh")
                sys.exit()
            else:
                continue


        elif pilihan_fitur == "3":
            os.system('cls')
            print("\nFitur Ambil Antar Obat")
            print("Silahkan isi data berikut")
            nama = input("Nama: ")
            print("Daftar Obat: ")
            print(" 1. Amoxilin             6. Dexanta              11. Panadol")
            print(" 2. Alergine             7. Dulcolax             12. Paratusin")
            print(" 3. Asam Mefenamat       8. Histapan             13. Ranitidine Hexpharm")
            print(" 4. Cetrizine            9. Imbost force         14. Salbutamol")
            print(" 5. Combantrin          10. Nalgestan            15. Voltadex")
            pilobat = input("Pilih obat yang diinginkan (1/2/3...): ")
            dafobat = ["Amoxilin", "Alergine", "Asam Mefenamat", "Cetrizine ", "Combantrin",
                       "Dexanta", "Dulcolax", "Histapan", "Imbost force", "Nalgestan",
                       "Panadol", "Paratusin", "Ranitidine Hexpharm", "Salbutamol", "Voltadex"]
            harobat = [3700, 44500, 2800, 6000, 14500,
                       5000, 8500, 8100, 70000, 9000,
                       10000, 10000, 1600, 1600, 15000]

            if pilobat == "1":
                obat = dafobat[0]
                harga_obat = harobat[0]
            elif pilobat == "2":
                obat = dafobat[1]
                harga_obat = harobat[1]
            elif pilobat == "3":
                obat = dafobat[2]
                harga_obat = harobat[2]
            elif pilobat == "4":
                obat = dafobat[3]
                harga_obat = harobat[3]
            elif pilobat == "5":
                obat = dafobat[4]
                harga_obat = harobat[4]
            elif pilobat == "6":
                obat = dafobat[5]
                harga_obat = harobat[5]
            elif pilobat == "7":
                obat = dafobat[6]
                harga_obat = harobat[6]
            elif pilobat == "8":
                obat = dafobat[7]
                harga_obat = harobat[7]
            elif pilobat == "9":
                obat = dafobat[8]
                harga_obat = harobat[8]
            elif pilobat == "10":
                obat = dafobat[9]
                harga_obat = harobat[9]
            elif pilobat == "11":
                obat = dafobat[10]
                harga_obat = harobat[10]
            elif pilobat == "12":
                obat = dafobat[11]
                harga_obat = harobat[11]
            elif pilobat == "13":
                obat = dafobat[12]
                harga_obat = harobat[12]
            elif pilobat == "14":
                obat = dafobat[13]
                harga_obat = harobat[13]
            elif pilobat == "15":
                obat = dafobat[14]
                harga_obat = harobat[14]
            else:
                print("Obat Tidak Tersedia")
                sys.exit()

                kuantitas = int(input("Masukkan jumlah obat yang diinginkan: "))
            totalobat = harga_obat * kuantitas

            print("Pilihan ")
            print(" 1. Diambil")
            print(" 2. Diantar (Jabodetabek)")
            amantar = input("Apakah obat ingin diambil atau diantar (1/2): ")
            if amantar == "1":
                print("\nFitur Pengambilan Obat")
                tglobat = input("Masukkan tanggal pengambilan obat (dd-mm-yy): ")
                jamobat = input("Masukkan waktu pemgambilan obat (contoh = 13:00): ")
                print()
                print()
                print("-----------------------------------")
                print("     Rumah Sakit Pasti Sembuh")
                print(" Jl.Bahagia No.76, Jakarta 12930")
                print("-----------------------------------")
                print("      Struk Pengambilan Obat")
                print()
                print("       Nama Pemesan: ", nama)
                print("       Nama Obat: ", obat)
                print("       Harga: ", totalobat)
                print(" Tanggal Pengambilan: ", tglobat)
                print("          Pukul ", jamobat)
                print("             Loket", random.randint(1, 5))
                print(" Terima Kasih Atas Kunjungan Anda")
                print("        Semoga Lekas Sembuh")
                print()

                tagihan = totalobat
                pay = "Pengambilan Obat"

            elif amantar == "2":
                print("\nFitur Pengantaran Obat")
                print("Pilih daerah pengantaran: ")
                print(" 1. Jakarta")
                print(" 2. Bogor")
                print(" 3. Depok")
                print(" 4. Tangerang")
                print(" 5. Bekasi")
                bantar = [10000, 35000, 20000, 250000, 22000]
                daerah = input("Masukkan daerah tempat tinggal Anda (1/2/3/4): ")
                if daerah == "1":
                    biaya_antar = bantar[0]
                    print("Biaya antar: Rp10.000")
                    alamat = input("Masukkan alamat lengkap: ")
                elif daerah == "2":
                    biaya_antar = bantar[1]
                    print("Biaya antar: Rp35.000")
                    alamat = input("Masukkan alamat lengkap: ")
                elif daerah == "3":
                    biaya_antar = bantar[2]
                    print("Biaya antar: Rp20.000")
                    alamat = input("Masukkan alamat lengkap: ")
                elif daerah == "4":
                    biaya_antar = bantar[3]
                    print("Biaya antar: Rp25.000")
                    alamat = input("Masukkan alamat lengkap: ")
                elif daerah == "5":
                    biaya_antar = bantar[4]
                    print("Biaya antar: Rp22.000")
                    alamat = input("Masukkan alamat lengkap: ")
                else:
                    print("Daerah Tidak Tersedia ")
                    biaya_antar = 0
                    sys.exit()


                tagihan = totalobat + biaya_antar
                pay = "Pengantaran Obat"

            
