from random import randint,shuffle



"""
while True:
 for a in list(range(30)):
    if a == 10:
     print("---Onu bulduk---\n",a)
     break

    else:
     continue
    """


for a in list(range(30,100,5)):
    print(a)


#İndexlerinide yazdırmak istiyorsan
indexx = 0
for a in list(range(30,40)):
    print(f"no:{a}, ix:{indexx}")
    indexx +=1


#İndexlerinide yazdırmak istiyorsan
for a in enumerate(list(range(30,40))):
    print(a)


#İndexlerinide yazdırmak istiyorsan
for index,value in enumerate(list(range(30,40))):
    print(index)
    print(value)


print("\n",randint(4,50), "\n")


my_list_bro = list(range(0,40))
shuffle(my_list_bro)                # Sayıları shuffle ediyor. 
print(my_list_bro)


sports = ["swimming", "spinning", "Parkour", "calisthenics"]
calories = ["100", "400", "500","2000"]
water = ["2L","4L","6L","10L"]

United = list(zip(sports,calories,water))                # Eğer ki değerler sözlük yerine bu şekilde verilmişse zip bunları birleştiriyor.
print(United)                                            # List komutu ilede liste haline getirip ekrana yazdırabiliyoruz


liste = []
words= "manalamanalaştıramadıklarımızdanmışcasına"

for element in words:                                   # Bir kelime grubundan listeye veri akatarma
    if element == "t":
        break
    else:
        liste.append(element)
        print(element)

print(liste)


new_list = []
new_list = [atom for atom in words]                    # Bir kelime grubundan listeye veri akatarma Kolay yol
print(new_list)


new_list3 = []
new_list3 = [atom for atom in list(range(80,100))]
new_list3 = [atom*5 for atom in list(range(80,100))]
print(new_list3)