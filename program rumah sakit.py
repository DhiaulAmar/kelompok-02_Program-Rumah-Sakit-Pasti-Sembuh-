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
    
