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

# Membuat DataFrame baru yang hanya berisi data mahasiswa dengan IPK lebih dari 3.3
filtered_df = df[df['IPK'] > 3.3]

# Menampilkan seluruh DataFrame yang berisi kolom tambahan 'IPK'
print(df)

# Menampilkan DataFrame yang sudah difilter, hanya mahasiswa dengan IPK di atas 3.3
print(filtered_df)
