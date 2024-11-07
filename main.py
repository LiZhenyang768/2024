def f(a,b,c,d):
    q=-(b**3)/(27*a**3)
    w=b*c/(6*a**2)
    e=d/(2*a)
    r=c/3/a
    t=b**2/(9*a**2)
    u=((q+w-e)+((q+w-e)**2+(r-t)**3)**0.5)**(1/3)
    i=((q+w-e)-((q+w-e)**2+(r-t)**3)**0.5)**(1/3)
    x=u+i-b/3/a
    return x.real#no j

def o():
    answer=a,"x^3",b,"x^2+",c,"x",d
    answer = answer.replace("+-","-")
    print(answer)

name=input("What is your name?")
a=int(input("a :"))
b=int(input("b :"))
c=int(input("c :"))
d=int(input("d :"))
print("Hello",name.capitalize(),"I will slove the ",a,"x^3",+b,"x^2",+c,"x",+d)
print("The root of the cubic is ",f(a,b,c,d))