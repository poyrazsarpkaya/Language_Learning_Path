""" 
def emunerate(*args):       #İstediğimiz kadar değer girebiliyoruz
    print(a)

enumerate(64,47)
"""


def dict_function(**kwargs):     # Dictinories oluşturma fonksiyonu
    dicti = [kwargs]
    #dicti = []
    #dicti.append(kwargs)
    print(dicti)

dict_function(swim="100 kcal", parkour="200kcal")


def divide (a):
    return a/2


my_list = [10,124]
print((list(map(divide, my_list))))      # map: Listedekileri fonksiyonlayan komut


my_list2 = []                            # Bu da map fonksiyonu
for element in my_list:
    print(divide(element)) 


def integer(inte):
   return "20" in inte                             
    

liste = ["200","240","dfgdf20","890","124"]        # Olup Olmamasına göre True False döndürecektir
l = list(map(integer,liste))
print(l)

l2 = list(filter(integer,liste))                   # Fonksiyondaki filtreyi uygulayarak bize sonucu döndürecektir
print(l2)


numbers = lambda num:num *10                       # Lambda tek kullanımlık ve değişebilen fonksiyondur
you_list = [13,4,35,23,24]

print(list(map(lambda num:num +2 ,you_list)))