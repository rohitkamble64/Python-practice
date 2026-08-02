a = (1, 56, 83.5, "Rohit", False, "Rex")
# Tuples are immutable
num = a.count(56)
print(num)

print(len(a))

i = a.index(False)
print(i) 

print(86 in a)

repeated = a * 2
print(repeated)