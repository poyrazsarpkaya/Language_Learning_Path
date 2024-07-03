from traceback import print_tb
import sys


data_user=["crazyboy_30", "xxxkaraltrx"]
data_password=["qwer","asdf"]


def membership():
 print(">>>>>>>>>>>>  Hoşgeldin Başkan  <<<<<<<<<<<<"+"\n")
 print("Kaydolmak için 'kayıt' diyin")
 print("Giriş yapmak için 'giriş' diyin")
 m=input("Hangisi?: ")


 girishak=4
 if m=="kayıt":
    while True:
      nick=input("Kullanıcı adı: ")
      if nick in data_user:
        print("Bu adkullanılmakta :( tekrar belirleyin :)")
        continue
      else:
        data_user.append(nick)
        print( "Harika bir nick şimdi parolanızı belirleyin")
        passs=input("Parola: ")
        paass=input("Parolayı doğrulayın: ")

      if not passs==paass:
       print("Parolalar uyuşmuyor :(")
       print("Tekrarkayıt olmayı deneyin :>")
       continue
    
      else:
       data_password.append(paass)
       print("Kaydediliyor...")
       print("Kayıt başarılı")
       break


 elif m=="giriş":
    while True:
      a=input("Kullanıcı adınızı girin: ")
      s=input("Şifrenizi girin: ")

      if not (a in data_user) and not (s in data_password):
         print("Kullanıcı adı yada parola hatalı.")
         print("Tekrar giriniz..")
         girishak-=1
         if girishak==0:
             print("Giriş hakkınız bitti")
             sys.exit()
         elif girishak==2:
             print("<<<<Son iki hakkınız kaldı!>>>>")
         continue

      else:
        print("Giriş başarılı")
        break
        
 else:
    print("Bir takım hatalı seçimler ## *_* ## ")
    end=input("Ana sayfaya dönmek için a ya basın\nÇıkmak için herhangi bir tuşa basın\n")

    if end=="a":
     print("Ana sayfaya dönülüyor...") ,membership()
    else:
        sys.exit() 
    

membership()



"""
y=0

while y<9:
    if y==8:
     continue     # Başa döndürür
    y+=1
"""