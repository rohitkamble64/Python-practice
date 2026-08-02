friends = ["Apple", "Red", 7, 398.46, True, "Rohit"]

friends[0] = "Grapes" # Unlike strings, Lists are mutable

print(friends[0])
print(friends)

# List methods

numbers = [1, 4, 7, 46, 82, 41, 63]
#numbers.sort()
#numbers.reverse()
#numbers.append(89)
#numbers.insert(3, 67) #insert 67 such that its index in the list is 3
print(numbers.pop(3))
print(numbers)