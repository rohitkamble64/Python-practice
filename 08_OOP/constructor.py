class Student() :
    name = "Rohit"
    age = 20
    marks = 90

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        print("This is a dunder method which is automatically called")

    def getInfo(self):
        print(f"Name is {self.name}, age is {self.age} and marks is {self.marks}")

Rohit = Student("Rohit", 20, 95)
Rohit.getInfo()
