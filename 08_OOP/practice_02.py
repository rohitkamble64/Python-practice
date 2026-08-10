class calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"Square of {self.num} is {self.num ** 2}")

    def cube(self):
        print(f"Cube of {self.num} is {self.num ** 3}")

    def sqrRoot(self):
        print(f"Square root of {self.num} is {self.num ** 0.5}")

a = calculator(12)
a.square()
a.cube()
a.sqrRoot()