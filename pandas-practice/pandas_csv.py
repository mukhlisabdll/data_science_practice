# Mengimpor library pandas dengan alias 'pd'
import pandas as pd

# Membaca file CSV 'Salary_Data.csv' dari lokasi yang diberikan dan menyimpannya dalam sebuah DataFrame bernama 'df'
df = pd.read_csv('C:\\data-science-practice\\datasets\\Salary_Data.csv')

# Menampilkan 5 baris pertama dari DataFrame 'df' menggunakan fungsi 'head()'
print(df.head())

