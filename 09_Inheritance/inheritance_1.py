class Employee():
    company = "Google"
    def __init__(self,name,company):
        self.name = name
        self.company = company

    def getInfo(self):
        print(f"Name is {self.name} and Company is {self.company} ")
#Multiple inheritance
class UiUx(Employee):
    job = "design"
    def design(self):
        print(f"Job is {self.job}")

class Programmer(Employee):
    language = "Python"
    def Language(self):
        print(f"Language is {self.language}")

a = Employee("Rohit", "Google")
b = Programmer("Aman", "Google")
c = UiUx("Rohan" , "Microsoft")
a.getInfo()
b.getInfo()
b.Language()
c.getInfo()
c.design()

