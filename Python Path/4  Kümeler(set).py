from ast import Break
from traceback import print_tb


kume={56,25,6457,253,345}       #Kümelerin sırası önemli değildir. İçindeki elaman tekrar etmez
kume.clear()                    #kümeyi temizler
print(kume)


F= [9,6,8]
D=set(F)                        #listeyi sete yani kümeye çevirebiliriz. SÖZLÜĞÜ SET YAPMAK İÇİN 
print(D)

 
kume1 ={1,2,3,4,5,6}
L = kume1.copy()                #Kümeyi kopyalayıp öbürünede atar böylelikle yazamakla uğraşmamış oluruz
print( L)

kumme= {23,45,345,21,13,}
kumme5={43,22,11}
kumme.update(kumme5)            #kümeyi diğer bi küme ile günceller,birleştirir
print(kumme)


kumma={2,4,5,6,7}
kumma.remove(7)
kumma.pop()                     #Bu komut kümeye yapılırsa ilk değeri,listede yapılırsa sonuncusunu çıkarır
print(kumma)
"Ve yahutta"
kumma6={2,4,5,6,7}
kumma6.discard(5)               # remove komutu gibi çalışmadığında hata vermez
print(kumma6)


p=set("Alibeyköy meslek")
f=set([2,5,7,9,0,2,5])
print(p)
print(f)

N= {76,56,71,23,11}
M={32,56,76,35,89}
print(N.union(M))               # Kümeleri birleştirir ve birleştirdiği için değer tekrar etmez
print(N-M)                      # N de olup M de olmayanları verir
print(N^M)                      # Her iki kümeyi sırayla farkını alır
print(N.intersection(M))        # Kümelerin  kesişimini veren methodtur



O = {"Smerkan1":123456789}
P ={"Avsım2": "yekdudusıseçorc"}


e = input("Kullanıcı adınız:")
r= input("Şifre:")

if e and e in O or P:
    print(" Giriş Başarılı")

elif e and r in O or N:
    print("Sucsess")

else:
    print("Yanlış parola Robot musun lan sen")


