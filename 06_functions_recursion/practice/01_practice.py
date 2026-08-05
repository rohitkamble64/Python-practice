# WAP using functions to find greatest of three numbers

def greatest_of_three(a, b, c):
    if (a > b and a > c) :
        return a
    elif (b > a and b > c):
        return b
    else:
        return c

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))    
n3 = int(input("Enter third number: "))

greatest = greatest_of_three(n1, n2, n3)
print(f"The greatest of {n1}, {n2} and {n3} is: {greatest}")