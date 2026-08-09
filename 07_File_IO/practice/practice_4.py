word = "Donkey"

with open("07_File_IO/practice/file2.txt","r") as f:
    content= f.read()

contentNew = content.replace(word, "#####")

with open("07_File_IO/practice/file2.txt", "w") as f:
    f.write(contentNew)