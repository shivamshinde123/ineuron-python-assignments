import numpy as np

class Parent:

    def input_sides(self):

        side1 = int(input("Enter the length of first side"))
        side2 = int(input("Enter the length of second side"))
        side3 = int(input("Enter the length of third side"))

        return side1, side2, side3

    
class Subclass(Parent):

    def calculate_area(self):

        side1, side2, side3 = super().input_sides()

        s = (side1 + side2 + side3)/2

        return (s*(s-side1)*(s-side2)*(s-side3))**0.5

    

if __name__ == '__main__':

    obj = Subclass()
    area = obj.calculate_area()

    print(f"Area of triangle: {np.round(area,2)} sq.units")
