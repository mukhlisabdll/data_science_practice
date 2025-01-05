# Mengimpor library pandas dengan alias 'pd'
import pandas as pd

# Membuat dictionary dengan kunci 'Nama', 'Umur', dan 'Jurusan'
data = {
    'Nama' : ['Mukhlis', 'Shanum', 'Berlin'],  # Daftar nama mahasiswa
    'Umur' : [22, 20, 21],                     # Daftar umur mahasiswa
    'Jurusan' : ['Informatika', 'Fisika', 'Matematika']  # Daftar jurusan mahasiswa
}

# Membuat DataFrame dari dictionary 'data'
df = pd.DataFrame(data)

# Menambahkan kolom baru 'IPK' ke DataFrame 'df' dengan nilai-nilai yang sesuai
df['IPK'] = [3.5, 3.2, 3.8]

# Menampilkan DataFrame 'df' yang sudah dimodifikasi
print(df)
