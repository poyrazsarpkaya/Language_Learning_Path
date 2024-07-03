

class milk():
    
    def __init__(self,name,calories):
        self.name = name
        self.calories = calories


    def __str__(self):
       return str(f"{self.name} SÜTÜ {self.calories} KALORİ İÇERİYOR")
    
    def __len__(self):
        return self.calories


my_milk = milk("Meme",5000)
print(my_milk)


liste = ["sdf","sdf"]
print(len(liste))