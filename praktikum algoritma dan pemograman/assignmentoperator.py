stok_barang = 50
barang_masuk = 20
barang_keluar = 10

# Menambah stok dengan barang yang masuk
stok_barang += barang_masuk
print(f"Stok setelah pembelian: {stok_barang}")

# Mengurangi stok dengan barang yang terjual
stok_barang -= barang_keluar
print(f"Stok setelah penjualan: {stok_barang}")