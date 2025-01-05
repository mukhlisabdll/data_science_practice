def rectangle_area(panjang, lebar):
    # Fungsi ini menghitung luas persegi panjang
    # dengan mengalikan panjang dan lebar.
    return panjang * lebar

def safe_input(prompt):
    # Fungsi ini memastikan input yang diberikan adalah angka positif.
    # Jika input tidak valid (bukan angka atau <= 0), fungsi akan meminta ulang.
    while True:
        try:
            value = float(input(prompt))  # Mencoba mengubah input menjadi float.
            if value > 0:
                return value  # Mengembalikan nilai jika positif.
            else:
                print("Masukan angka lebih besar dari 0.")  # Pesan jika nilai <= 0.
        except ValueError:
            print("Input tidak valid, harap masukan angka.")  # Pesan jika input bukan angka.

while True:
        print("===============================")
        print("Menghitung Luas Persegi Panjang")
        print("===============================\n")

        # Meminta input panjang dan lebar dari pengguna.
        panjang = safe_input("Masukan panjang: ")
        lebar = safe_input("Masukan lebar: ")

        # Menghitung luas persegi panjang menggunakan fungsi rectangle_area.
        hasil = rectangle_area(panjang, lebar)
        print(f"Luas persegi panjang adalah: {hasil} cm²")

        # Memastikan apakah pengguna ingin menghitung lagi.
        ulang = input("Apakah anda ingin menghitung lagi? (y/n): ").strip().lower()
        if ulang != 'y':  # Keluar jika input bukan 'y'.
            print("Terima kasih! Program selesai.")
            break  # Mengakhiri loop.
