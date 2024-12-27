# Mengimpor library pandas dengan alias 'pd'
import pandas as pd

# Membuat sebuah kamus (dictionary) bernama 'data' yang berisi tiga kolom: 'Nama', 'Umur', dan 'Jurusan'
data = {
    'Nama' : ['Mukhlis', 'Shanum', 'Berlin'],  # Kolom 'Nama' berisi daftar nama
    'Umur' : [22, 20, 21],                    # Kolom 'Umur' berisi daftar umur masing-masing individu
    'Jurusan' : ['Informatika', 'Fisika', 'Matematika']  # Kolom 'Jurusan' berisi jurusan dari masing-masing individu
}

# Mengonversi kamus 'data' menjadi DataFrame bernama 'df' menggunakan fungsi 'pd.DataFrame()'
df = pd.DataFrame(data)

# Mencetak isi DataFrame 'df' ke layar
print(df)
