# Mengimpor library NumPy dan memberikan alias np untuk kemudahan
import numpy as np

# Membuat array satu dimensi menggunakan numpy dengan elemen-elemen 1 hingga 9
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Menghitung nilai rata-rata (mean) dari array 'data'
mean = np.mean(data)

# Menghitung nilai tengah (median) dari array 'data'
median = np.median(data)

# Menghitung standar deviasi (standard deviation) dari array 'data'
# Standar deviasi mengukur seberapa jauh data tersebar dari nilai rata-rata
std_dev = np.std(data)

# Mencetak hasil perhitungan mean, median, dan standar deviasi
print("Mean:", mean)
print("Median:", median)
print("Standar Deviasi:", std_dev)


