class Employee():
    def __init__(Self):
        print("Constructor of Employee")
    a = 1

class Manager(Employee):
    def __init__(Self):
        print("Constructor of Manager")

    def getStatus(self):
        print("Hello")
    b = 2

class Programmer(Manager):
    def __init__(Self):
        print("Constructor of Programmer")
        super().__init__()
        super().getStatus()
    c = 3

o = Employee()
print(o.a)

m = Manager()
print(m.b, m.a)

p = Programmer()
print(p.c, p.b, p.a)