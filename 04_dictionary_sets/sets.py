e = set()  #Empty set

s = {1, 5, 7, 48, 5, 34, "Rohit"}
s.add(53)
print(s)

s1 = {1, 56, 7, 8}
s2 = {6, 7, 34, 8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2)