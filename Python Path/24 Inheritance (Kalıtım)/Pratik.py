
class uni:
    
    def __init__(self,name,surname,age,material_strength):
        self.name= name
        self.surname= surname
        self.age= age
        self.material_strength= material_strength

        self.write= print("Name:",self.name,"Surname:",self.surname,"Age:",self.age,"Material Strength:",self.material_strength)

    def power_change(self,power):
        self.material_strength= power
        print("Materal Strength (updated):",self.material_strength)



class codename(uni):

    def __init__(self,name,surname,age,material_strenght,code_name):
        
        super().__init__(name,surname,age,material_strenght)
        self.code_name= code_name
        print("Kod adı:",code_name)
        super().power_change(100)



sig_in= codename("Banu","Ozcelik",27,70000,"B123nu865")
sig_in.power_change(87634634)