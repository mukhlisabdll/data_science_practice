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

# Mengelompokkan DataFrame 'df' berdasarkan kolom 'Jurusan' dan menghitung rata-rata 'IPK' untuk setiap kelompok
grouped_df = df.groupby('Jurusan')['IPK'].mean()

# Menampilkan seluruh DataFrame yang berisi kolom tambahan 'IPK'
print(df)

# Menampilkan DataFrame yang berisi rata-rata IPK untuk setiap jurusan
print(grouped_df)
