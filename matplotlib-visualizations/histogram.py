# Import library Matplotlib
import matplotlib.pyplot as plt

# Data untuk histogram
nilai_ujian = [55, 60, 65, 70, 75, 80, 85, 90, 95, 60, 65, 70, 75, 80, 85, 70, 75, 80, 85, 90]

# Membuat histogram
plt.hist(nilai_ujian, bins=5, color='purple', edgecolor='black')

# Menambahkan judul dan label
plt.title("Distibusi Nilai Ujian Kelas")
plt.xlabel("Nilai") 
plt.ylabel("Frekuensi")

# Menampilkan grafik
plt.show()