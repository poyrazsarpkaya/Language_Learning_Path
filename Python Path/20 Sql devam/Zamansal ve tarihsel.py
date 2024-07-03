import sqlite3 as sql
import random
import time
import datetime
import sys


try:
  time_m=sql.connect("Tarih_ve_zaman.db")
  cur=time_m.cursor()
  
  
  def head():
      cur.execute(""" CREATE TABLE IF NOT EXISTS Table_4(Zaman REAL, Tarih TEXT,
       Key_word TEXT, Value REAL  
       
     )""")

  
  def randomvalue():
      zaman= time.time
      tarih= str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-&d %H:%M:%S'))
      keyword= "SQL"
      value= random.randrange(3,27)
  
      cur.execute(" INSERT INTO Table_4 (Zaman,Tarih,Key_word,Value) VALUES(?,?,?,?)", (zaman,tarih,keyword,value))
      time_m.commit()                                                     
                                                                        #VALUES değerleri bu şekilde de girilebiliyor
  
  head()


  i=0
  while (i<11):                 #Kadar rastgele yazdırıyor
    randomvalue()
    time.sleep(1)

    i+=1


except (ValueError, NotADirectoryError):
    print("Error")



finally:
    time_m.close
    sys.exit()