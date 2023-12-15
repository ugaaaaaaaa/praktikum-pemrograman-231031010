#Anugrah Dwi Ansarna    
#231031010
#Sistem Informasi A
#LATIHAN 4

pendapatan = int(input('Masukkan pendapatan: '))

if pendapatan <= 1000:
    persentase = 0
elif 1001 <= pendapatan <= 2000:
    persentase = 10
elif 2001 <= pendapatan <= 3000:
    persentase = 20
elif 3001 <= pendapatan <= 4000:
    persentase = 30
elif 4001 <= pendapatan <= 5000:
    persentase = 40
else:
    persentase = 50

bonus = pendapatan * (persentase / 100)

total = pendapatan + bonus

print('Pendapatan:', pendapatan)
print('Persentase:', persentase, '%')
print('Bonus:', bonus)
print('Jumlah Total:', total)