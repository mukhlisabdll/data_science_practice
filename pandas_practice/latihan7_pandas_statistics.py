# Mengimpor library pandas dengan alias 'pd'
import pandas as pd

# Membuat dictionary dengan data Nama, Umur, dan Jurusan
data = {
    'Nama' : ['Mukhlis', 'Shanum', 'Berlin'],  # Nama mahasiswa
    'Umur' : [22, 20, 21],                    # Umur masing-masing mahasiswa
    'Jurusan' : ['Informatika', 'Fisika', 'Matematika']  # Jurusan yang diambil
}

# Membuat DataFrame dari dictionary 'data'
df = pd.DataFrame(data)

# Menambahkan kolom baru 'IPK' ke DataFrame 'df' yang berisi nilai IPK untuk setiap mahasiswa
df['IPK'] = [3.5, 3.2, 3.8]

# Menampilkan seluruh DataFrame yang sudah berisi kolom tambahan 'IPK'
print(df)

# Menampilkan ringkasan statistik deskriptif dari DataFrame 'df'
print(df.describe())
