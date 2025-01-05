# Membuat dictionary kosong untuk menyimpan data siswa
data_siswa = {}

# Menambahkan data siswa di dalam dictionary kosong
data_siswa["siswa1"] = {
    "Nama": "Mukhlis Abdiilah",  # Nama siswa
    "Kelas": "XII RPL 2",        # Kelas siswa
    "Nilai": 98                  # Nilai siswa
}
data_siswa["siswa2"] = {
    "Nama": "Bruce Wayne",  # Nama siswa
    "Kelas": "XII RPL 2",   # Kelas siswa
    "Nilai": 100            # Nilai siswa
}

# Menambahkan data siswa secara manual
while True:  # Perulangan untuk terus meminta input hingga pengguna berhenti
    # Menanyakan apakah pengguna ingin menambahkan data siswa baru
    tambah = input("Apakah anda ingin menambahkan data siswa baru (ya/tidak): ").lower()
    
    if tambah == "tidak":  # Jika jawabannya 'tidak', keluar dari loop
        break
    elif tambah == "ya":  # Jika jawabannya 'ya', lanjutkan untuk menambah data
        # Meminta nama siswa
        nama = input("Masukkan nama siswa: ")
        # Meminta kelas siswa
        kelas = input("Masukkan kelas siswa: ")

        try:
            # Meminta nilai siswa dan mencoba mengonversinya ke tipe float
            nilai = float(input("Masukkan nilai siswa: "))
        except ValueError:  # Jika terjadi kesalahan (nilai bukan angka), tampilkan pesan error
            print("Nilai harus berupa angka.")
            continue  # Kembali ke awal perulangan jika input tidak valid
        
        # Membuat ID unik untuk siswa baru berdasarkan jumlah data yang sudah ada
        id_baru = f"siswa{len(data_siswa) + 1}"
        # Menyimpan data siswa baru ke dalam dictionary
        data_siswa[id_baru] = {
            "Nama": nama,
            "Kelas": kelas,
            "Nilai": nilai
        }
        print("Data siswa berhasil ditambahkan!")  # Konfirmasi berhasil menambahkan data
        print(f"ID baru untuk siswa ini adalah: {id_baru}")
    else:
        # Jika input selain 'ya' atau 'tidak', beri pesan bahwa input tidak valid
        print("Input tidak valid. Ketik 'ya' atau 'tidak'.")

# Mencetak data siswa yang ada di dalam dictionary menggunakan perulangan for
print("\nData Siswa:")
for nama, info in data_siswa.items():  # Iterasi untuk setiap item di dalam dictionary data_siswa
    print(f"Nama: {info['Nama']}")       # Menampilkan nama siswa
    print(f"- Kelas: {info['Kelas']}")   # Menampilkan kelas siswa
    print(f"- Nilai: {info['Nilai']}")   # Menampilkan nilai siswa
    print()  # Memberikan spasi antar data siswa

print(data_siswa)