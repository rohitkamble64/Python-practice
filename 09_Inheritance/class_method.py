class Employee():
    a = 1 
    @classmethod  #a method which is bound to the class and not tye objectof the class
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return self.ename

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 454
print(e.a)

e.name("Rohit")
print(e.name)


e.show()
 