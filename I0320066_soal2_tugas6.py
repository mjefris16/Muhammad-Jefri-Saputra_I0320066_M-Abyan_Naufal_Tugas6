nilai = input("Masukkan nilai yang ingin dirata-ratakan: ")
list_nilai = nilai.split(",")
total_nilai = [float(x) for x in list_nilai]

total = 0

for nilai in total_nilai :
    total = total + nilai
rata_rata = total/len(total_nilai)
print("Total nilai anda adalah: ", total)
print("Rata-rata nilai anda adalah: ", rata_rata)