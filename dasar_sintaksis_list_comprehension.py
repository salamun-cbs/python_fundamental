print('\nPerintah Del')
daftar_buku = ['Seven Habit', 'How to Influence People', 'First Things First', '4DX']
del(daftar_buku[2])
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan list Comprehension')
daftar_buku = ['Seven Habit', 'How to Influence People', 'First Things First', '4DX']
del(daftar_buku[:])
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan list Comprehension start')
daftar_buku = ['Seven Habit', 'How to Influence People', 'First Things First', '4DX']
del(daftar_buku[0:-2]) #START:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan list Comprehension start')
daftar_buku = ['Seven Habit', 'How to Influence People', 'First Things First', '4DX']
del(daftar_buku[0::2]) #START:END:STEP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
daftar_buku = ['Seven Habit', 'How to Influence People', 'First Things First', '4DX']
daftar_buku_baru = daftar_buku[:]
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])
print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: ganjil')
daftar_buku = ['1 Seven Habit', '2 How to Influence People', '3 First Things First', '4 4DX']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: genap')
daftar_buku = ['1 Seven Habit', '2 How to Influence People', '3 First Things First', '4 4DX']
daftar_buku_baru = daftar_buku[1::2] #start stop end
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: buang diujung')
daftar_buku = ['1 Seven Habit', '2 How to Influence People', '3 First Things First', '4 4DX']
daftar_buku_baru = daftar_buku[0:-1:2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: ganjil')
daftar_buku = ['1 Seven Habit', '2 How to Influence People', '3 First Things First', '4 4DX']
print(daftar_buku[0::2])
