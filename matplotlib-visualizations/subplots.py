# Import library Matplotlib
import matplotlib.pyplot as plt

# Data untuk plot
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]  # Kuadrat dari x
y2 = [25, 16, 9, 4, 1]  # Kuadrat terbalik
y3 = [2, 4, 6, 8, 10]  # Linear
y4 = [1, 2, 1, 2, 1]  # Sinyal periodik

# Membuat subplots dengan 2 baris dan 2 kolom
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot 1: Grafik garis
axs[0, 0].plot(x, y1, color='blue', marker='o')
axs[0, 0].set_title("Grafik Kuadrat")
axs[0, 0].set_xlabel("X")
axs[0, 0].set_ylabel("Y")

# Plot 2: Grafik scatter
axs[0, 1].scatter(x, y2, color='red')
axs[0, 1].set_title("Grafik Kuadrat Terbalik")
axs[0, 1].set_xlabel("X")
axs[0, 1].set_ylabel("Y")

# Plot 3: Grafik batang
axs[1, 0].bar(x, y3, color='green')
axs[1, 0].set_title("Grafik Linear")
axs[1, 0].set_xlabel("X")
axs[1, 0].set_ylabel("Y")

# Plot 4: Grafik garis
axs[1, 1].plot(x, y4, color='purple', linestyle='--')
axs[1, 1].set_title("Grafik Sinyal Periodik")
axs[1, 1].set_xlabel("X")
axs[1, 1].set_ylabel("Y")

# Menambahkan jarak antar plot
plt.tight_layout()

# Menampilkan grafik
plt.show()
