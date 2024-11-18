import matplotlib.pyplot as plt

# Data untuk stack plot
hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat']
belajar = [2, 3, 4, 3, 5]
makan = [1, 1, 1, 1, 1]
istirahat = [1, 2, 1, 2, 2]
hiburan = [2, 1, 2, 1, 3]

# Membuat stack plot
plt.stackplot(hari, belajar, makan, istirahat, hiburan,
              labels=['Belajar', 'Makan', 'Istirahat', 'Hiburan'],
              colors=['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3'])

# Menambahkan judul dan label
plt.title("Distribusi Waktu dalam Seminggu")
plt.xlabel("Hari")
plt.ylabel("Jam")

# Menambahkan legenda
plt.legend(loc='upper left')

# Menampilkan plot
plt.show()