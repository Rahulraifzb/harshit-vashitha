# class variable
# circle
# area
# circum

class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    def calc_circumference(self):
        return 2*Circle.pi*self.radius

c1 = Circle(4)
c2 = Circle(7)

print(c1.calc_circumference())
