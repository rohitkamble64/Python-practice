# Write a program that takes a number from the user and prints the multiplication table for that number in reverse order from 10 to 1.

n = int(input("Enter a number: "))

for i in range(10, 0, -1):
    print(f" {n} x {i} = {n*i}")