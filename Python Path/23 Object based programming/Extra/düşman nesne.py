import random
import time

class enemy:
    health=110
    def attack(self):
        print("Charge")
        self.health-=random.randint(20,64)

    def check(self):
     if self.health<=0:
        print("Enemy died")

     else: 
        print("Kalan can: " +str(self.health))


enemy1=enemy()
enemy2=enemy()

print("Enemy1:")
time.sleep(2)
enemy1.attack() , time.sleep(1), enemy1.check()
time.sleep(2)
enemy1.attack() ,time.sleep(1) , enemy1.check()
 
time.sleep(5)

print("Enemy2:")
time.sleep(2)
enemy2.attack()
time.sleep(1)
enemy2.check()