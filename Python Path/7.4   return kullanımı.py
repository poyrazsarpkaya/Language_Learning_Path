#b^2 -4*a*c

def kok(a,b,c):
    delta=(b**2-4*a*c)
    x1 = (-b -delta**0.5/(2*a))
    x2 = (-b +delta**0.5/(2*a))

    if delta<0:
        print("Reel kökü yoktur")
        return

    else:
      return (x1, x2)
      

z=int(input("a:"))
x=int(input("b:"))
c=int(input("c:"))

print(kok(z,x,c))