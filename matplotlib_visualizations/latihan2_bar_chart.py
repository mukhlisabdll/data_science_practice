# Import library Matplotlib
import matplotlib.pyplot as plt

# Data untuk plot
kategori = ['A', 'B', 'C', 'D', 'E']  # Kategori yang akan dibandingkan
nilai = [80, 70, 90, 85, 75]  # Nilai dari setiap kategori

# Membuat grafik batang
plt.bar(kategori, nilai, color='orange')

# Menambahkan judul dan label
plt.title("Perbandingan Nilai per Kategori")
plt.xlabel("Kategori")
plt.ylabel("Nilai")

# Menampilkan grid untuk kemudahan visualisasi
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Menampilkan grafik
plt.show()