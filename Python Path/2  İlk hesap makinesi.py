
def Top(m,n):          # Def bir fonksiyon yaratmamıza imkan sağlar.
    return m+n         #Çağırıldığında belirtilen işlemi yapar yani kolaylık sağlar

def Cik(m,n):          
    return m-n

def Carp(m,n):
    return m*n

def Bol(m,n):
    return m/n 

print("Hesap makinesine hoşgeldiniz :)")
print("Lütfen Bir işlem Seçiniz:")
print("+")
print("-")
print("*")
print("/")

islem= input("İşlem:")
m= int(input())
n = int(input())

if   islem == "+":
    print("Sonuc:" , Top(m,n))

elif  islem == "-":
    print("Sonuc:" , Cik (m,n))

elif islem == "*":
    print("Sonuç:" , Carp (m,n))

elif islem == "/":
    print("Sonuç:" , Bol(m,n))

else:
     print("Hatalı Giriş")
    

