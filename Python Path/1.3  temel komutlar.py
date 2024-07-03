from pkgutil import extend_path

print("Hello space")
a= 1
m ="3"
print (a+int(m))

value = 5
print("a =", value, sep='00000', end='\n\n\n')
print("a =", value, sep='0', end='')
print("\nanswer: ", value, sep="1. ", end="\nGreat!")


#Listeler mutable dır yani değişkendirler
J = ["\nJET ", "uçak sondası", "Nunchaku","Bojutsu"]
J = J+ ["Anatomi"]
print(J)


p="Yıldızlar arasında seyahat ederken manzara karşısında kahve keyfi "
o= p[15:-1]
ı= p[0:1]                        #Belirtilen aralığı yazdırır
print(o,ı)


wer=[34,556,8,6978,345]
del wer[0]                       #Belirtilen aralığı siler.
del wer[1:3]
print(wer)



#TUPLE

I=(2,3,5,6)                      #Tuple olduğu zaman değer değişmez.Kalıcıdır.(immutable)
#I[0]=4
print(I)


v=([23,43,67],[12,14,15])        #Tuple elemanlarını değiştirmeyiz içinde bir liste varsa onu değiştirebilriz tuple buna bakmaz
v[0][1]= 4                        #örnek:Çikoalta kutusunun içinin boş olup olmamasıyla ilgilenmez kutunun kalıcı olarak var olmasını sağlar
print(v)

T=1,2,3,4                        # Bu da bir tuple dır
print(T)



u=[2,6,8,45,4]
u.insert(3,645)             #verdiğiniz sıraya değeri ekler
print(u)


u.append(123)
print(u)

vpop=u.pop(0)               #verilen değeri siler. Ancak bu elinde komut o değeri elinde tutar 
print(vpop)                 #istediğimizde başka bir yere koyabilriz 
                            #u.pop() Sondaki değeri siler 


u.pop(0)     
u.remove(8)                 #hangi değeri sileyim?
print(u)                    #u.discard  hata vermeden çalışır


print(u.index(45))       #Kaçıncı sırada olduğunu bulmaya yarıyor
u.append(123)
print(u.count(123))      #Şu değerden kaç tane var?

u2=[7,69,60]
u.extend(u2)             #Bunları listeye ekledi, içindeki tüm değerleri
print(u)                 #Neden append yapmıyoruz? yapalım da alt kümesi olarak alsın
                         #append komutu sadece verilen değeri atar yani bir değer atar

"""u2=[7,6,69]
u.upgrade(u2)
print(u)
#Kümeyi upgrade edebilirsin listeyi değil
""" 

u2.sort()                 # sort sıralar küçükten büyüğe doğru
print(u2)

Ters=[234,65,23,45]
Ters.reverse()            #Tersten sırlar
del Ters[0]
print(Ters)                 

u.clear( )                #Temizler
print(u)


pi=[234,345,36,34]
p2=pi.copy()              #copy() dediğimizde asıl listeden bir tane daha oluşturulur ve değişkene bağlanır
p2.append(1)
print(pi)
print(p2)

my_name= "Uvuvuvuvuvn"
my=my_name.upper()
print(my)

my_surname= my_name * 7
print(my_surname)

#syntax:Söz dizimi  vaild:geçerli invaild:geçersiz
