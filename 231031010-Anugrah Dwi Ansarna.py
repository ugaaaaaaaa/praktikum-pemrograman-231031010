def judul():
    print('PROGRAM MENGHITUNG LUAS DAN KELILING'.center(b))
    print('BANGUN DATAR PERSEGI'.center(b))
    print()

def inputan():
    panjang = float(input('Masukkan Panjang: '))
    lebar = float(input('Masukkan Lebar: '))
    return panjang,lebar

def hitung(panjang,lebar):
    luas = panjang*lebar
    keliling = (panjang*lebar)*2
    return luas,keliling

def tampil(pesan,nilai):
    print(f'Hasil Perhitungan nilai {pesan}: {nilai}')

def pilihan():
    pilih = input('apakah ingin melanjutkan? [y/n]: ')
    if pilih == 'y':
        a = True
    else:
        a = False
        print('Bye Bitch!')
    return a

a = True
b = 50

while a:

    print('='*b)

    #judulc
    judul()

    #inputan panjang dan lebar
    panjang,lebar = inputan()
    luas,keliling = hitung(panjang,lebar)

    #cetak atau display 
    tampil('luas',luas)
    tampil('keliling',keliling)

    #pilihan
    a = pilihan()

    print('='*b)