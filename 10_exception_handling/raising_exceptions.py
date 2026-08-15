a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if(b == 0):
    raise ZeroDivisionError("Hey you cannot divide a number by zero")

else:
    print(f"The division a/b is {a/b}")