a=int(input("enter the value of  "))
b=int(input("enter the value of  "))
c=int(input("enter the value of  "))
d=int(input("enter the value of  "))
m=int(input("enter the value of  "))
n=int(input("enter the value of  "))

if (a*b)-(c*d)==0:
    print("error")
else:
    x1=(m*d)-(b*n)/(a*d)-(c*d)
    x2=(n*a)-(m*c)/(a*d)-(c*d)
    print(x1)
    print(x2)