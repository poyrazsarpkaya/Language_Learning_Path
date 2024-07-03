
class athlete:

    def __init__(self,name,age,branch,wage):
        self.name= name
        self.age= age
        self.branch= branch
        self.wage= wage

    def athletes(self):
        print("Name:",self.name,"Age",self.age,"Branch", self.branch,"Wage",self.wage)

    def interest(self,interest):
        print("Zam yapıldı....")
        self.wage+= interest

    def branch_change(self,change):
        print("Branş değiştiriliyor..")
        self.branch= change


class manager(athlete):                                 #Burada yaptığımız şey ise sporcu sınıfını üst küme olarak almak ebevyn sınıf olarak yani
  print("Thıs is managment class")



Buse= manager("Buse",19,"Jimnastik",20000)               #Bu sayede o sınıftaki fonksiyonları bu sınıftada kullanabiliriz
Buse.athletes()
Buse.interest(300)
Buse.athletes()