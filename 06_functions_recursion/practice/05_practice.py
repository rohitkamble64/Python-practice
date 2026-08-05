# Write a Python function to multiply a given number by 1 to 10 and display the results.

def multiply(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

multiply(6)