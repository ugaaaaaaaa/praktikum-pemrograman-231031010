'''UTS
1. Buat variabel jenis list berikut.
    
    BIO =  ['Nama Lengkap',
            'NIM',
            'Tanggal-Bulan-Tahun Lahir'
            'aktif'
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil'
            'Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu rencana studi mahasiswa']
#(NOTED: sesuaikan dengan data anda)
            
2. Buat variabel jenis nested list berikut.

MK =   [['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216',],
        ['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [2,3,3,2,3,3,3,2],
        ['Selasa','Senin','Rabu','Senin','Kamis','Kamis','Kamis','Kamis'],
        ['07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10']]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, waktu kuliah, dan jadwal)
        
3. Susun Kode dengan hasil runing seperti berikut.
           
            
             INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                        JURUSAN SAINS PROGRAM
                    KARTU RENCANA STUDI MAHASISWA
                           GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : 60022010
Program/prodi   : S1/Sistem Informasi A
Tahun Masuk     : 2023 Ganjil
Status          : Aktif
|--|--  10  --|--           26         --|--5--|-- 8  --|--    13   --|
-----------------------------------------------------------------------
No. Kode      |      Mata Kuliah         | SKS |  Hari  |    Jadwal   |
-----------------------------------------------------------------------
1   22A1209   | Matkul1                  |  2  | Senin  |  07.30-09.10|
2   22A1210   | Matkul2                  |  3  | Selasa |  07.30-09.10|
3   22A1211   | Matkul3                  |  3  | Rabu   |  07.30-09.10|
4   22A1212   | Matkul4                  |  2  | Senin  |  07.30-09.10|
5   22A1213   | Matkul5                  |  3  | Kamis  |  07.30-09.10|
6   22A1214   | Matkul6                  |  3  | Kamis  |  07.30-09.10|
7   22A1215   | Matkul7                  |  3  | Kamis  |  07.30-09.10|
8   22A1216   | Matkul8                  |  2  | Kamis  |  07.30-09.10|
-----------------------------------------------------------------------
                        TOTAL SKS           21                        |
-----------------------------------------------------------------------
|---------------------------------71-----------------------------------|
Summary:
Jumlah Mata Kuliah       : 8
Jumlah Mata Kuliah 2 SKS : 3 Mata Kuliah
Jumlah Mata Kuliah 3 SKS : 5 Mata kuliah
Mata Kuliah hari Senin   : 2 Mata Kuliah
Mata Kuliah hari Selasa  : 1 Mata Kuliah
Mata Kuliah hari Rabu    : 1 Mata Kuliah
Mata Kuliah hari Kamis   : 1 Mata Kuliah
Mata Kuliah hari Jumat   : 0 Mata Kuliah
                                              Parepare, 25 Oktober 2023



                                                     NAMA LENGKAP      
                                                     ------------
'''


# Tulis Kode Jawaban di bawah!

bio =  ['Anugrah Dwi Ansarna',
            '231031010',
            '1-Maret-2005',
            'aktif',
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil',
            'Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu rencana studi mahasiswa']

mk =   [['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216',],
        ['Pemrograman','Kalkulus Dasar','Sains Terpadu','Bahasa Indonesia','Pengantar Teknologi Informasi','Cinta dan Imteq','Pancasila','Agama'],
        ['3,3,3,2,3,2,2,2'],
        ['Selasa','Senin','Rabu','Senin','Kamis','Kamis','Kamis','Kamis'],
        ['07.30-09.10','13.30-15.10','13.30-15.10','07.30-09.10','13.30-15.10','15.30-17.00','09.20-11.10','13.30-15.10']]

print()
sp = 71
strr = bio[-5]+ ' '+ bio[-6].replace('-','/')


print(f"""
{bio[-4].upper().center(sp)}
{bio[-2].upper().center(sp)}
{bio[-1].upper().center(sp)}
{strr.upper().center(sp)}

Nama Lengkap    : {bio[0].upper()}
NIM             : {bio[1]}
Program/prodi   : {bio[4]} / {bio[5]}
Tahun Masuk     : {bio[6][0:4]} {bio[7].title()}
Status          : {bio[3].title()}
""")

print('-'*71)
print('No.'+'|'+'Kode'.center(10)+'|'+'Mata Kuliah'.center(26)+'|'+'SKS'.center(5)+'|'+'Hari'.center(8)+'|'+'Jadwal'.center(13)+'|')
print('-'*71)
print('2. '+'|'+mk[1][0].ljust(10)+'|'+mk[2][0].ljust(26)+'|')
print('3. '+'|'+mk[1][1].ljust(10)+'|'+mk[2][1].ljust(26)+'|')
print('4. '+'|'+mk[1][2].ljust(10)+'|'+mk[2][2].ljust(26)+'|')
print('5. '+'|'+mk[1][3].ljust(10)+'|'+mk[2][3].ljust(26)+'|')
print('6. '+'|'+mk[1][4].ljust(10)+'|'+mk[2][4].ljust(26)+'|')

  