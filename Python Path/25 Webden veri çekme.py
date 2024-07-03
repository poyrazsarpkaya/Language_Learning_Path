import requests
from bs4 import BeautifulSoup
"""
gett= requests.get("https://www.mekansepeti.com.tr")           #Burada sitenin kaynak kodlarının alıp değişkene atıyoruz
#print(gett.content)                                           #Content içerik demek aldığı kaynağın içeriğini göstertiyoruz

supra = BeautifulSoup(gett.content)                          
print(supra.prettify)                                          #Prettify güzelleştirmek demek
#supra.find_all("a")                                           #A etiketi olan tüm satırları yazdırıyor

links = supra.find_all("a")
for link in links:                                             #a etiketi olan tüm linkleri alıyor
    print(links)
    print(link.gett("href"))                                   #Sadece linkleri alıyor yalın bir biçimde

"""

ho = requests.get("https://www.mekansepeti.com.tr")
hoo = BeautifulSoup(ho.content,"html.parser")
hoo.prettify
links = hoo.find_all("a")
for link in links:
    #print(link.get("href"))                                    # Linkleri gösteririyor
    print(link.text,link.get("href"))                           #Linklerin neye götürdüğünü gösteriyor



a = requests.get("https://www.mekansepeti.com.tr")
aa = BeautifulSoup(a.content)
aa.prettify
aaa = aa.find_all("a")
for link in aaa:
    print(link.text,link.get("href"))