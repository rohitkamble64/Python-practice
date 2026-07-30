"""
Question:
Write a Python program to find the largest among four numbers
entered by the user.
"""

a = int(input("enter no 1: "))
b = int(input("enter no 2: "))
c = int(input("enter no 3: "))
d = int(input("enter no 4: "))

if(a>b and a>c and a>d):
    print("Greatest number is:", a)

elif(b>a and b>c and c>d):
    print("Greatest number is:", b)

elif(c>a and c>b and c>d):
    print("Greatest number is:", c)

else:
    print("Greatest number is:", d)