

try:
  def customer():
    a = str(input("Adı:"))
    b = str(input("Soyadı:"))         # alacağımız değerin biçimine göre int,string, float gibi belirtmeliyiz
    c = int(input("Doğum yılı:"))
    d = str(input("E-posa adresi:"))
    e = str(input("Annenizin kızlık soyadı:"))

    age=2022-c

    if not(14<age<81):
        print("Hatalı değer girdiniz Lütfen tekrar giriniz")
        customer()
    else:
     print("Kaydınız başarıyla tamamlandı")
     print("Ad:",a," " ,"Soyad:",b," ","Yaşı:",age," ","Posta:",d," ","Kızlık soyad:",e)
     order()

  
  def order():
     print("\nTek seferde yanlızc 3 sipariş verilebilir.\n")

     K= int(input("Siparişiniz:"))
     L= int(input("Sipariş2:"))
     M= int(input("Sipariş3"))
     A = K+L+M

     print("Total:",A,"ödemeniz gerekmektedir")


  customer()

except ValueError :
  print("Eksik ya da hatalı giriş yaptınız\nTekrar deneyin")
  customer()
 

finally:
    print("Afiyet olsun :)")
