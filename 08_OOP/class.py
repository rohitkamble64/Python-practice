class Employee():
    emp_id = "156"  #Tis is a class Attribute
    salary = 1700000


    def getInfo(self):
        print(f"Name is {self.name} and ID is {self.emp_id}, salary is {self.salary}") 

    @staticmethod
    def greet():
        print("Good Morning")

Rohit = Employee()
Rohit.name = "Rohit"  #This is an instance attribute
#print(Rohit.emp_id, Rohit.salary)
Rohit.greet()
Rohit.getInfo()
#Employee.getInfo(Rohit)

'''
Rohan = Employee()
Rohan.emp_id = "157"
Rohan.greet()
print("ID of Rohan is", Rohan.emp_id)'''

    