class livings():

    def __init__(self):
        pass

    def breath(self):
        print("Geted the breath")

    def ate(self):
        print("ate")


class kedicikler(livings):

    def __init__(self):    
     livings.__init__(self)

    def yaralamak(self):
        print("lssssllpp")

a = kedicikler()
a.breath()
a.yaralamak()