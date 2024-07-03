"""
#This is a Calculator

def topla(x,y):
    return x+y

def cikar(x,y):
    return x-y

def carp(x,y):
    return x*y

def bol(x,y):
    return x/y


x = float(input("Enter Number: "))
y = float(input("Enter Other Number: "))
z = str(input("Enter the symbol: "))


if z == "+":
    print(topla(x,y))

elif z== "-":
    print(cikar(x,y))

elif z == "*":
    print(carp(x,y))

elif z == "/":
    print(bol(x,y))

else:
     print("Please try again")
     proccess()

"""


class fruit():
    kcal=11
    suagar= "16 gr"
    protein= "10gr"

elma = fruit()
print(elma.suagar)



class cat():

    ageg=7

    def __init__(self,name,age,tiype,color):           
        self.name=name
        self.age=age
        self.tiype=tiype
        self.color=color      
        #self.humanage= age*7                      #humanage method fonksiyonu vereceğimize bunu özellik yapabilirz. direkt şartlandırabiliriz
                
#1  def humanage(self,ageg=7):
#1     return self.age * ageg
       

#2  def humanage(self):
#2    return self.age * cat.ageg
    
    def humanage(self):
        return self.age * self.ageg


                                               #Self aslında classın içine dahil ettiğimiz rex değişkeni. Rexin Özellikleri bir nevi sınıfın içine kaydediyorum sonra fonksiyon olarak çağırıyorum
rex= cat("rex", 15, "germany", "Black")         # Yani her rex. birşeyler yazınca fonksiyon içeride, Verdiğimiz girdileri döndürmesini söylüyor.  Rexe color vermişim fonksiyon içeride color değerine ne girilmişşe ona eşittir diyor
print(rex.tiype)
print(rex.humanage())

rex2= cat("rex2", 4, "a","b")
#1 print(rex.humanage(10))                        #Fonksiyon Methodunda defaultdeğer verip hesaplama yapan kişi isterse yılçarpanını(ageg) değiştirebilir.

rex3= cat("rex3", 3, "k", "blackwhite")
#2 rex3.ageg = 10                                 #Sabit değerli bir değişken atayıp hiç değişmemesini sağladık
#2 print(rex3.humanage())

rex4 = cat("rex4", 6,"t", "y")
rex4.ageg = 4                                     #Bu kullanımda ise yıl çarpanı (ageg) değişkeninin değişebildiğini görüyoruz
print(rex4.humanage())