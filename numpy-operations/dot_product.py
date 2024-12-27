# Latihan 8: Menghitung Dot Product dari Dua Array

# Mengimpor pustaka NumPy dengan alias 'np'
import numpy as np

# Membuat dua array menggunakan fungsi np.array()
array1 = np.array([1, 2, 4])  # Array pertama dengan elemen 1, 2, dan 4
array2 = np.array([4, 5, 6])  # Array kedua dengan elemen 4, 5, dan 6

# Menghitung dot product dari kedua array menggunakan fungsi np.dot()
dot_product = np.dot(array1, array2)

# Menampilkan hasil dot product
print("Dot product:", dot_product)

