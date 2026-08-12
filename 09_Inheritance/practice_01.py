# Create a class 2-D vector and use it to create another class representing a 3-D vector. Use the show method to display the vector in both cases.
class TwoDvector():
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"2-D vector is {self.i}i + {self.j}j")

class ThreeDvector(TwoDvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k 

    def show(self):
        print(f"3-D vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDvector(2,6)
a.show()

b = ThreeDvector(6, 8, 9)
b.show()
