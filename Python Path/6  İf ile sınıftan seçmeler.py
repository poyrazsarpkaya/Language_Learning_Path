print("seçmelere hoşgeldin")
A= ("kaan","Okan", "lUcifer","Uzay")
B = ("Ahmet", "Mehmet", "Mert", "Yılda")

h = str(input("İsim Giriniz:"))


"""if h in A:
    print("Aradığın adam bu: ")

elif h in B:
    print("Adam bu: " , A in h)

else:
    print("İsim kayıtlı değil", B in h)"""

#Bir takım denemeler oldu yukarıda

if h in A:
    print("A sınıfında dostum")

elif h in B:
    print("B sınıfında dostum")

else:
    print("Yanlış yerde arıyorsun Bilader")

##############################################################

wakeup = False

if wakeup:
    print("Yes")

else:
    print("No")