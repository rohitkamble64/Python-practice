class Employee():
    a = 1

class Manager(Employee):
    b = 2

class Programmer(Manager):
    c = 3

o = Employee()
print(o.a)

m = Manager()
print(m.b, m.a)

p = Programmer()
print(p.c, p.b, p.a)

#Multi-Level Inheritance