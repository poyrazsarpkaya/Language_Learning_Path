
import sys


try: 

   def write(f="App",m="w",y=" "):
      createfile=open(f,m)
      if m=="r":
        print(f.read())
        f.close()

      elif m=="w":
        m.write(y)                                 #neden komut olarak görmüyor bilmiyorum muhtemelen dosya yazılı olmadığından
        print("Kaydedildi..")
        f.close()

      elif m=="a":
        f.write(y)
        print("Kaydedildi..")
        f.close()

      else:
        print("Yanlış mod seçimi") , istek()

                             
    
   
   def istek():
     filee=input("Açmak istediğiniz dosyayı yazın,uzantısı ile birlikte; \n Example: Myproject.css \n ")
     mod=input("Hangi modda açılsın \n r: okuma modu \n w: Yazma modu \n a: ekleme modu ")
     yazı=input("Yazılıcakları giriniz\nYoksa Devam ediniz..\n")
    
     filee=str(filee)
     mod=str(mod)                        #Burada write fonksiyonundaki open komutunu 
     yazı=str(yazı)                      #anlayabilmesi için string ifadeye dönüstürdük
     write(filee,mod,yazı) 
   

   istek()


except (FileNotFoundError,OSError):
    print("Filename or extension is incorrect\nTry again")


finally:
    a=input("Yeni bir dosya da işlem yapmak isterseniz open diyin \nProgramı kapatmak için Herhangi bir tuşa basın : ")
    if a=="open":
        istek()
    else:
        sys.exit()
