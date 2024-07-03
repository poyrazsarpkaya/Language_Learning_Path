
mx = [("a","d"),("h",4),("n",5)]

for (x,y) in mx:
    print(x)

#İyi bak

rx = {"key1":"ananas", "Key2":"Elma", "Key3":"kivi"}

for key,value in rx.items():
    print(value)


x = {"a":123, "b":4234}
print(', '.join(str(key) + ', ' + str(value) for key, value in x.items()))