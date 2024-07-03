kayıtlistesi=[("Katrin","Selsim",19,"Oyuncu")]

def printkayıt(ad="bilgi yok", soyad="Bilgi yok", yas="Bilgi yok", meslek="Bilgi yok"):
 print("Kayıt yapılıyor...")
 print("\n Ad: {} \n Soyad: {} \n Yas: {} \n Meslek: {} \n".format(ad,soyad,yas,meslek))
 print("Kayıt başarılı :)")


def kayıt():
 m=input("Adınız?: ")
 n=input("Soyadınız?: ")
 u=input("Yaşınız kaç? ")
 y=input("Mesleğiniz nedir? ")
 p=(m,n,u,y)
 kayıtlistesi.extend(p)
 printkayıt(m,n,u,y)

kayıt()