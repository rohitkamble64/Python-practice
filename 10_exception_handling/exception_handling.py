try:
    a = int(input("Enter a number: "))
    print(a)

except ValueError as v:
    print(v)
    print("Please enter a valid number")

except Exception as e:
    print(e)

else:
    print("Thank you") #This is executed only if try was successfull