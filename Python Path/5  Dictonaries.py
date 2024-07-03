#Dictionaries#
import sys


Yep={"lxst": 124, "twox": 2354}
Yep["lxsty"] = 3554                       # Dictinoray value added
print(Yep.values())
print(Yep["lxst"]+34)     


#Örnek 2
Tipbox={"ma":123, "w":234}
print(Tipbox["ma"])
#print(Tipbox[1])             #Burada bir key atıyoruz yani Yep[1] yaparak çağıramayız. 
                              #Çağıdığımmızda küme olduğundan rastgele seçip verir


                              #her keyin bir değeri olduğundan bir nevi tuple dır

#örnek3
pet=dict([("rain",80 ), ("geat",422 ), ("roe","pamlas")])
word=input("Anahtar kelime giriniz: ")

print(pet.get(word,"Anahtar eşleşmemektedir"))

print(pet["geat"]+Tipbox["ma"])



#ekstra
lamma= dict([("game",123) , ("moode",23.204) ,("jey",1348123) ])
print(lamma["moode"]+pet["rain"])


p=dict([("y",2324), (1.00,2332)])
print(p[1])                            #Küme olmadığından 1. olanı baz alır
print(p.values())


################################
print( (1,3,5)       <(1,3,7))            
print([5,6,7]        <[5.0,6.0,7.0])
print((8,9)          <(8,9,-3))
print(("a",5)        <("ab",1))         #İlk denk geldiği sağlanan olayı baz alır
