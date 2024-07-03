import sqlite3 as sql


table=sql.connect("Plus_üyeler.db")
cur=table.cursor()                                                                                                          # VARCHAR: Değerin İNT olduğunu söylüyoruz. 
                                                                         
                                                                                                                            # INT PRIMARY KEY: Öncelikli değer ilk bakılacak temel değer
                                                                                                                            # UNION: Bu ise koddaki ilk tablonun kategorizasyonunu temel alarak,değerleri ile ikinci tabloyu birleştiriyor.Ayrıca tabloların sütunları aynı miktarda değilse bu birleşim olmayacaktır yani verileri ele geçirmemiz uzayacaktır. Ya da başka bir yöntem yapacağız                 
def head():                                                                                                                
    cur.execute(""" CREATE TABLE IF NOT EXISTS Plus (id PRİMARY KEY, name TXT, age INT) 
    """)

    table.commit



def add_value():
    cur.execute(""" INSERT INTO Plus (id,name,age) VALUES (1,'zeynep',22) """)
    cur.execute(""" INSERT INTO Plus (id,name,age) VALUES (2,'Özge',23) """)
    table.commit


def get_value():
    cur.execute(""" SELECT * FROM Plus WHERE name LIKE '%Ze%' ; """)                                                        # LIKE: Bunun gibileri bul demek. Değerede % işsareti koyulmadılır.
    fetch=cur.fetchall

    for i in fetch:
        print(i)



add_value()
get_value()
table.close

