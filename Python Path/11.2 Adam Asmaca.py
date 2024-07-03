from time import sleep
from sys import exit



def boot():
    name = input("What's Name: ")
    welcome = f"Welcome to My Hangman game {name}"
    print(welcome)
    sleep(2)


    stick = "------------------"
    lenen = len(stick)

    counter = lenen
    while True:
        counter-=1
        result = lenen+1* - counter-1
        space = " " * result
        print(stick[:counter], stick[:counter], sep=space,)
        
   
        if counter == 0:
           break

    print(">> Hangman Game <<")

    counter = 0
    while True:
        counter +=1
        result = lenen - counter
        space = " " * result
        print(stick[0:counter],stick[:counter], sep=space)
      

        if counter == lenen:
            break
    sleep(2)
    control()



word = "SpaceRock"
result = ""

def control():
    global result

    lives = 15
    while True:

       character_left = 0

       for character in word:
         if character in result:
            character_left +=1
            print(character)


         else:
            print("-")
            

       if character_left == 9:
            print("You Win")
            break


       a = input("Please a letter: ")
       result +=a
       

       
       if a not in word:
         lives -=1
         print(f"Wrong letter \nRemaninf Life {lives}")
 
         if lives == 0:
             print("You Dead")
             break

    
boot()
