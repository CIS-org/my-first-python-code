# KONSTRUKSI DASAR PYTHON
# SEQUENITIAL : Eksekusi berurutan

print('Hello World')
print('by Gunawan')
print('Tanggal 23 September 2022')
print('_'*10)

# PERCABANGAN : Eksekusi Terpilih
ingin_cepat = False
if ingin_cepat:
    print('Jalan lurus aja ya!')
else:
    print('Jalan lain')
print('_'*10)

# pengulangan
jumlah_anak = 4
for index_anak in range(1, jumlah_anak+1): # jumlah perulangan = 5 - 1 = 4
    print(f'Hallo anak #{index_anak}')