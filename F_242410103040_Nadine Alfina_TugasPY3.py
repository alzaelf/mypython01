# NADINE ALFINA AZZAHWA
# 242410103040
# KELAS F

# Soal 1
nilai =int(input("Masukkan nilai: ")) #Fungsi input() digunakan untuk meminta pengguna memasukkan data. Dalam hal ini, pengguna diminta untuk "Masukkan nilai: ".
if nilai < 7 or (14 < nilai < 17): #untuk mencari tau apakah input yang di masukkan memenuhi atau tidak
    print(True) 
else:
    print(False)
    
print("--------------")
    
# Soal 2
Nama= input("Masukkan nama: ") #pengguna input nama
rekening = int(input("Masukkan rekening: ")) #pengguna input no rek, harus dalam bentuk angka
saldo = 50000000 #pengguna memiliki limit saldo 50 juta

if Nama == "" and rekening == "" and saldo < 0:
    print("Anda tidak bisa melakukan transaksi") #apakah semua inputan pengguna dalam bentuk yang benar
else:
    penarikan = int(input("Masukkan nominal penarikan : ")) #pengguna memasukkan nominal yang akan diambil
    if penarikan > saldo:
        print("Maaf, Saldo anda tidak cukup") #jika melebihi nilai saldo, tidak akan bisa
    else:
        saldo = saldo - penarikan
        print("Penarikan berhasil, Sisa Saldo anda : ", saldo) #jika saldo mencukupi, maka saldo akan berkurang
   
print("-------------------")     
# Soal 3

barang = ["RAM 16 GB", "GPU RTX 9060", "Casing"] 
hargabarang = [800000, 12000000, 200000] #harga masing masing barang
hargadiskon = [95/100*hargabarang[0], 95/100*hargabarang[1], 95/100*hargabarang[2]] #harga barang otomatis diskon
totalharga = (hargadiskon[0]+hargadiskon[1]+hargadiskon[2]) #total harga seluruh barang
print(f"RAM 16GB: {hargadiskon[0]}")
print(f"GPU RTX 9060: {hargadiskon[1]}")
print(f"Casing: {hargadiskon[2]}")
print(f"total harga: {totalharga}")

voucher = ["H4L0D3K"] #nilai voucher
punya = input("Apakah anda punya voucher? : ") #apakah pengguna punya voucher
if punya == "iya" :  #jika punya
    ada = (input("Masukkan voucher anda: ")) #masukkan voucher
    if ada in voucher :
        print("Selamat anda mendapat diskon tambahan") #jika voucher benar
        totalhargadiskon = totalharga*(97/100)
        print("Total belanja anda: Rp.", totalhargadiskon) #pengguna akan mendapat diskon tambahan
    else:
        print("Voucher tidak ter deteksi") #jika punya voucher tapi salah
else:
    print(f"Total harga barang anda: {totalharga}") #jika tidak punya voucher



        