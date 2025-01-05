# Mengimpor pustaka NumPy dengan alias 'np'
import numpy as np

# Membuat array dua dimensi (matriks) menggunakan fungsi np.array()
array = np.array([[18, 11], [12, 17]])  # Matriks 2x2 dengan elemen yang diberikan

# Menghitung invers dari matriks menggunakan fungsi np.linalg.inv()
invers = np.linalg.inv(array)

# Menghitung determinan dari matriks menggunakan fungsi np.linalg.det()
determinan = np.linalg.det(array)

# Menampilkan matriks asli
print("Matrix asli:")
print(array)

# Menampilkan invers matriks
print("Invers:")
print(invers)

# Menampilkan determinan matriks
print("Determinan:")
print(determinan)

