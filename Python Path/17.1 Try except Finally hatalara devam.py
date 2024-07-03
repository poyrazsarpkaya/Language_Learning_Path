
try:
    fi=open("düşman nesne.py","r")

except IOError:
    print("Böyle bir dosya yok")
  
finally:
    fi.close()       #Açsın yada açmasın her türlü kapatır. O zaman neden açtık? Yaanii bende bilmiyorum



"""
#Dosyanın olmadığı hali
try:
    fi=open("dne.py","r")

except IOError:
    print("Böyle bir dosya yok")

finally:
    fi.close()
"""