tabungan_awal = 5000
jumlah_bulan = int(input("Berapa bulan Anda ingin menghitung deposito? "))

deposito_bulanan = []
for i in range(1, jumlah_bulan + 1):
  deposito = float(input(f"Masukan nilai deposito bulan ke-{i}: "))
  deposito_bulanan.append(deposito)

total_tabungan_akhir = tabungan_awal + sum(deposito_bulanan)

print(f"Tabungan saya sekarang adalah Rp{total_tabungan_akhir}.")