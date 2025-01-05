import random  # Mengimpor modul random untuk menghasilkan angka acak

# Menampilkan judul permainan
print("=====================")
print("Permainan Tebak Angka")
print("=====================")

# Menginisialisasi angka yang harus ditebak dan jumlah percobaan
number_to_guess = random.randint(1, 10)  # Menentukan angka acak antara 1 dan 10
attempts = 0  # Menginisialisasi jumlah percobaan
max_attempts = 5  # Menentukan batas percobaan

# Memulai loop untuk meminta tebakan dari pemain
while attempts < max_attempts:
    try:
        guess = int(input("Tebak angka antara 1 sampai 10: "))  # Meminta input tebakan angka
        attempts += 1  # Menambah jumlah percobaan

        # Mengecek apakah tebakan benar, terlalu kecil, atau terlalu besar
        if guess == number_to_guess:
            print("Selamat! Anda menebak dengan benar.")
            break  # Menghentikan permainan jika tebakan benar
        elif guess < number_to_guess:
            print("Terlalu kecil!")
        elif guess > number_to_guess:
            print("Terlalu besar!")
    except ValueError:  # Menangani kesalahan input jika bukan angka
        print("Input harus angka yang valid!")

# Menampilkan hasil jika percobaan habis
if attempts == max_attempts and guess != number_to_guess:
    print(f"Anda gagal menebak dalam {max_attempts} kali percobaan. Angka yang benar adalah {number_to_guess}.")
