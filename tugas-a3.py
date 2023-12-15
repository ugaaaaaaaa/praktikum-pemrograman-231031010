print('Tugas Praktikum 3'.center(40).upper())
nama = 'Anugrah Dwi Ansarna'
nim  = '231031010'
prodi= 'Sistem Informasi A'
print(f'''
Nama\t: {nama}
NIM\t: {nim}
prodi\t: {prodi}\n''')


'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outpunya sesuai'''


str1 = 'duFort Frankel Von Neumann'
#output: NEUMANN DUFORT FRANKEL VON
up1 = str1.upper()
print(up1)
up1 = up1.split()
print(up1)
print(up1[3],up1[0],up1[1],up1[2])
print()
str2 = 'duFort Frankel Von Neumann'
#output: DFV NEUMANN
up2 = str2.upper()
print(up2)
up2 = up2.split()
print(up2)
print(up2[0][0],up2[1][0],up2[2][0],up2[3])
print()
str3 = 'duFort Frankel Von Neumann'
#output: DUFORT FVN
up3 = str3.upper()
print(up3)
up3 = up3.split()
print(up3)
print(up3[0],up3[1][0],up3[2][0],up3[3][0])
print()
str4 = 'duFort Frankel Von Neumann'
#output: N duFort FV
up4 = str4
print(up4)
up4 = up4.split()
print(up4)
print(up4[3][0],up4[0],up4[1][0],up4[2][0])
print()
str5 = 'duFort Frankel Von Neumann'
#output: NEUMANN d f v
up5 = str5.upper()
print(up5)
up5 = up5.split()
print(up5)
print(up5[3],up5[0][0].lower(),up5[1][0].lower(),up5[2][0].lower())
print()
str6 = 'duFort Frankel Von Neumann'
#output: NEUMANN DFV
up6 = str6.upper()
print(up6)
up6 = up6.split()
print(up6)
print(up6[3],up6[0][0],up6[1][0],up6[2][0])
print()
str7= '@duFort Frankel Von Neumann$'
#output: duFort Frankel Von NEUMANN
up7 = str7
print(up7)
up7 = up7.split()
print(up7)
print(up7[0][1:-1],up7[1],up7[2],up7[3][0:-2].upper())
print()
str8 = '#duFort4Frankel4Von4Neumann$'
#output: duFort Frankel Von Neumann
up8 = str8
print(up8)
up8 = up8.split('4')
print(up8)
print(up8[0].strip('#'),up8[1],up8[2],up8[3].strip('$'))
print()
str9 = '@duFort@-^Frankel*-(Von(-(Neumann$'
#output: duFort Frankel Von Neumann
up9 = str9
print(up9)
up9 = up9.split('-')
print(up9)
print(up9[0].strip('@'),up9[1].strip('^*'),up9[2].strip('('),up9[3].strip('($'))
print()
str10 = '@DUFort@1^FraNkel*1(VoN(1(NeuMann^'
#output: duFort Frankel Von Neumann
up10 = str10.title()
print(up10)
up10 = up10.split('1')
print(up10)
#print(up10[0][1:-1].replace('f','F'),up10[1][1:-1].title(),up10[2][1:-1].title(),up10[3][1:-1].title())
print(up10[0][1:-1].lower().replace('f','F'),up10[1][1:-1],up10[2][1:-1],up10[3][1:-1])
print()