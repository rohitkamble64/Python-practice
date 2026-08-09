with open("07_File_IO/practice/file3.txt") as f:
    content = f.read()

if("python" in content):
    print("python word is present")

else:
    print("python word is not present")


