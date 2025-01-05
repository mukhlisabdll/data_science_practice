# Mengimpor library NumPy untuk operasi numerik
import numpy as np

# Membuat array NumPy yang berisi angka 1, 2, dan 3
array = np.array([1, 2, 3])

# Menghitung eksponensial dari setiap elemen dalam array menggunakan fungsi exp() dari NumPy
eksponensial = np.exp(array) # np.exp menghitung e (bilangan Euler) yaitu sekitar sekitar 2.71828 dipangkatkan dengan elemen array

# Menampilkan hasil eksponensial dari array
print("Eksponensial dari array:", eksponensial)


