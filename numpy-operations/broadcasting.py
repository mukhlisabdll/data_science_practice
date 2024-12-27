# Latihan 10: Melakukan Broadcasting pada Array

# Mengimpor pustaka NumPy dengan alias 'np'
import numpy as np

# Membuat array 1D dan 2D
array1d = np.array([1, 2, 3])  # Membuat array satu dimensi dengan elemen 1, 2, dan 3
array2d = np.array([[10, 20, 30], [40, 50, 60]])  # Membuat array dua dimensi (matriks) 2x3

# Melakukan broadcasting
hasil = array2d + array1d  # Menambahkan array 1D ke setiap baris array 2D secara otomatis

# Menampilkan hasil
print("Array 1D:")  # Menampilkan teks untuk menjelaskan bahwa yang berikutnya adalah array 1D
print(array1d)  # Menampilkan array 1D
print("Array 2D:")  # Menampilkan teks untuk menjelaskan bahwa yang berikutnya adalah array 2D
print(array2d)  # Menampilkan array 2D
print("Hasil broadcasting:")  # Menampilkan teks untuk menjelaskan bahwa yang berikutnya adalah hasil dari operasi broadcasting
print(hasil)  # Menampilkan hasil penjumlahan dengan broadcasting

