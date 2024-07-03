
tamer=[54,23,547,7867,7,63,31,22,3,0.33]
print("Listeniz:",tamer)

print("-------İşlemi seçiniz---------")
print("-Ekleme: ek")
print("-Silme: sil")
print("-Kaç adet var: kac")
print("-kaçıncı sırada: sıra")
print("-Sıralama yapma: sırala")
print("-Tersten sırala: ters")
print("-Belirlenen yere ekleme yapar: yer ek")
print("-Değer var mı yok mu: varyok")

t=str(input("işlemi Girin: "))


if t=="ek":
    y=int and float (input("Sayıyı Girin: "))
    tamer.append(y)
    print("Güncel listen",tamer)

elif t=="sil":
    y=int and float (input("Sayıyı Girin: "))
    tamer.remove(y)
    print("Güncel liste",tamer)

elif t=="kac":
    y=int and float(input("Sayıyı Girin: "))
    print(tamer.count(y))

elif t=="sıra":
    y=int and float(input("Sayıyı Girin: "))
    print(tamer.index(y))

elif t=="sırala":
    y=int and float(input("Sayıyı Girin: "))
    print(tamer.sort())

elif t== "ters":
    y=int and float(input("Sayıyı Girin: "))
    print(tamer.reverse())
    
elif t=="yer ek":
    y=int and float(input("Sayıyı Girin: "))
    z=(int(input("Kaçıncı sıraya eklensin?")))
    tamer.insert(z,y)
    print("Yeni liste",tamer)

elif t=="varyok":
    y=int and float(input("Sayıyı Girin: "))
    print("Kontrol ediliyor...")
    for i in tamer:
       if i==y:
          print("Değer var")
       else:
        exit
        print("Değer Yok")

else:
    print("Hatalı girdin")