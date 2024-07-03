import sqlite3 as sql



hacktivist= sql.connect("Hacked_list_data.db")              
cur= hacktivist.cursor()                                    

                                                                                                                       # VARCHAR: Değerin İNT olduğunu söylüyoruz.                                   
def head():                                                                                                            # INT PRIMARY KEY: Öncelikli değer ilk bakılacak temel değer
    cur.execute("""CREATE TABLE IF NOT EXISTS                                                                               
    HACKLIST_2022( Persons TXT PRIMARY KEY,  
    Phone_number INT,
    Card_numbers INT,
    Valuee INT
    )""")   



def value_add():
    cur.execute(""" INSERT INTO  HACKLIST_2022 VALUES("Mustafa gezip", 536124, 979824, 5)
    """)

    cur.execute(""" INSERT INTO HACKLIST_2022 VALUES("RİTHER",4323536,6336785684,5)
    """)

    cur.execute(""" INSERT INTO HACKLIST_2022 VALUES("KATARİNA",72344534566,23214124,7) 
    """)


def get_value():
    cur.execute(" SELECT * FROM HACKLIST_2022 ")     
    kpop=cur.fetchall()                  
    print("First Values ---------------------------------------\n",kpop)                                                                                                                      
                                                                       
                                                
    cur.execute(""" UPDATE HACKLIST_2022 SET Valuee=77 WHERE Valuee=5""")            #UPDATE komutu ile güncelleme yapacağımızı belirledik. Sonra SET ile kurulacak yeni değeri ve en sonda WHERE ile güncellenecek değeri girdik
    cur.execute(""" SELECT * FROM HACKLIST_2022""")                                  
    up=cur.fetchall()
    print("Updated Values-------------------------------------\n",up)


    cur.execute(""" DELETE  FROM HACKLIST_2022 WHERE Valuee=7 """)                  #DELETE komutu ile de silme işlemini yapabiliyoruz
    cur.execute(""" DROP TBALE HACKLIST_2022 """)                                   #Tabloya Siler
    cur.execute(""" SELECT * FROM HACKLIST_2022""")
    dell=cur.fetchall()
    print("Deleted-----------------------------------------------\n",dell)




head()
value_add()
get_value()
hacktivist.commit()
hacktivist.close()     
                  
                                    


