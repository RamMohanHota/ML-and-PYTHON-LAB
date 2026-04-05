n = int(input("Enter how many Fibonacci numbers to print: "))

a, b = 0, 1

print("First", n, "Fibonacci numbers:")

for i in range(n):
    print(a, end=" ")
    a= b
    b=a + b