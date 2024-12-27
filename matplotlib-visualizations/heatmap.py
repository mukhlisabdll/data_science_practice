# Import library Matplotlib & Numpy
import matplotlib.pyplot as plt
import numpy as np

# Data untuk heatmap
data = np.array([
    [10, 15, 20, 25],
    [30, 35, 40, 45],
    [50, 55, 60, 65],
    [70, 75, 80, 85]
])

# Membuat heatmap
plt.imshow(data, cmap='viridis', interpolation='nearest')

# Menambahkan color bar
plt.colorbar(label="Intensitas Nilai")

# Menambahkan label
plt.title("Heatmap Sederhana")
plt.xlabel("Kolom")
plt.ylabel("Baris")

# Menampilkan heatmap
plt.show()