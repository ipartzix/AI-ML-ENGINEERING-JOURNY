class Geometry:
    def area(self, a, b=0):  # useing default value we can do method overloading
        if b == 0:
            print("Circle", 3.13 * a * a)
        else:
            print("Rectangle", a * b)


obj = Geometry()
obj.area(4)
obj.area(4, 6)
