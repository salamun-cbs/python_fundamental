"""
Program perulangan membaca buku dengan while sampai paham
"""
jumlah_buku = 10
print('Ibu berkata, "baca semua bukumu"')
jumlah_baca = 0

jumlah_paham = 0
print(f'jumlah buku yang sudah dibaca dan dipahami {jumlah_paham}')

while jumlah_baca < jumlah_buku * 2:
    jumlah_baca = jumlah_baca + 1
    if jumlah_paham == 9:
        print(f"buku ke {jumlah_paham + 1 } belum pahami")
    else:
        jumlah_paham = jumlah_paham + 1
        print(f"buku ke {jumlah_paham} sudah dibaca dan dipahami")

print(f'jumlah buku yang sudah dibaca dan dipahami {jumlah_paham} buku')
if jumlah_paham == jumlah_buku:
    print('Bu, semua buku sudah dibaca dan dipahami')
else:
    print(f'Bu, tidak semua buku bisa dipahami. '
          f'Budi hanya bisa memahami {jumlah_paham} buku ')
