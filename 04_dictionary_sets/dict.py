d ={} #empty dictionary
marks = {   #key value pairs
    "Rohit" : 100,
    "Shubh" : 73,
    "Ash" : 23
}

#print(marks["Rohit"])
#print(marks.items())
#print(marks.keys())
#print(marks.values())
marks.update({"Rohit" : 99, "Rohan" : 87})
#print(marks.get("Rohan2"))  #prints none
#print(marks["Rohan2"]) #returns an error
print(marks.pop("Ash"))
