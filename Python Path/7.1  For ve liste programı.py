

liste=[44,54,23,767,214,67,67,44,689,234]

print("Listeniz: ",liste)
print("---------İşlemler----------")
print("Değer ekleme: ekle")
print("Değer silme: sil")
print("> < e sırlama: sırala")
print("< > e sıralama: ters")
print("Kaç tane var: kac")
print("Kaçıncı sırada: sıra")
print("Belirli bir sıraya ekleme: bsıra")
print("Değer var mı yok mu : varyok")

s=str(input("İşleminizi seçin: "))


if s=="ekle":
    m=int(input("Eklenecek eğeri girin: "))
    liste.append(m)
    print("Güncel liste: " ,liste)

elif s== "sil":
     m=int(input("silinecek eğeri girin: "))
     liste.remove(m)
     print("Güncel liste:", liste)

elif s=="sırala":
    liste.sort()
    print(liste)

elif s=="ters":
    liste.reverse()
    print(liste)

elif s=="kac":
    m=int(input("Değer girin: "))
    print("adet saysısı:",liste.count(m))

elif s=="sıra":
    m=int(input("Değeri girin:"))
    print(liste.index(m))

elif s=="bsıra":
    m=int(input("Hangi sıraya: "))
    n=int(input("Hangi değer: "))
    liste.insert(m,n)
    print(liste)

elif s=="varyok":
    m=int(input("Değeri girin:"))
    for i in liste:
        if i==m:
             print("Değer var")
        else:
             print("Değer yok") 
else:
    print("Hatalı giriş yaptınız:")

            