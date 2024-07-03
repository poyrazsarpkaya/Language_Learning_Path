from asyncore import write,read

"""
m= open('p.py', 'w')        #Yazma  modu
m.write(str("Merhaba eski dostum ")+str(40.5)+str(" Yıl oldu görüşmeyeli aha ah neler oldu bir bilsen!"))
m.close()
#Dosyadan çıkmazsak ekrana hiçbirşey gelmeyecektir 
"""


o=open("p.py", "r")
print(o.read())     #okuma modu  ## okuttuğumuz dosyayı yazdırıyoruz ki görelim
o.close