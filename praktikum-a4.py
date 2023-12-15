nama = 'Anugrah Dwi Ansarna'
nim = ['2','3','1','0','3','1','0','1','0']
print(nim)
print('------akses item------')
print(f'item indeks 0: {nim[0]}')
print(f'item indeks 4: {nim[1]}\n')
print('------akses indeks dengan jumlah list yang tidak di ketahui jumlah list-----')
print(f'item indeks terakhir: {nim[len(nim) - 1]}')
print(f'item indeks pertama: {nim[-len(nim)]}\n')
print("-------akses indeks negatif------")
print(f'item indeks 6 [-3]: {nim[-3]}') # notice the pattern that if u subtract it, it 
print(f'item indeks 4 [-5]: {nim[-5]}') # will be equal to total item in the list
print(f'item indeks 7 [-2]: {nim[-2]}')
print(f'item indeks semua: {nim[:]}') # this just means, takes data start from index zero 
                                      # because the left part isn't filled and take all data 
                                      # because the right part isn't filled
print(f'item indeks [:8]: {nim[:-1]}') # this means, takes len(nim) - 1 data, and start from 
                                        # zero index because left part isn't filled
print(f'item indeks [:6]: {nim[:-3]}') # this means, takes len(nim) - 3 data, and start from
                                        # zero index becaues left part isn't filled
print(f'items indeks kosong: {nim[-3:-3]}') # the quick trick is, if the left and right part
                                        # is equal, the array is 0
print(f'items indeks kosong: {nim[-2:-3]}') # also another quick trick is,
                                        #  if the left part is smaller than and right part
                                        # the is also. This trick is only allowed in negative 
                                        # indexing

print(f'{nim[len(nim) - 3]}')
# the code above is equivalent with the code below 
# so if you're asked, to find the positive index of a negative index
print(f'{nim[-3]}\n')


data = ['Anugrah Dwi Ansarna',2023,'Aktif'],
[95,96,96,95],
[20,22],
[['S1-Reguler','Ganjil']]

matkul = ['Agama Islam','Pancasila','Bahasa Indonesia','Wawasan Cinta IPTEK dan IMTAQ']
sks    = [2,2,2,2]
# Menambahkan matkul dan sks ke dalam data (di akhir)
data.append(matkul)
data.append(sks)

# Mata kuliah 1: Matkul1 dengan jumlah 2 sks
print(f'{data[4][0]} dengan jumlah {data[-1][0]} sks\n')
# Mata kuliah 2: Matkul2 dengan jumlah 3 sks
print(f'{data[4][1]} dengan jumlah {data[-1][1]} sks\n')
# Mata kuliah 3: Matkul3 dengan jumlah 3 sks
print(f'{data[4][2]} dengan jumlah {data[-1][2]} sks\n')
# Mata kuliah 4: Matkul4 dengan jumlah 2 sks
print(f'{data[4][3]} dengan jumlah {data[-1][3]} sks\n')
data[4].append('Pengantar Pemrograman')
data[5].append(3)
# print(data)
# Tambahkan 3 matkul dengan sks nya
data[4].append('Pengantar Teknologi Informasi')
data[5].append(3)
data[4].append('Kalkulus Dasar 1')
data[5].append(3)
data[4].append('Sains Terpadu')
data[5].append(3)
# Mata kuliah 6: Matkul6 dengan jumlah .. sks
print(f'{data[4][4]} dengan jumlah {data[-1][4]} sks\n')
# Mata kuliah 7: Matkul7 dengan jumlah .. sks
print(f'{data[4][5]} dengan jumlah {data[-1][4]} sks\n')
# Mata kuliah 8: Matkul8 dengan jumlah .. sks
print(f'{data[4][6]} dengan jumlah {data[-1][6]} sks\n')
# Mata kuliah 8: Matkul8 dengan jumlah .. sks
print(f'{data[4][7]} dengan jumlah {data[-1][6]} sks\n')

# Tambahkan 8 nilai masing-masing
data[1].append(98)
data[1].append(96)
data[1].append(90)
data[1].append(91)
print(data[0][0])
print(data[-1][0])
print(data[2][0:])

# >> Tugas: Nama Mahasiswa Thomas dengan NIM: 600201014
print(f'Nama Mahasiswa {data[0][0]} dengan NIM {"".join(nim)}')
# >> Program pendidikan Thomas: S1-Reguler
print(f'Program pendidikan {data[0][0]}: {data[3][0]}')
# >> Angkatan : 2023-Ganjil
print(f'Angkatan : {data[0][1]}-{data[3][1]}')
# >> Jumlah nilai Thomas adalah: 8
print(f'Jumlah nilai {data[0][0]} adalah: {len(data[1])}')
# >> Data terbesar Thomas adalah: 98
print(f'Data terbesar {data[0][0]} adalah: {max(data[1])}')
# >> Data terkecil Thomas adalah: 90
print(f'Data terkecil {data[0][0]} adalah: {min(data[1])}')
# >> Rata-rata nilai Thomas adalah: 94.625
print(f'Rata-rata nilai {data[0][0]} adalah: {sum(data[1])/(len(data[1]))}')