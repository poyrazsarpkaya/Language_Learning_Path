

def Gün(yas):
    if yas <=0:
        return 0

    else:
       return 365.25 + Gün(yas-1)

w=int(input("Yaşınızı Girin: "))
print(Gün(w),"Gündür hayattasın")
