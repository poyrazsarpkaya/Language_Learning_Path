
#Önemli for örneği
rey={"Ruby": "Güzel bir dil" , "bash": "Çok kritik" , "rain":"Yağmur" }

for a,i in rey.items():
    print(a+ " "+ i) 



#Önemli örnek2

lessons={"Sude":["Math"], "Nurella":["Türkish"], "Naz":["Siber güvenlik"]}

def search(a):
    while True:
      name=input("İsim Giriniz: ")
     
      if not (name in lessons):
        print("İsim bulunamadı tekrar giriniz..")
        continue

      else:
        print("{} nin aldığı dersler: ".format(name))
        for i in (lessons[name]):                              #Bu örneğe dikkat et
         return print(i) , search(a)

search(a)




lessons1={"Banu":["fizik","kimya", "sosyoloji"] , "Ezgi":["Beden Eğitimi","Ruby"]}
name1=input("Bir ad giriniz:")
print("{} nin aldığı dersler:".format(name1))

for i in (lessons1[name1]):
    print(i)