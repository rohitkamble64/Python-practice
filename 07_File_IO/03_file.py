f= open("07_File_IO/practice/file.txt")
print(f.read())
f.close()

# The same can be written using with statement:

with open("07_File_IO/practice/file.txt") as f:
    print(f.read())

# You dont have to explicitly close the file