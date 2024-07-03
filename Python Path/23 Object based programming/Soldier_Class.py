
import time
import random

class warrior:

    """
    def __init__(self):                        #__init__ değikenlerin sınıfa ait olduğunu belirleyen function
        self.bell= 100
        self.bullet= 20
        self.attack_power= 70
    """
    
    def __init__(self,ibell=50,ibullet=50,attack_power=random.randint(20,100)):
        self.bell = ibell
        self.bullet = ibullet
        self.attack_power = attack_power        


    def attack(self):
        print("Attack power",self.attack_power)
        print("Cahrgeee!!")
        self.bell-= random.randint(self.bell%50,self.bell%100)
        self.bullet-= random.randint(self.bullet%50,self.bullet%100)
        self.attack_power-= random.randint(self.attack_power%20,self.attack_power%100)


    def check(self):
        if (self.bell or self.bullet or self.attack_power) <=0:
            print("Soldier Died")
            pass

        else:
            print(str(self.bell)+" he has life left")
            print(str(self.bullet)+ " you have a bullet left ")
            print("Staying power:",self.attack_power)


    def loading():   
          print("The Game Begins.....")
          time.sleep(1)
          
  


loadingg= warrior
loadingg.loading()

print("\nFor Enemy1")
for1_bell= int(input("Bell: "))
for1_bullet= int(input("Bullet: "))

print("\nFor Enemy2")
for2_bell= int(input("Bell: "))
for2_bullet= int(input("Bullet: "))

soldier1 = warrior(for1_bell,for1_bullet) 
soldier2 = warrior(for2_bell,for2_bullet)


print("Soldier1 attacking-----------------")
time.sleep(1)
soldier1.attack()
soldier1.check()
print("\n")


time.sleep(1)
print("Soldier2 attacking-----------------")
time.sleep(1)
soldier2.attack()
soldier2.check()


