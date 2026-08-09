with open ("07_File_IO/practice/poem.txt") as f:
    content = f.read()

    if("twinkle" in content.lower()):
        print("Twinkle is present in the file")

    else:
        print("Twinkle is not present in the file")

