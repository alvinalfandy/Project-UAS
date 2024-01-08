from datetime import datetime

# Kode Rincian toko
toko = {
    "nama": "===== Alfandy Geprek  =====",
    "alamat": "BLOK A 2",
    "nomor_telepon": "083814329508"
}

# Daftar menu
daftar_menu = {
    1: {"nama": "Ayam Geprek", "harga": 5000},
    2: {"nama": "AYAM Bakar", "harga": 5000},
    3: {"nama": "Paket Chakung Hemat 1", "harga": 10000},
    4: {"nama": "Paket Chakung Hemat 2", "harga": 20000},
    5: {"nama": "Minuman Air Putih", "harga": 2000}
}

# Tampilkan rincian toko
print(toko["nama"])
print(toko["alamat"])
print(toko["nomor_telepon"])
print("=" * 29)

# Tampilkan daftar menu
print("Daftar Menu:")
for i, menu in daftar_menu.items():
    print(f"{i}. {menu['nama']} ({menu['harga']} IDR)")

# Input pesanan
pesanan = {}
total_harga = 0

while True:
    pilihan = input("Pilih menu (1-5) atau ketik 'selesai' untuk mengakhiri pesanan: ")
    if pilihan.lower() == 'selesai':
        break
    elif not pilihan.isdigit() or int(pilihan) not in daftar_menu:
        print("Pilihan tidak valid.")
    else:
        indeks_menu = int(pilihan)
        menu_terpilih = daftar_menu[indeks_menu]
        jumlah = input(f"Jumlah {menu_terpilih['nama']} yang dipesan: ")
        while not jumlah.isdigit() or int(jumlah) <= 0:
            print("Jumlah tidak valid. Harap masukkan angka positif.")
            jumlah = input(f"Jumlah {menu_terpilih['nama']} yang dipesan: ")
        jumlah = int(jumlah)
        total_harga += menu_terpilih['harga'] * jumlah
        pesanan[menu_terpilih['nama']] = jumlah

# Input uang dari pelanggan
uang_pelanggan = float(input("Input uang: "))

# Tampilkan struk
print("# Nama toko")
print(toko["nama"])
print(toko["alamat"])
print(toko["nomor_telepon"])
print("=" * 29)
print("Menu yang dipesan:")
for item, jumlah in pesanan.items():
    print(f"{item}: {jumlah} x {daftar_menu[item]['harga']} IDR = {jumlah * daftar_menu[item]['harga']} IDR")
print("Total: ", total_harga)
print("Uang: ", uang_pelanggan)
print("Kembalian: ", uang_pelanggan - total_harga)
print("=" * 29)
print("Barang yang sudah dibeli tidak dapat dikembalikan")
print("=" * 29)
print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
