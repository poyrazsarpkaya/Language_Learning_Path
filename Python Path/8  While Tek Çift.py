"""a =int(input("Kaça kadar çift sayı yazılsın?"))
b =-1

while a>=b:
    b+=1
    if b%2==1:
        continue
    print(b)  """   #İk deneme


"""say1= int(input("Kaça kadar yazdırsın?"))
H=-1

while say1>H:  #Tek 
    H+=1
    if say1%2==0:
        continue 
    print(H)"""    #İkinci deneme




islem = str( input("'Tek' mi yoksa 'Çift' mi yazdırsın? "))
say1 = int(input("Kaça kadar yazdırsın?"))
sayac=0

if islem== "Çift":
  while say1> sayac:
     if sayac%2 ==0:
        print(sayac)

     sayac+=1

if islem == "Tek":
    while say1>sayac:
        if sayac%2==1:
            print(sayac)

        sayac+=1 


