"""
tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = Kamus
"""

kamus_ind_eng ={'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother' }
print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('\nData ini dikirimkan oleh server Gojek, untuk memberika informasi driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal' : '2020-06-10',
    'driver_list': [
        {'nama': 'Eko', 'jarak': 10},
        {'nama': 'Dwi', 'jarak': 30},
        {'nama': 'Tri', 'jarak': 100},
        {'nama': 'Catur', 'jarak': 1000}
    ]
}

print(data_dari_server_gojek)
