# Mengimpor library pandas dengan alias 'pd'
import pandas as pd

# Membuat dictionary dengan data Nama, Umur, dan Jurusan
data = {
    'Nama' : ['Mukhlis', 'Shanum', 'Berlin'],  # Nama mahasiswa
    'Umur' : [22, 20, 21],                    # Umur masing-masing mahasiswa
    'Jurusan' : ['Informatika', 'Fisika', 'Matematika']  # Jurusan yang diambil
}

# Membuat dictionary dengan data Hobi
data_lain = {
    'Nama' : ['Mukhlis', 'Shanum'],  # Nama mahasiswa yang memiliki hobi
    'Hobi' : ['Membaca', 'Berenang']  # Hobi masing-masing mahasiswa
}

# Membuat DataFrame dari dictionary 'data'
df = pd.DataFrame(data)

# Membuat DataFrame dari dictionary 'data_lain'
df_hobi = pd.DataFrame(data_lain)

# Menggabungkan DataFrame 'df' dan 'df_hobi' berdasarkan kolom 'Nama' menggunakan metode join 'left'
merged_df = pd.merge(df, df_hobi, on='Nama', how='left')

# Menampilkan DataFrame asli 'df'
print(df)

# Menampilkan DataFrame hasil gabungan 'merged_df'
print(merged_df)
