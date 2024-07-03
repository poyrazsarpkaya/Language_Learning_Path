"""
fak=1

while True:
    sayyı=int(input("Faktöriyeli hesaplanacak değeri girin: "))
    if sayyı <=0:
        print("Negatif olmamalı! tekrardan başlatın.")
    else:
        for i in range(1,sayyı+1):
         fak*=i
         print(fak)
        break

"""

k=1

while True:
    rakam=int(input("Lütfen negatif değer girmeyin: "))
    if rakam <=0:
            print("Negatif değer girdin mal! Değer gir: ")
    else:
        for i in range(1,rakam+1):
             k=k*i
        print(k)
        break