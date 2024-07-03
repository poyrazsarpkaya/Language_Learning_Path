
with open("Yazılım_bilgisi.txt","r+") as dile:                    #r+= read and write
    m=dile.read()
    dile.seek(0)
    m="iyiyim" + m
    dile.write(m)
    dile.close()




with open("Yazılım_bilgisi.txt","r+") as kile:
    list=kile.readlines()
    list.insert(1," Siz nasılsınız? ")
    kile.seek(0)                       
    kile.writelines(list)   
    kile.close()


with open("Yamaha.css","r+") as moto:
    hoto=moto.readlines()
    hoto.insert(17,"yAMAHA motorları dünya çapında ses getirmiş ve tutumuşbir motor markasıdır \n ayrıca bakınız:")
    moto.seek(0)
    moto.writelines(hoto)
    moto.close()

with open("Wiii.txt","r+") as aim:
    l=aim.readlines()
    l.insert(8, "239rwepjfmsfkmsf")
    aim.seek(0)
    aim.writelines(l)
    aim.close()


with open("jafnaf.txt","r+") as ham:
    a=ham.read()
    ham.seek(0)
    a="asdubkahsdm"+a
    ham.write(a)
    ham.close()

with open("baszgettbOOL.txt","r+") as basket:
    bas=basket.readlines()
    bas.insert(5,"İşte gördünüz bu top bir basketbal topudur")
    ham.seek(16)
    ham.writelines(bas)
    basket.close()
 
"""
#Example
with open("remnayrer.txt","r+") as jile:
    o=jile.read()
    jile.seek(0)
    o="pomodoro"+o
    jile.write(o)


with open("yamatekutasayiiiii.txt","r+") as yamate:
    y=yamate.read()
    yamate.seek(0)
    y="yazmak istediklerim" + y
    yamate.write(y)

"""

