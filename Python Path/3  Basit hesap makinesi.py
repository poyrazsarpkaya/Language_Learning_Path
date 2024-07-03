
print("makinaya hoşşgeln")
islem = str(input("Lütfen bir işlem girin:"))
say1 = int(input("sayı:"))
say2 = int(input("Sayı:"))

q = say1 + say2
w = say1 - say2
e= say1 * say2
r= say1 / say2

if islem == "q":
    print("Sonuç:", q)

elif islem == "w":
    print("Sonuç:" , w)

elif islem == "e":
    print("Sonuc:" , e)

elif islem =="r":
    print("Sonuç:" ,r)

else:
    print("Hatalı girdin mk")