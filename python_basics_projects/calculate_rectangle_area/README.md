# Menghitung Luas Persegi Panjang dengan Python

Repository ini berisi kode Python sederhana untuk menghitung luas persegi panjang. Program ini dirancang untuk membantu pemula belajar Python dengan memahami konsep fungsi, validasi input, dan pengulangan (loop).

## Fitur

- **Fungsi Modular:** Kode memanfaatkan fungsi terpisah untuk perhitungan dan validasi input.
- **Validasi Input:** Memastikan bahwa panjang dan lebar yang dimasukkan oleh pengguna adalah angka positif.
- **Pengulangan:** Pengguna dapat memilih untuk menghitung luas beberapa kali tanpa perlu menjalankan ulang program.

## Kode Program

```python
def rectangle_area(panjang, lebar):
    return panjang * lebar

def safe_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Masukan angka lebih besar dari 0.")
        except ValueError:
            print("Input tidak valid, harap masukan angka.")

while True:
    print("===============================")
    print("Menghitung Luas Persegi Panjang")
    print("===============================\n")

    panjang = safe_input("Masukan panjang: ")
    lebar = safe_input("Masukan lebar: ")

    hasil = rectangle_area(panjang, lebar)
    print(f"Luas persegi panjang adalah: {hasil} cm²")

    ulang = input("Apakah anda ingin menghitung lagi? (y/n): ").strip().lower()
    if ulang != 'y':
        print("Terima kasih! Program selesai.")
        break
```

## Cara Menjalankan

1. **Unduh Kode**: Salin atau unduh file kode dari repository ini.
2. **Jalankan Program**: Gunakan Python versi 3.x untuk menjalankan file di terminal atau IDE pilihan Anda.
   ```bash
   python nama_file.py
   ```
3. **Masukkan Input**: Ikuti petunjuk di terminal untuk memasukkan panjang dan lebar.

## Contoh Eksekusi

Berikut adalah contoh input dan output program:

```plaintext
===============================
Menghitung Luas Persegi Panjang
===============================

Masukan panjang: 10
Masukan lebar: 5
Luas persegi panjang adalah: 50.0 cm²

Apakah anda ingin menghitung lagi? (y/n): n
Terima kasih! Program selesai.
```

## Tujuan

Kode ini dibuat untuk:

- Membantu pemula belajar Python.
- Memahami penggunaan fungsi, validasi input, dan pengulangan.
