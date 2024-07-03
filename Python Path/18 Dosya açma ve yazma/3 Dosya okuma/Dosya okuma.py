
try:
    
  """
  file=open("Yazılım bilgisi.txt","r")
  print(file.read())                      #Okuma moduunda açtık ve okudaklarını ekrana yazdırdık
  """


  """
  file=open("Yazılım bilgisi.txt","r")
  print(file.readline())                  
  print(file.readline())                  #Her komutta diğer satıra geçer. Note:Aralara boşluk bırakır
  print(file.readline())
  print(file.readline(6))
  """
  p=[235,45336,"oıugvh"]
  file= open("Yazılım bilgisi.txt","r")
  mile= print(file.readlines())            #İçeriği listenin içerisine alıyor     
                                          #Bir kod dosyasını okumak içinde kullanılabilir.Küçük boyutlu olmak şartıyla
 

except FileNotFoundError:
 print("not found file!")


finally:
   file.close() 
