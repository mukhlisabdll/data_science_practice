# Import library Matplotlib
import matplotlib.pyplot as plt

# Data untuk scatter plot
tinggi = [150, 155, 160, 165, 170, 175, 180, 185, 190]
berat = [50, 53, 55, 60, 65, 68, 70, 75, 80]

# Membuat scatter plot
plt.scatter(tinggi, berat, color='green', edgecolor='black', s=100)

# Menambahkan judul dan label
plt.title("Hubungan Tinggi Badan dan Berat Badan")
plt.xlabel("Tinggi Badan (cm)")
plt.ylabel("Berat Badan (kg)")

# Menampilkan grid untuk kemudahan visualisasi
plt.grid(True)

# Menampilkan grafik
plt.show()