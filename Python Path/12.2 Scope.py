#LEGB
#Logical
#Enclosing
#Global
#Built-it

my_string = "sarp"
#Global

def my_func():
    my_string = "James"
    #Enclosing:Çevreleyen
    
    def my_func_2():
        
        #Local
        my_string = "Lars"
        print(my_string)
        
    my_func_2()


my_func()
print(my_string)