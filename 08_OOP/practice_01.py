class Programmer:
    company = "Google"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

    def getDetails(self):
        print(self.name, self.salary, self.pincode)

Rohit = Programmer("Rohit", 1200000, 408352)
Rohit.getDetails()
