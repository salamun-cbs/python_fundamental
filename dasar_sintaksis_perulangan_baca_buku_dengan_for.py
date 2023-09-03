"""
Program perulangan membaca buku dengan for
"""
jumlah_buku = 10
print('Ibu berkata, "baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 0
print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

print("Dengan for")
for jumlah_buku_yang_sudah_dibaca in range(1, jumlah_buku+1):
    print(f"Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")

print(f"jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}")