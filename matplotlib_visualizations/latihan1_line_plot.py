# Import library Matplotlib
import matplotlib.pyplot as plt

# Data untuk plot
waktu = [1, 2, 3, 4, 5]  # Contoh data waktu (jam)
suhu = [30, 32, 34, 33, 31]  # Contoh data suhu (derajat Celcius)

# Membuat grafik garis
plt.plot(waktu, suhu, color='blue', marker='o', linestyle='-', linewidth=2, markersize=6)

# Menambahkan judul dan label
plt.title("Perubahan Suhu Seiring Waktu")
plt.xlabel("Waktu (jam)")
plt.ylabel("Suhu (°C)")

# Menampilkan grid untuk kemudahan visualisasi
plt.grid(True)

# Menampilkan grafik
plt.show()
