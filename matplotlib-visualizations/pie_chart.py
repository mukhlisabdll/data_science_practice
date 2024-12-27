# Import library Matplotlib 
import matplotlib.pyplot as plt

# Data untuk pie chart
aktivitas = ["Tidur", "Belajar", "Olahraga", "Rekreasi", "Coding"]
waktu = [8, 6, 2, 3, 5]

# Membuat pie chart
plt.pie(waktu, labels=aktivitas, autopct='%1.1f%%', startangle=90)

# Menambahkan judul
plt.title("Distribusi Penggunaan Waktu Sehari")

# Menampilkan pie chart
plt.show()