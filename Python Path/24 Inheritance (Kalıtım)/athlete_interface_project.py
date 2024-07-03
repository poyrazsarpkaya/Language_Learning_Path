
class athlete:

    def __init__(self,name,age,branch,wage):
        self.name= name
        self.age= age
        self.branch= branch
        self.wage= wage
        print("Name:",self.name,"Age:",self.age,"Branch:", self.branch,"Wage:",self.wage)

    def interest(self,interest):
        print("Zam yapıldı....")
        self.wage+= interest
        print("Name:",self.name,"New Wage:",self.wage)

    def branch_change(self,change):
        print("Branş değiştiriliyor..")
        self.branch= change
        print("Name:",self.name,"Age:",self.age,"New Branch:", self.branch)



class manager(athlete):          

    def __init__(self, name, age, branch, wage,personel_code):      #Burada kendi init fonksiyonumuzu atıyoruz yani üst kümeden almaıyoruz  bana ait olan var
        
        super().__init__(name,age,branch,wage)                      #Buda super init (Bunlar ebevyn init'e gönderilsin)
        self.personel_code= personel_code                           #ek özellik ekledik bu sınıftaki inite
        
        print(f"Personel kodları:{self.personel_code}")             #Sadece athlete sınıfı sorgusu yapan kişi name, age, branch ve wage sogularını görebilir
        super().interest(1414)                                      #manager ile yaparsak bunu yönetime kod adı ile kaydolmuş olunur
        super().branch_change("crossfit")                           #Üst Fonksiyonları burada da kulanabiliyoruz
                                                                    #Format şeklide böyle yazılıyor


mana= manager("Hun",22,"Yoga",15000,"Yog89hun")