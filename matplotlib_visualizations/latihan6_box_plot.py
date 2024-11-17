# Import library Matplotlib
import matplotlib.pyplot as plt

# Data untuk box plot
data = {
    "Grup A": [85, 86, 87, 88, 90, 80, 95],
    "Grup B": [75, 78, 80, 85, 88, 90, 93],
    "Grup C": [85, 87, 88, 89, 90, 92, 94],
}

# Membuat box plot
plt.boxplot(data.values(), tick_labels=data.keys(), patch_artist=True,
            boxprops=dict(facecolor="lightblue", color="blue"),
            medianprops=dict(color="orange", linewidth=2))

# Menambahkan judul dan label
plt.title("Distribusi Nilai Antar Grup")
plt.ylabel("Nilai")

# Menampilkan box plot
plt.show()
