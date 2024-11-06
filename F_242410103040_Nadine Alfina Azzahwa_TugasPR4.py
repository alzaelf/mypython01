print ("""
       Nama : Nadine Alfina Azzahwa
       NIM  : 242410103040
       Kelas: F
       Prodi: Informatika
       """)
print ('<===============================>')


# SOAL 1
# Daftar barang dan harga
nama_barang = ["Beras", "Gula", "Minyak", "Daging", "Telur", "Susu", "Roti", "Sayur", "Buah", "Ikan"]
harga_barang = [10000, 12000, 15000, 30000, 20000, 15000, 5000, 5000, 10000, 20000]

def show_price(nama_barang, harga_barang): #jika pengguna memilih lihat harga
    print("\nDaftar Harga Produk:")
    for i in range(len(nama_barang)): #menghitung masing masing elemen di dalam list dan urut sesuai urutan
        print(f"{nama_barang[i]}: Rp {harga_barang[i]}") #menampilkan nama barang dan harga barang

def purchase (nama_barang, harga_barang): #jika pengguna memilih pembelian
    show_price(nama_barang, harga_barang) #akan ditampilkan kembali nama dan harga barang
    
    produk = input("Kamu mau beli apa?: ").lower() # Meminta input dari pengguna
    nama_barang_lower = [item.lower() for item in nama_barang] # Mengubah semua nama barang menjadi huruf kecil untuk perbandingan
    if produk not in nama_barang_lower: #Memastikan nama produk benar atau tidak
        print("Produk tidak ditemukan. Silakan masukkan nama produk yang valid.") #jika tidak maka akan kembali ke menu awal
        return
    
    jumlah = int(input("kamu mau beli berapa?: ")) #jika inputan nama benar, akan dilanjutkan meminta inputan jumlah barang
    index = nama_barang_lower.index(produk) #memanggil harga produk
    total_harga = harga_barang[index] * jumlah #mengalikan harga produk dengan jumlah barang
    
    print("\nTOKO VIAN CABANG MARS")
    print("\n*****************************")
    print(f"\nNama Pembeli: {user_name}")
    print(f"Jumlah {produk} yang dibeli: {jumlah}")
    print(f"Total harga: Rp {total_harga}")

def main(): #titik dimulai program
    global user_name
    user_name = input(" Halo, silahkan masukkan nama kamu ya: ") #pengguna memasukkan input sebelum mengakses menu
    
    while True:  #akan menampilkan pilihan menu terus menerus kecuali dia keluar
        print("\nMenu:")
        print("1. Lihat Harga")
        print("2. Pembelian")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == '1':
            show_price(nama_barang, harga_barang) #jika pengguna ingin melihat harga akan ditampilkan nama dan harga
        elif pilihan == '2': 
            purchase(nama_barang, harga_barang) #jika pengguna ingin melakukan pembelian akan ditampilkan nama dan harga
        elif pilihan == '3':
            print("Terima kasih telah berkunjung di toko vian, hehe.")
            break #jika pengguna ingin keluar maka sistem akan stop proses perulangan
        else: #jika pengguna tidak memasukkan angka 1-3
            print("Masukkan angka yang benar, hanya ada angka 1,2 dan 3!.")

# Menjalankan program
main()

print ('\n<===============================>')
# Soal 2
# digunakan function untuk memisahkan blok kode masing-masing luas bangun datar
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar #rumus luas persegi panjang

def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi #rumus jajar genjang

def luas_persegi(sisi):
    return sisi ** 2 #rumus persegi

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi #rumus segitiga

def luas_lingkaran(jari_jari):
    phi = 3.14 #membuat variable phi dengan nilai 3.14
    return phi * (jari_jari ** 2) #rumus lingkaran

def main(): #titik awal program dimulai
    while True: #akan terus mengulang selama keadaan benar 
        print("\nHalo, kamu mau ngitung apa nih? ") #tampilan awal program
        print("1. Persegi Panjang")
        print("2. Jajar Genjang")
        print("3. Persegi")
        print("4. Segitiga")
        print("5. Lingkaran")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ") #meminta input pengguna atas pilihan yang tersedia

        if pilihan == '1': #jika pengguna ingin menghitung persegi panjang
            try:
                panjang = float(input("Masukkan panjang: ")) #pengguna diminta untuk menginput angka yang akan dihitung, tidak harus bilangan bulat
                lebar = float(input("Masukkan lebar: "))
                print(f"Luas Persegi Panjang: {luas_persegi(panjang, lebar)}") #menampilkan hasil operasi sesuai rumus bangun datar
            except ValueError: #jika pengguna tidak memasukkan input angka, maka tidak akan bisa dijalankan operasi
                print("Input yang anda masukkan tidak benar, Sistem hanya menerima input angka!")

        elif pilihan == '2': #jika pengguna ingin menghitung jajar genjang
            try:
                alas = float(input("Masukkan alas: ")) #pengguna diminta untuk menginput angka yang akan dihitung, tidak harus bilangan bulat
                tinggi = float(input("Masukkan tinggi: "))
                print(f"Luas Jajar Genjang: {luas_jajar_genjang(alas, tinggi)}") #menampilkan hasil operasi sesuai rumus bangun datar
            except ValueError: #jika pengguna tidak memasukkan input angka, maka tidak akan bisa dijalankan operasi
                print("Input yang anda masukkan tidak benar, Sistem hanya menerima input angka!")

        elif pilihan == '3': #jika pengguna ingin menghitung persegi
            try:
                sisi = float(input("Masukkan sisi: "))#pengguna diminta untuk menginput angka yang akan dihitung, tidak harus bilangan bulat
                print(f"Luas Persegi: {luas_persegi(sisi)}") #menampilkan hasil operasi sesuai rumus bangun datar
            except ValueError: #jika pengguna tidak memasukkan input angka, maka tidak akan bisa dijalankan operasi
                print("Input yang anda masukkan tidak benar, Sistem hanya menerima input angka!")

        elif pilihan == '4': #jika pengguna ingin menghitung segitiga
            try:
                alas = float(input("Masukkan alas: ")) #pengguna diminta untuk menginput angka yang akan dihitung, tidak harus bilangan bulat
                tinggi = float(input("Masukkan tinggi: "))
                print(f"Luas Segitiga: {luas_segitiga(alas, tinggi)}") #menampilkan hasil operasi sesuai rumus bangun datar
            except ValueError: #jika pengguna tidak memasukkan input angka, maka tidak akan bisa dijalankan operasi
                print("Input yang anda masukkan tidak benar, Sistem hanya menerima input angka!")

        elif pilihan == '5': #jika pengguna ingin menghitung lingkaran
            try:
                jari_jari = float(input("Masukkan jari-jari: ")) #pengguna diminta untuk menginput angka yang akan dihitung, tidak harus bilangan bulat
                print(f"Luas Lingkaran: {luas_lingkaran(jari_jari)}") #menampilkan hasil operasi sesuai rumus bangun datar
            except ValueError: #jika pengguna tidak memasukkan input angka, maka tidak akan bisa dijalankan operasi
                print("Input yang anda masukkan tidak benar, Sistem hanya menerima input angka!")

        elif pilihan == '6': #jika pengguna memilih keluar
            print("Terima kasih! Semoga program ini membantu kamu ya :)") #menampilkan ini jika pengguna akan keluar
            break #program akan berhenti jika pengguna memilih keluar

        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-6.") #tdak bisa jika pilihan tidak antara 1-6

# Menjalankan program
main()

print('\n<===============================>')
# Soal 3

def pola_belah_ketupat(size):
    # Mencetak bagian atas belah ketupat yaitu baris 1-5
    for i in range(size): # mengulangi blok kode sampai di range size, misal size 5 maka range angkanya nya yaitu 0 sampai 4
        if i == 0: #untuk awal, karena i dimulai dari 0
            print(' ' * (size - i - 1) + '*')  # Baris pertama hanya satu bintang di tengah, karena spasi dikali kan dengan 4(hasil operasi) lalu baru muncul bintang
        else: #dilanjutan dengan i selanjutnya sampai range 4
            print(' ' * (size - i - 1) + '*' + ' ' * (2 * i - 1) + '*')  # dengan nilai i yang semakin bertambah maka spasi depan akan berkurang setiap perulangan dan spasi tengah bertambah banyak, disini ada 2 bintang untuk membentuk pola

    # Mencetak bagian bawah belah ketupat yaitu baris 6-9
    for i in range(size - 2, -1, -1): #jika size 5 maka range dimulai sari 3 dan berhenti sebelum -1(yaitu 0) dan dengan setiap iterasi nilainya berkurang -1
        if i == 0: #jika range 0
            print(' ' * (size - i - 1) + '*')  # Baris terakhir hanya satu bintang di tengah yang menjadi penutup dari pola
        else: #jika range tidak 0 maka akan dijalankan kode ini
            print(' ' * (size - i - 1) + '*' + ' ' * (2 * i - 1) + '*')  # dimulai dari range 3, jadi spasi awal 1, lalu bintang lalu spasi 5 dan diakhiri bintang.


def main(): #titik awal program dijalankan
    while True: #perulangan akan terus dilakukan jika program yang dijalankan belum benar
        try:
            size = int(input("Masukkan ukuran pola belah ketupat (harus bilangan bulat positif ya!): ")) #meminta inputan
            if size > 0: #memastikan jika inputan merupakan bilangan bulat positif
                pola_belah_ketupat(size) #menampilkan pola belah ketupat sesuai ukuran
                break #jika sudah benar maka program berhenti
            else:
                print("Ukuran harus bilangan bulat positif.") #jika angka yang diinput tidak bilangan bulat positif maka akan meminta input ulang
        except ValueError:
            print("Input tidak valid, silakan masukkan bilangan bulat.") #jika input bukan angka, maka akan meminta input ulang

if __name__ == "__main__": #menjalankan program
    main()

