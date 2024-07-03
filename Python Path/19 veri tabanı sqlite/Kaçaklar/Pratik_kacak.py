
import sys
import sqlite3 as sql


try:
    kacak_list= sql.connect("Kacak.db")
    cur= kacak_list.cursor()


    def head():
        cur.execute(""" CREATE TABLE IF NOT EXISTS Kacak_Ogrenci(
        Ad TEXT,
        Soyad TEXT,
        Numara INT,
        Sınıf REAL
        )
        """)
        kacak_list.commit()
    
    
    def body(a,s,n,sınıf):
        value_list= [a,s,n,sınıf]
        cur.execute(""" INSERT INTO Kacak_Ogrenci VALUES(?,?,?,?)""", value_list)

        print("Ad: {} soyad: {} numara: {} sınıf: {} olarak kaydedildi".format(a,s,n,sınıf))
        kacak_list.commit()
        


    def pannel():
        a= str(input("Kaçak adı giriniz: "))
        s= str(input("Kaçak soyadı giriniz: "))
        n= int(input("Kaçağın numarası:"))
        sınıf= str(input("Sınıfı: "))

        head()
        body(a,s,n,sınıf)
        
    
    pannel()


except ValueError:
    print("Hatalı bir değer girdin")
    pannel()

finally:
    kacak_list.close
    sys.exit()