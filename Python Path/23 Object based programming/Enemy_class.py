import time
import random

class enemy:
    bell=100 

    def attack(self):                                 #Self,Sınıf içerisindeki bir değere ulaşılmak isteniyorsa kullanılır
        print("Cahrgeee!!")
        self.bell-=random.randint(1,100)

    def in_life(self):
        if self.bell <=0:
            print("The enemy is dead")

        else:
            print(str(self.bell)+" he has life left")

    def lobby(self):
        print("Lobby is loading....")
        time.sleep(2)

        counter = 4
        while counter == 0:
            print(counter)
            time.sleep(1)
            counter-=1


enemy1= enemy()
enemy2= enemy()
lob = enemy()


lob.lobby()
print("Let the game begin ;)")

print("Enemy1:")
time.sleep(1)
enemy1.attack()
time.sleep(1)
enemy1.in_life()
time.sleep(2)

print("Enemy2:")
enemy2.attack()
time.sleep(2)
enemy2.in_life()


