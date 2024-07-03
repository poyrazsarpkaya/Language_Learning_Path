import sqlite3 as sql



hacktivist= sql.connect("Hacked_list_data.db")                #Connect database or create new database
cur= hacktivist.cursor()                                      # add to cursor for write in database


def head():                                                   #IF NOT EXISTS: tablo yoksa oluştur varsa oluşturma
    cur.execute("""CREATE TABLE IF NOT EXISTS           
    HACKLIST_2022( Persons TXT,
    Phone_number INT,
    Card_numbers INT,
    Valuee INT
    )""")   

    hacktivist.commit()                                       #burada verileri databasemize işliyoruz


def value_add():
    cur.execute(""" INSERT INTO  HACKLIST_2022
    VALUES(
        "Mustafa gezip",
        5367127841124,
        9734023829824,
        5
    )""")

    hacktivist.commit()


def get_value():
    cur.execute(" SELECT * FROM HACKLIST_2022 WHERE valuee = 5 ")      #Example: SELECT table5 FROM HACKLIST_2022 
    kop=cur.fetchall()                                                 #Alınan değerleri değişkene atar fetchall
                                                                     
    for i in kop:                                                      #example an good
        print(i)                                                       #for i in kop[:1]:
                                                                       #print(i)


head()
value_add()
get_value()
hacktivist.close()     
                  
                                    


