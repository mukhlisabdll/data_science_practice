# Import library Matplotlib
import matplotlib.pyplot as plt

# Data untuk plot
waktu_belajar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]  # Waktu belajar dalam jam
nilai_ujian = [50, 52, 55, 60, 62, 68, 70, 75, 85, 95, 100]  # Nilai ujian yang diperoleh

# Membuat grafik scatter
plt.scatter(waktu_belajar, nilai_ujian, color='red', marker='o')

# Menambahkan judul dan label
plt.title("Hubungan antara Waktu Belajar dan Nilai Ujian")
plt.xlabel("Waktu Belajar (jam)")
plt.ylabel("Nilai Ujian")

# Menampilkan grafik
plt.show()