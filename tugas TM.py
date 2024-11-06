#NADINE ALFINA AZZAHWA
#242410103040
# KELAS F


# Soal 1: Sistem Diskon Restoran
# Seorang pelanggan di restoran ingin mengetahui harga akhir dari makanannya berdasarkan jenis makanan yang 
# dipesan dan apakah pelanggan tersebut anggota loyal. Berikut adalah kriteria harga:
# Makanan utama: Rp100.000
# Makanan penutup: Rp30.000
# Diskon 10% untuk anggota loyal
# Tambahan biaya 15% jika pelanggan memesan lebih dari 2 jenis makanan
# Buatlah program untuk menghitung total harga berdasarkan kriteria di atas!
# Input:
# Jenis Makanan (Makanan Utama/Makanan Penutup)
# Jumlah Makanan
# Anggota Loyal (True/False)
print('-'*60)
print(" "* 25,'SOAL 1')
print('-'*60)
    
JenisMakanan = input('''
1. Makanan Utama
2. Makanan Penutup

(1 / 2)? : ''')
punyaMembership = input('Anggota loyal? \n( True / False ) : ')
print('-'*60)

if JenisMakanan == '1':
    JumlahMakananUtama = int(input('Jumlah pesanan : '))
    if punyaMembership == True:
        if JumlahMakananUtama > 2:
            totalbiaya = (JumlahMakananUtama * 100000) * 0.90 * 1.15 # jumlah dengan biaya tambahan 15% dan diskon 80%
            print(f'total biaya adalah : {totalbiaya}') 
        else:
            totalbiaya = (JumlahMakananUtama * 100000) * 0.90 # jumlah tanpa biaya tambahan tapi dengan diskon
            print(f'total biaya adalah : {totalbiaya}') 
    else:
        totalbiaya = (JumlahMakananUtama * 100000) # biaya akhir tanpa diskon dan pesanan kurang dari 1
        print(f'total biaya adalah : {totalbiaya}') 
        

elif JenisMakanan == '2':
    JumlahMakananPenutup = int(input('Jumlah pesanan : '))
    if punyaMembership == True:
        if JumlahMakananPenutup > 2:
            totalbiaya = (JumlahMakananPenutup * 30000) * 0.90 * 1.15 # jumlah dengan biaya tambahan 15% dan diskon 80%
            print(f'total biaya adalah : {totalbiaya}') 
        else:
            totalbiaya = (JumlahMakananPenutup * 30000) * 0.90 # jumlah tanpa biaya tambahan tapi dengan diskon
            print(f'total biaya adalah : {totalbiaya}') 
    else:
        totalbiaya = (JumlahMakananPenutup * 30000) # biaya akhir tanpa diskon dan pesanan kurang dari 1
        print(f'total biaya adalah : {totalbiaya}') 
     
else:
    print('input salah!')
        
# Soal 2: Sistem Penerimaan Beasiswa
# Sistem penerimaan beasiswa menentukan apakah seorang mahasiswa berhak mendapatkan beasiswa berdasarkan IPK dan jumlah kegiatan ekstrakurikuler:
# IPK ≥ 3.5: Berhak mendapatkan beasiswa penuh
# IPK antara 3.0 dan 3.5: Berhak mendapatkan beasiswa sebagian jika jumlah kegiatan ekstrakurikuler > 2
# IPK < 3.0: Tidak berhak mendapatkan beasiswa
# Buatlah program untuk menentukan status beasiswa mahasiswa!
# Input:
# IPK
# Jumlah Kegiatan

print('-'*60)
print(" "* 25,'SOAL 2')
print('-'*60)

ipk = int(input('masukkan ipk :'))
ekstra = input('masukkan jumlah kegiatan ekstra')

if ipk >= 3.5:
    print('SELAMAT ANDA MENDAPATKAN BEASISWA PENUH')
elif 3.0 < ipk < 3.5 and ekstra > 2:
    print('SELAMAT ANDA BERHAK MENDAPATKAN BEASISwA SEBAGIAN')
else:
    print('anda tidak keren dan tidak berhak mendapat beasiswa')
    
         
 
 
#  Soal 3: Sistem Penilaian Ujian
# Sistem penilaian ujian menentukan nilai akhir berdasarkan nilai ujian dan kehadiran. Aturan penilaian adalah sebagai berikut:
# Nilai Ujian ≥ 80 dan Kehadiran ≥ 75%: A
# Nilai Ujian ≥ 70 dan Kehadiran ≥ 50%: B
# Nilai Ujian < 70: C
# Jika kehadiran < 50%: Nilai langsung D
# Buatlah program untuk menentukan grade mahasiswa berdasarkan kriteria di atas!
# Input:
# Nilai Ujian
# Kehadiran (dalam persen)

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
    s