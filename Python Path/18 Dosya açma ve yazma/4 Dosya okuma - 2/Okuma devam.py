
"""
with open("piton_metin.txt","w") as fork:                          #open("erksdkn.txt","w") ile fork olarak
 print(fork.write("yazılımlaştıramadıklar"))                   #Yani başta yazdığımız fonksiyonu değişkenine bağlıyor

"""


with open("Piton_metin.txt","r") as file:
    file.seek(12)                             # karakterden sonrasını oku diyoruz en sonda yazdırıyoruz
    print(file.read())
    print(file.read(7))

    file.seek(9)
    urm=file.read(8)
    file.seek(6)
    urm2=file.read(4)
    print(urm,urm2)

file.close()
    