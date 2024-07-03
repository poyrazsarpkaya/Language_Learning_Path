
#recursion bir fonksiyonun kendi kendine çağırması

#Örnek 1
"""
def topla(list):
    total=0

    for a in list:
        total+=a
    return total

print(topla([2,4,6,7,8,8,7]))"""



#Örnek Recursion
""""
def tu(list):

    if len(list) <=0:
        return 0

    else:
        return list[0] + tu(list[1:])

print(tu([235,45,46,4363,78]))
"""


#Örnek 3 Recursion
def fak(list):
    if list == (0 or 1):
        return 1

    else:
       return list*fak(list-1)


m=int(input("Kaça kadar hesaplayalım? "))
print(fak(m))