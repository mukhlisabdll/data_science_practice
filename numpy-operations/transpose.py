# Latihan 7: Melakukan Transpose pada Array 2D

# Mengimpor library NumPy dan memberi alias np
import numpy as np  

# Membuat array 2D dengan dua baris dan tiga kolom
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Melakukan transpose pada array 2D
transpose = np.transpose(array_2d)

# Menampilkan array asli
print("Array asli:")
print(array_2d)

# Menampilkan array setelah dilakukan transpose
print("Array setelah transpose:")
print(transpose)
