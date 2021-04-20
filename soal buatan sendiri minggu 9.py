# Aloysius Gonzaga Ardhian Krisna Aji
# 71180298

# Brandon dimintai oleh gurunya untuk membuat program 
# menghitung nilai rata2, sebagai teman karibnya bantulah brandon 
# membuat programnya.

#Input
# memasukan jumlah data yang diminta
# memasukan angka sesuai jumlahnya

#Output
# outputnya berupa nilai rata2 nya

masukan = int (input("\n Masukan Banyak data: "))
print()
data = []
hasil = 0

for i in range(0,masukan):
    angka = int(input("Masukan data ke %d: "% (i + 1)))
    data.append(angka)
    hasil = hasil + data[i]
    rata = hasil / masukan
    
print ("\nNilai Rata2nya adalah: " ,rata)








