words = ["donkey", "bad", "stfu"]

with open("07_File_IO/practice/file.txt") as f:
    content= f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("07_File_IO/practice/file.txt", "w") as f:
    f.write(content)