#NADINE ALFINA AZZAHWAA
#242410103040
# KELAS F
# SOAL 1

print('-'*60)
print(" "* 25,'SOAL 1')
print('-'*60)
 
harga1 = 100000
harga2 = 30000
    
JenisMakanan = input('''
1. Makanan Utama
2. Makanan Penutup

(1 / 2)? : ''')
jumlah = int(input("anda pesan berapa? "))

if JenisMakanan == '1':
    hargautama = harga1    
if JenisMakanan == '2':
    hargautama= harga2
    
hargaakhir= hargautama*jumlah
    
Membership = input("Anggota loyal? ( True / False ) : ").lower() == "true"
print('-'*60)
    
if Membership:
    hargadiskon = hargaakhir * 0.10
    hargaakhir = hargaakhir - hargadiskon 
else:
    hargaakhir
    
if jumlah > 2 :
    hargaakhir = hargaakhir * 1.15
    
print("baik anda harus membayar sebesar: Rp.", hargaakhir)

        
# Soal 2

print('-'*60)
print(" "* 25,'SOAL 2')
print('-'*60)

ipk = float(input('masukkan ipk :'))
ekstra = int(input('masukkan jumlah kegiatan ekstra: '))

if ipk >= 3.5:
    print('SELAMAT ANDA MENDAPATKAN BEASISWA PENUH')
elif 3.0 < ipk < 3.5 and ekstra > 2:
    print('SELAMAT ANDA BERHAK MENDAPATKAN BEASISWA SEBAGIAN')
else:
    print('anda tidak cukup keren, sehingga tidak bisa mendapat beasiswa')
    
         
 
 
#  Soal 3:

print('-'*60)
print(" "* 24,'SOAL 3')
print('-'*60)

Nilai = float(input('masukkan nilai :'))
Kehadiran = float(input('masukkan persentase kehadiran :'))

if Nilai >= 80 and Kehadiran >= 75:
    print('Nilai Akhir anda adalah : A')
elif Nilai >= 70 and Kehadiran >= 50:
    print('Nilai Akhir anda adalah : B')
else:
    print('Nilai Akhir anda adalah : C')
    





