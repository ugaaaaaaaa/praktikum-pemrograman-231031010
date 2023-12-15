import random 

nama = "Anugrah Dwi Ansarna"
nim = "231031010"
meet = "praktikum 3"
prodi = "sistem informasi a"
email = "ugapares03@gmail.com"
sp = 35
Ttl = "1-januari-2005"
Alamat = "Perumahan Grand Sulawesi Blok E35F"
Asal = "Parepare"
Hobi = "Baca buku"
Tinggi = "170"
print("-" * sp)
print(f"{nama.upper().center(sp)}")
print(f"{nim.center(sp)}")
print("\n" * 2)
print(f"{meet.capitalize().rjust(sp)}")
print(f"{prodi.title().rjust(sp)}")
print(f"{email.rjust(sp)}")
print("-" * sp)


print(
    f"""   Halo, nama saya {nama.upper()}dengan NIM {nim} dari prodi\n{prodi.title()}, ini adalah file {meet.title()}. Terima kasih"""
)
print("\n")
print(
    f"Biodata Saya: \nNama\t: {nama.title()}\nNIM\t: {nim}\nProdi\t: {prodi.title()}\nTTL\t: {Asal}, {Ttl}\nAlamat\t: {Alamat}\nAsal\t: {Asal}\nHobi\t: {Hobi}\nTinggi\t: {Tinggi}cm"
)

print()

stat = 'sir issac newton'
up = stat.upper()
statArr = up.split(" ")
print(statArr[2][0], statArr[0], statArr[1])
print(statArr[2], statArr[0][0], statArr[1][0])



stat2 = "&sir$ @issac# *newton." 
print(stat2.strip('&$@#*.'))

angka =  random.randint(0,9)
inputan = int(input("masukkan angka: "))
if(angka == inputan):
    print("benar!")
else:
    print("maaf anda salah\n")
    print(f'jawaban yang benar adalah {angka}')
    print()

