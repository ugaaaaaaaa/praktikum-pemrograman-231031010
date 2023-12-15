#Anugrah Dwi Ansarna    
#231031010
#Sistem Informasi A
#LATIHAN 3

nama_karyawan = input('Masukkan nama: ')
pendapatan = int(input('Masukkan pendapatan: '))
status = 'Berhak'  # Menyimpan status awal

if pendapatan > 1000:
    print('Status: Berhak mendapatkan bonus')
else:
    status = 'Tidak Berhak'  # Mengubah status jika pendapatan kurang atau sama dengan 1000
    print('Status: Tidak Berhak mendapatkan bonus')

# Menampilkan informasi menggunakan f-string
print(f"""
    Nama karyawan: {nama_karyawan}
    Pendapatan: {pendapatan}
    Status: {status}
""")