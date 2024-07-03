import urllib.request


url1="https://img1.goodfon.com/wallpaper/nbig/c/c0/tony-kokhan-moto-smoke.jpg"
url2="https://www.pixel4k.com/wp-content/uploads/2019/11/ducati-4k_1574943323.jpg"
url3="https://c4.wallpaperflare.com/wallpaper/127/341/265/motocross-kiss-love-moto-wallpaper-preview.jpg"


urllist=[url1,url2,url3]
say=1

for url in urllist:
    urllib.request.urlretrieve(url, str(say) + ".Fotoğraf" + ".jpg")
    say+=1




"""
#Pratik
    list=[2342]
    reurl=input("Url yi giriniz")
    sayı=1
    for rl in list:
        urllib.request.urlretrieve(reurl,sayı + ". İndirme" + "jpeg")
        sayı+=1
"""