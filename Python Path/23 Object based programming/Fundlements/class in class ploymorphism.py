

class calisthenics():

    def __init__ (self,name):
        self.name=name

    def Get_info(self):
        return self.name + " 3500 kcal yaktırır"
    

class bojutsu():

    def __init__(self,name):
        self.name=name
    
    def Get_info(self):
        return self.name + " 2000 kcal yaktırır"
    


calis = calisthenics("calisthenics")
bo = bojutsu("bojutsu")

spor_list=[calis,bo]

for i in spor_list:
    print(i.Get_info())




class superhero():

    def __init__(self,name,power):
        self.name=name
        self.power=power

    def __str__(self):                                                                   #Eğer ki self değeri str olarak çağırılırsa (örneğin print) bunu döndür
        return "{} {} Gücünde bir super kahramandır" .format(self.name,self.power) 

    def __len__ (self):                       #len(wal) dendiği zaman şunu ver diyoruz. Sadece integerlar içindir
        return self.power

walwerine= superhero("walwerine",3000)
print(walwerine)

print(len(walwerine))