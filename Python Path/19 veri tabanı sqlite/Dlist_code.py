
import sys
import sqlite3 as sql


try: 
   deadfile=sql.connect("Dead_List.db")
   cur=deadfile.cursor()
   
   def head():
        cur.execute (""" CREATE TABLE IF NOT EXISTS Deads_List( Dead_Humans TXT, Age INT
        
        )""")
   
   def body():
       cur.execute (""" INSERT INTO  Deads_List VALUES (Mvictor , 28
       
       )""")

   head()
   body()

except ValueError:
    print("Value error, re-enter bro")


finally:
    deadfile.commit()
    deadfile.close()
    sys.exit()