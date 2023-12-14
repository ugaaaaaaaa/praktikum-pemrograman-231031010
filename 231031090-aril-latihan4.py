pendapatan = int(input("pendapatan :"))

if pendapatan <= 1000:
    presentase = 0
elif pendapatan > 1000 and pendapatan <= 2000:
    presentase = 10
elif pendapatan > 2000 and pendapatan <= 3000:
    presentase = 20
elif pendapatan > 3000 and pendapatan <= 4000:
    presentase = 30
elif pendapatan > 4000 and pendapatan <= 5000:
    presentase = 40
else:
    pendapatan >5000
    presentase = 50

bonus = pendapatan*(presentase/100)
total = pendapatan + bonus

print(f"""
pendapatan\t: {pendapatan}
presentase: {presentase}
Bonus\t\t : {bonus}
Total Pendapatan: {total}     """)