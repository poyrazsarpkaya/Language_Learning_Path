
def work(day):
    if day==0:
        return 0

    else:
        return clock + work(day-1)


clock=int(input("Günde Kaç saat çalışıyorsun? "))
q=int(input("Gün sayısını giriniz: "))
print(work(q),"saat çalıştınız")