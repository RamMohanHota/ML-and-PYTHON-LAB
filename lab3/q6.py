n=int(input("enter a no."))
temp=n
rev=0
while n!=0:
    rem=n%10
    rev=10*rev+rem
    n=n//10
if(rev==temp):
    print("palindrom")
else:
    print("not a palindrom")