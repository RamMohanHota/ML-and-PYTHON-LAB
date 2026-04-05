age = int(input("Enter your age: "))

if 0 <= age <= 12:
    print("Category: Child")
elif 13 <= age <= 19:
    print("Category: Teenager")
elif 20 <= age <= 59:
    print("Category: Adult")
elif age >= 60:
    print("Category: Senior Citizen")
else:
    print("Invalid age entered.")