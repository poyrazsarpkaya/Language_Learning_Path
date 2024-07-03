import sys
import sqlite3 as sql

try:
    androstar= sql.connect("Andromeda_Stars.db")              #Connect database or create new database
    cur = androstar.cursor()                                  # add to cursor for write in database


    def head():
       cur.execute(""" CREATE TABLE IF NOT EXISTS Andromeda_Star_List(
           Star_Name TXT,
           Star_Age_m REAL,
            Star_Size_r REAL
       )""")


    def body(A,B,C):
       s_list= [A,B,C]
       cur.execute(""" INSERT INTO  Andromeda_Star_List 
       VALUES(?,?,?)""",s_list )
       #Format methodunu bu şekilde kullanıyoruz burada
    
    def pannel():

        print("-------> Yıldız Kayıt sistemi <--------")
        x= str(input("Yıldız adı giriniz: "))
        y= float(input("Yaşını giriniz: "))
        z= float(input("Boyut bilgisi giriniz: "))
        print("Save to data in database :)")

        body(x,y,z)


    head()
    pannel()
    

except (ValueError):
    print("Value false, Try again"), pannel()


finally:
    androstar.commit()
    again=input("Yeni bir veri kaydı yapmak ister misiniz? E/H")

    if again=="E":
        pannel()
    else:
     androstar.close
     sys.exit()