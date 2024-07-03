from ast import Try
from distutils.file_util import write_file


a=input("Sayı1: ")
b=input("Sayı2: ")


try:
     a=int(a)
     b=int(b)
     print(a/b)
       
except ZeroDivisionError:
      print("0 Girmeyiniz!")
    
except ValueError:
        print("Lütfen Tam sayı giriniz! ")


      
"""
except (ValueError,ZeroDivisionError):                     #İkisini birleştirdik
    print("Bir haa oluştu Tekar giriniz")
"""




try:
 def fak(number):
    if number ==(0 or 1):
        return 1
    else:
        return number* fak(number-1)

 def Girdi():
  a=int(input("SAYI GİRİNİZ:"))
  print(a,"kadar olan çarpımı",fak(a))

 Girdi()
  
except ValueError:
    print("Lütfen Tam sayı giriniz"),Girdi()

