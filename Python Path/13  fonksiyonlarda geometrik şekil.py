def geo(m):
    if m==3:
        a=int(input("1.köşe: "))
        b=int(input("2.köşe: "))
        c=int(input("3.köşe: "))

        if (c<a+b) and (b<a+c) and (a<b+c):
            if a==b==c:
                print("Eşkenar üçgen")

            elif (a==b) or (b==c) or (a==c):
                print("İkiz kenar üçgen")
            else:
                print("Çeşit Kenar Üçgen")
        else:
            print("üçgen değildir")


    elif m==4:
        x=int(input("1.köşe: "))
        y=int(input("2.köşe: "))
        z=int(input("3.köşe: "))
        q=int(input("4.köşe: "))

        if x==z==y==q:
            print("Eşit kenar Dörtgen yani Kare!")

        elif (x==z and y==q) or (x==y and z==q) or (x==q and y==z):
            print("Dikdörtgendir")

        else:
            print("Çeşit kenar dörtgen")

    else:
        print("Hatalı giriş yaptınız")





while True:
    istek=int(input("Köşe sayısını seçiniz: "))

    if not (istek==3 or istek==4) :
          print("Hatalı  girdiniz tekrar deneyin")
          continue

    elif istek==3 or istek==4:
      geo(istek)
      break
    


