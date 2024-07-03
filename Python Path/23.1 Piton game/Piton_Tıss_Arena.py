import time
import random


class hero:
    enemy_bell= []
    enemy_power= []

    warrior_bell = 65
    warrior_power = random.randint(30,50)
 
    tank_bell = 95
    tank_power = random.randint(20,30)
 
    magician_bell = 45
    magician_power = random.randint(45,70)
 
    assasin__bell = 55
    assasin_power = (40,65)


    def enemy_create(self):
        print("\nİşte düşman kahramanlar\n ")

        i=1
        while i<5:
          b= random.randint(40,100)
          p= random.randint(35,70)
          print(f"Enemy{i}\nBell: {b}\nPower: {p}\n")
          self.enemy_bell.append(b)
          self.enemy_power.append(p)

          i+=1



class fight(hero):

    def __init__(self,herro,ennemy):
        self.ennemy= ennemy


        if herro=="Warrior":
            
            print("Warrior: Chargegeee")
            time.sleep(1)
            print("Düşman kahraman: Attacakkkk")
            time.sleep(1)
            print("Warrior: Keskin ve sert Kılıcımın tadına bak seni pislik")
            time.sleep(1)
            print("Düşman kahraman: Belliki birileri sana tattırmış")
        

            while self.warrior_bell ==0 or self.enemy_bell[ennemy-1]==0:
              self.warrior_bell - self.enemy_power[ennemy-1]
              self.enemy_bell[ennemy-1] - self.warrior_power

            if self.warrior_bell <1:
                print("Düşman kazandı savaşçın öldü\n")
                print("Arenaya yeni bir Kahraman gönder")
            
            else:
                  print("Warrior kazandı!")
                  time.sleep(1.5)
                  print("Warrior: Dua etsinde öbür kılıcı tattırmadım")
                  time.sleep(1.5)
                  print("Magician: Mmm baya iyiydin he")
                  time.sleep(1.3)
                  print("Assasin: İyi mi?? tek yaptığı şey kılıç sallamak")
                  time.sleep(1.5)
                  print("Tank: Ben aranızda bir fark göremedim dostum")
                  time.sleep(1.5)
                  print("Assasin: Birazdan görürsün,, Dostum!.. -_-")
                  time.sleep(1.5)
                  print("Magician: Sakin olun beyler bu kadar yeter, en azından şunların icabına bakana kadar")
                  time.sleep(2)
                  print("Düşmanların Canını Okumaya Devam et!!")


        elif herro=="Magician":
            print("Magician: Hıhım, Ekpossam apialutummm!")
            time.sleep(2)
            print("Düşman kahraman: hah, women.")
            time.sleep(1)
            print("ATTACKK!!")


            while self.magician_bell ==0 or self.enemy_bell[ennemy-1]==0:
              self.magician_bell - self.enemy_power[ennemy-1]
              self.enemy_bell[ennemy-1] - self.magician_power

            if self.magician_bell<1:
                print("Düşman kazandı Büyücü öldü\n")
                print("Arenaya yeni bir Kahraman gönder")
                
            
            else:
                  print("Büyücü kazandı!")
                  time.sleep(1.5)
                  print("Assasin: Sanırım büyülendim")
                  time.sleep(1.5)
                  print("Tank: Galiba kusucam")
                  time.sleep(1.3)
                  print("Magician: Hah kolaydı.")
                  time.sleep(1.5)
                  print("Warrior: Evet öyleydi nasıl da halt ettik onları ama")
                  time.sleep(1.5)
                  print("Assasin:...")


        elif herro=="Assasin":
            print("Assasin: Hıhımm..")
            time.sleep(2)
            print("Düşman kahraman: Uuuv çok korktum. ")
            time.sleep(1)

            while self.assasin__bell ==0 or self.enemy_bell[ennemy-1]==0:
              self.assasin__bell - self.enemy_power[ennemy-1]
              self.enemy_bell[ennemy-1] - self.assasin_power

            if self.assasin__bell <1:
                print("Düşman kazandı Asssasin öldü\n")
                time.sleep(1)
                print("Arenaya yeni bir Kahraman gönder")
            
            else:
                  print("Assasin kazandı!")
                  time.sleep(1.5)
                  print("Assasin: Şimdi ne dediğimi anladın mı hantal herif")
                  time.sleep(1.5)
                  print("Tank: birleri fena halde kaşınmak istiyor galiba")
                  time.sleep(1.3)
                  print("Magician: Ne haliniz varsa görün artık.")
                  
      
        elif herro=="Tank":
            print("Tank: BEN OPTIMUS HULK PRIME Seni Ezip Geçicem")
            time.sleep(1.5)
            print("Düşman Kahraman: hah, Pekela görelim")


            while self.tank_bell ==0 or self.enemy_bell[ennemy-1]==0:
              self.tank_bell - self.enemy_power[ennemy-1]
              self.enemy_bell[ennemy-1] - self.tank_power

            if self.tank_bell <1:
                print("Düşman kazandı Tank öldü\n")
                print("Arenaya yeni bir Kahraman gönder")
            
            else:
                  print("Tank kazandı!")
                  time.sleep(1.5)
                  print("Tank: Çizik bile yok dostum çizik bile")
                  time.sleep(1.5)
                  print("Warrior: İyi iş koca adam")
                  time.sleep(1.5)
                  print("Assasin: Yani sayılır")
                  time.sleep(1.3)
                  print("Magician: Birirleri kıskandı bakıyorum")
            
        else:
            print("Olmayan bir seçim yaptın tekrardan seç")



class interface:
        
    def skills(self):
        print("Warrior: \nBell: 65 \nPower: 30 - 50\n ")
        print("Tank: \nBell: 95 \nPower: 20 - 30\n")
        print("Magician: \nBell: 45 \nPower: 45 - 70\n")
        print("Assasin: \nBell: 55 \nPower: 40 - 65\n")
        print("Savaş ya da Çık!")

    def inter(self):
        print(">>>>>>>>>>>>> Piton Tıss Arenaya Hoşgeldin Kahraman! <<<<<<<<<<<<") 
        time.sleep(2)
        print("\n))) Dud-du-du-dud  duru-rut-tut-tut  duru-riivut! (((")
        time.sleep(2)
        print("\nKarakter Özellikleri için ^Skills^")
        print("Arenada Savaşmak için ^Savas^")

    def loading(self):
        print("Rakip Kahramanlar Aranıyor...")
        time.sleep(2)
        print("Kahramanlar bulundu")
        time.sleep(1)
        print("Savaş başlıyor!")
        time.sleep(2)
        
        
    def select(self):
        a= str(input("Tercihiniz: "))
        
        if a ==("Skills"):
          self.skills()
          self.select()

        elif a ==("Savas"):
          self.loading()

        else:
          print("Yanlış girdin adam akıllı birini seç zaten 2 seçenek var")
          self.select()


    def arena(self):
        time.sleep(2)
        print("sunucu: BAYANLAR VE BAYLARRR PİTON ARENAYA HEPİNİZZ, HOŞGELDİNİZ!!")
        time.sleep(2)
        print("seyirci x: O ahmağın canını okuuu ")
        time.sleep(2)
        print("seyirci y: Hey, büyücü kadın! Bacakların çok büyüleyici")
        time.sleep(2)
        print("Tank: Burada kemiklerinin kırılmasını isteyen biri mi var ")
        time.sleep(2)
        print("Assasin: Bana bırakın")
        time.sleep(0.8)
        print("Warrior: Burada ben varken sana ne oluyor")
        time.sleep(1)
        print("sunucu: Savaş başlasınn!")
        time.sleep(2)
        print("Magician: Onu daha sonra hallederiz çocuklar \n")
        time.sleep(1)
        


i= interface()
i.inter()

s= interface()
s.select()

e= hero()
e.enemy_create()

we= interface()
we.arena()


war= str(input("Kahramanını seç: "))
ene= int(input("Düşman kahramanı seç: ")) 
fight(war,ene)

