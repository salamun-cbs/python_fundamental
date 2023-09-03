"""
Semua sintaksis dasar pemrograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: Mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuansial
print('Ibu berkata,"Pergi ke toko"')
print('Budi menjawab,"Baik, apa yang harus saya lakukan di toko"')
print('Ibu menjawab,"Beli satu botol susu"')
print("Maka Budi berangkat ke toko")
print("Dan mulai berbelanja")

# Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1577
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang kerumah")
print("Menyampaikan hasilnya kepada Ibu")
