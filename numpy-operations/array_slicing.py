# Latihan 4: Membuat Array 2D dan Melakukan Slicing

# Mengimpor library NumPy dan memberikan alias np untuk kemudahan
import numpy as np

# Membuat array 2D dengan 3 baris dan 3 kolom
# Baris 1: [1, 2, 3]
# Baris 2: [4, 5, 6]
# Baris 3: [7, 8, 9]
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Mengambil elemen pada baris kedua (indeks 1) dan kolom ketiga (indeks 2)
# Dalam array 2D, indeks pertama adalah untuk baris, dan yang kedua untuk kolom
sliced = array_2d[1, 2]  # Elemen yang diambil adalah 6

# Menampilkan array asli (2D)
print("Array asli:")
print(array_2d)

# Menampilkan elemen yang diambil (hasil slicing)
print("Elemen yang diambil:", sliced)


