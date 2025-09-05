#Tugas 1: Menyimpan dan Menampilkan Data
Nama_Produk_1 = 'Kopi Pagi'
Harga_produk_1 = 18000.5
Nama_Produk_2 = 'Roti Coklat'
Harga_produk_2 = 10000
status_ketersediaan_roti = True #roti tersedia

print("Nama produk 1: ", Nama_Produk_1)
print("Harga produk 1: ", Harga_produk_1)
print("Nama produk 2: ", Nama_Produk_2)
print("Harga produk 2: ", Harga_produk_2)
print("Status ketersediaan roti:", status_ketersediaan_roti)

#Tugas 2: Konversi Tipe Data dan Input Pengguna
garis_pemisah = "=" * 20
print(garis_pemisah)

jumlah_kopi_str = input('Masukkan jumlah pesanan kopi: ')
jumlah_roti_str = input('Masukkan jumlah pesanan roti: ')

print("Masukkan jumlah pesanan kopi: ", jumlah_kopi_str)
print("Masukkan jumlah pesanan roti: ", jumlah_roti_str)
print("Tipe data awal jumlah kopi: ", type(jumlah_kopi_str))
print("Tipe data awal jumlah roti: ", type(jumlah_roti_str))

#tipe data setelah konversi
jumlah_kopi_int =  int (jumlah_kopi_str)
jumlah_roti_int = int (jumlah_roti_str)
print("Tipe data setelah konversi: ", type(jumlah_kopi_int))
print("Tipe data setelah konversi: ", type(jumlah_roti_int))

# Tugas 3: Operasi pada Angka
garis_pemisah = "=" * 20
print(garis_pemisah)

Total_harga_kopi = Harga_produk_1 * jumlah_kopi_int
Total_harga_roti = Harga_produk_2 * jumlah_roti_int  
Total_belanja = Total_harga_kopi + Total_harga_roti
Uang_bayar = 50000
Kembalian = Uang_bayar - Total_belanja

print("Total harga kopi: ", Total_harga_kopi)
print("Total harga roti: ", Total_harga_roti)
print("Total belanja keseluruhan: ", Total_belanja)
print("Uang yang dibayarkan: ", Uang_bayar)
print("Kembalian: ", Kembalian)

#Tugas 4: Operasi pada String
garis_pemisah = "*" * 25
print(garis_pemisah) 

nama_pelanggan = input("Masukkan nama anda: ")
pesan_terima_kasih = f"Terimakasih, {nama_pelanggan} sudah berbelanja di Coffee Shop Bahagia !"
print(pesan_terima_kasih)

garis_pemisah = "*" * 25
print(garis_pemisah)

print(f"Total harga {Nama_Produk_1} adalah Rp{Total_harga_kopi} ")