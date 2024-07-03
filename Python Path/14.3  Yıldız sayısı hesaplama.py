
#Görge ufku yıldızları: Bir yıldız bölegesinin en yakınındaki olası yıldız sayısıdır 
#Görge ufku yıldızları hedef uzay bölgesinin ışık yılı genişliğinin 5 katından çıkartılarak bulunur

def star(ısıkyılı):
    if ısıkyılı ==0:
        return 0
    
    else:
        return 10654829+ star(ısıkyılı-1)


year=int(input("Hedef Yıldız bölgesi genişliği: "))
gorgeyear=year*5-year
print("Görge ufkunda",star(gorgeyear),"yıldız bulunmaktadır.")




#fonksiyon her çalıştığında baştaki rakam ile fonksiyona giren rakamla toplanıyor ve 
#onda da başta girdiğimiz değer olduğundan onunla topluyor ta ki 0 olana denk