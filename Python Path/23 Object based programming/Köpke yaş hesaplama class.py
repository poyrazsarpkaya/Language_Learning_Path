
class Dog_age():

    age_dict = {"a":5, "b":7, "c":10, "d":15}


    def __init__(self,name,my_age,age):
        self.age = age
        self.name =name
        self.my_age = my_age


    def calculation(self):

        for key,value in self.age_dict.items():
            if key == self.name:
                if value*self.age>self.my_age:
                   result= value*self.age - self.my_age
                   self.result = result
                   return print(f"Köpken senden {self.result} yaş Daha büyük")
                
                elif self.my_age>value*self.age:
                   self.result = self.my_age - value*self.age
                   return print(f"Köpkenden {self.result} yaş daha yaşlasın.")
                    


a = input(str("Köpkenin cinsi: "))
b = int(input("Yaşın: "))
c = int(input("Köpkenin yaşı: "))

köpkem = Dog_age(a,b,c)
köpkem.calculation()
