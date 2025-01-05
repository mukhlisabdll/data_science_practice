# Meminta pengguna untuk memasukkan angka dan mengubahnya menjadi integer
angka = int(input("Masukan angka: "))

# Mengecek apakah angka yang dimasukkan lebih besar dari 0
if angka > 0:
    # Jika angka lebih besar dari 0, maka angka tersebut positif
    print("Angka positif")
# Mengecek apakah angka yang dimasukkan sama dengan 0
elif angka == 0:
    # Jika angka sama dengan 0, maka angka tersebut adalah nol
    print("Angka nol")
# Jika angka tidak lebih besar dari 0 dan tidak sama dengan 0, maka angka tersebut negatif
else:
    # Jika angka lebih kecil dari 0, maka angka tersebut negatif
    print("Angka negatif")
