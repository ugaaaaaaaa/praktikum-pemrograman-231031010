# Fungsi Rekursif factorial dengan perulangan
def faktorial(nilai):
    if nilai <= 1:
        return 1
    else:
        return nilai * faktorial(nilai - 1)

# Program Utama
for i in range(11):
    print('%2d! = %d' % (i, faktorial(i)))
      
#Fibonaci
b = 35
print()
print('='*35)
print()
def fibonacci(n):
    a = [0, 1]
    while len(a) < n:
        a.append(a[-1] + a[-2])
    return a[:n + 1]

nilai = int(input("Masukkan batas untuk deret Fibonacci: "))

hasil = fibonacci(nilai)
print(f"Deret Fibonacci hingga {nilai}: {hasil}")