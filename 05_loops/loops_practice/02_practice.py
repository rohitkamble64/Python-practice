# Write a program that takes a list of names and prints "Hello <name>" for each name that starts with the letter "R".

l = ["Harry", "Rohit", "Sohan", "Sachin"]

for name in l:
    if name.startswith("R"):
        print("Hello " + name)

