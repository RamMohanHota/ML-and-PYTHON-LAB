a= int(input("enter a no."))
if a%11==0 and a%13==0:
    print("divisible by both 11 & 13")
elif a%11:
    print("by 11")
elif a%13:
    print("by 13")
else :
    print("not")
