name = "Have a great day!"

f= open("07_File_IO/myfile.txt", "a")  #append mode
f.write(name)
f.close()