
def func1(func):
    print("Selamlar")
    func()
    print("Aslar")

def newfunc():
    print("Nabıyonuz")

func1(newfunc)



def fanc(a):                       # Fonksiyon içerisine fonksiyon değeri koyup çağırıyoruz
    print("heelllo")

    def fanc2():
        a()
        print("fanclandın")
    return fanc2


def hello():
    print("Hello Brolar")

value= fanc(hello)
value()



def decorator_function(func):
    
    def wrapper_function():
        
        print("wrapper started")
        
        func()
        
        print("wrapper stopped")
    
    return wrapper_function


@decorator_function                                # Bir fonksiyona Decerator fonksiyon komutu verildiğinde,
def func_new():                                    # O fonksiyon Kendi adını Dosyadaki ilk fonksiyona değer olarak veriyor
  print("hello world")
func_new()
