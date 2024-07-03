
def plus(key):                           #Kaça kadar toplayalım ileri versiyon :)
    if key <=0:
        return 0
    else:
        return key + plus(key-1)


a=10
print(plus(a))  
print(a)
