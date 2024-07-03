

"""def fak(m):
    s=1
    for a in range(1,m+1):
     s*=a
    print(s)


sayı=int(input("Kaça kadar hesaplayalım? "))

fak(sayı)"""



def dalan(m):
    k=3.14*m**2
    #print("Dairenin alanı:",k)
    return k
    #return bulunan değeri yerine koyar artık o ifade buraki işlemin sonucuna eşittir
    #örn=dalan(9)  bu ifade artık sonucuna eşit :)


o=124.3

pono=dalan(8)*15
anado=dalan(int(o))

print(pono,anado)