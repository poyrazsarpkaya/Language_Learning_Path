
from multiprocessing import *
import sqlite3 as sql



hacktivist= sql.connect("Hacked_list.db")                #Connect database or create new database
cur= hacktivist.cursor()                                 # add to cursor for write in database


def head():                                              #IF NOT EXISTS: tablo yoksa oluştur varsa oluşturma
    cur.execute("""CREATE TABLE IF NOT EXISTS           
    HACKLIST_2022( Persons TXT,
    Phone_number INT,
    Card_numbers INT
    )""")   

    hacktivist.commit()                                      #burada verileri databasemize işliyoruz


def value_add():
    cur.execute(""" INSERT INTO  HACKLIST_2022
    VALUES(
        "Mustafa gezip",
        5367127841124,
        9734023829824
    )
    """)

    hacktivist.commit()
    hacktivist.close()



head()
value_add()
                  
                  
                                    


