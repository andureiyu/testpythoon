class Shape:
    def __init__(self, *sides):
        self.sides = sides

    def printArea(self):
        num_sides = len(self.sides)
        
        if num_sides == 1:
            radius = self.sides[0] / 2
            area = 3.14159 * radius ** 2
            print(f"{area:.1f}")
        elif num_sides == 3 and len(set(self.sides)) == 1:
            side = self.sides[0]
            area = (1.73205 / 4) * side ** 2  
            print(f"{area:.1f}")
        elif num_sides == 4 and len(set(self.sides)) == 1:
            side = self.sides[0]
            area = side ** 2
            print(f"{area:.1f}")
        else:
            print("Shape Area Error!")
