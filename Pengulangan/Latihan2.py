import random
n = int(input("Masukkan jumlah n: "))
jumlah = 0
while jumlah < n:
    angka = random.random()  
    if angka < 0.5:
        print(angka)
        jumlah += 1
