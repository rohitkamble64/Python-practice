f = open("07_File_IO/practice/file.txt")

# lines = f.readlines()
# print(lines, type(lines))
'''
line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))
'''

lines = f.readline()
while (lines != ""):
    print(lines)
    lines = f.readline()
f.close()