# Latihan 6: Membuat Array Acak dan Mencari Nilai Minimum serta Maksimum

# Mengimpor library NumPy dan memberi alias np
import numpy as np  

# Membuat array acak dengan 10 elemen yang bernilai integer antara 0 dan 99
array_acak = np.random.randint(0, 100, size=10)

# Menemukan nilai minimum dan maksimum dalam array acak
minimum = np.min(array_acak)  # Menemukan dan menyimpan nilai terkecil dari array
maksimum = np.max(array_acak)  # Menemukan dan menyimpan nilai terbesar dari array

# Menampilkan array acak, nilai minimum, dan nilai maksimum yang ditemukan dari array
print("Array acak:", array_acak)  # Mencetak array acak yang telah dibuat
print("Nilai minimum:", minimum)    # Mencetak nilai minimum yang ditemukan dari array
print("Nilai maksimum:", maksimum)    # Mencetak nilai maksimum yang ditemukan dari array

