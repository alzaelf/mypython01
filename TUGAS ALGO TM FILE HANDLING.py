#NADINE ALFINA AZZAHWA
#242410103040
#KELAS F

#Tugas 1 (slide 20)
data = open ("C:\\Users\\lenovo\\Documents\\FASILKOM\\Kuliah\\Algo1\\2122 Gasal\\Data\\Text 01.txt", "r")
# Variabel data berfungsi untuk membuka file text dalam mode read
tambahan_teks = data.readlines()
# Variabel list_teks berfungsi untuk menjadikan variable data sebagai program list

tambahan_teks.insert(2, 'Matakuliah favoritnya adalah "Algo"\n')
# Penggunaan insert bertujuan untuk menyelipkan string tersebut ke dalam index 2

data = open("C:\\Users\\lenovo\\Documents\\FASILKOM\\Kuliah\\Algo1\\2122 Gasal\\Data\\Text 01.txt", "w")
# Di sini variabel data dibuka kembali namun dalam mode write

for t in tambahan_teks:
    data.write(t)
# "for t in" disini berfungsi untuk menjadikan "t" sebagai variable tambahan_teks yang sudah ada dalam variabel tambahan_teks
# Kemudian method write digunakan untuk menuliskan list pada variabel tambahan_teks ke dalam file

data.close()
# Close berfungsi menutup sesi dari file teks tersebut


#Tugas 2 Slide 25
import os

path_directory = "C:\\Users\\lenovo\\Documents\\FASILKOM\\Kuliah\\Algo1\\2122 Gasal"
files = os.listdir(path_directory)

file_count = 1
for file in files:
    full_path = os.path.join(path_directory, file)
    if os.path.isfile(full_path):  # Mengecek apakah item adalah file
        print(f"File {file_count} : {file}")
        file_count += 1

