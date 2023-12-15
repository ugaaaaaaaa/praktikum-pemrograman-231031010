#Fungsi Rekursif Fibonacci
def fibonacci(n):
	if n < 0:
		print('Tidak ada bilangan yang bernilai negatif')
		return None
	elif n == 0 or n == 1:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)
	
#ProgramUtama
nilai = 20
a = 35
hasil = fibonacci(nilai)
print('Finobacci (%d) = %d'  % (nilai, hasil))
print()
print('='*35)
print()

#Program Input Fibonacci
nilai_2 = int(input('masukkan sebuah bilangan : '))
hasil_2 = fibonacci(nilai_2)
print('Finobacci (%d) = %d'  % (nilai_2, hasil_2))