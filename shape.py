# pylint: disable=too-few-public-methods missing-module-docstring
class Shape:
    '''Base class for all shapes with common attributes and methods.
    '''
    def __init__(self, color, name):
        '''
        Initialize shape with color and name.
        '''
        self.color = color
        self.name = name
    def say_name(self):
        '''
        Return the name of the shape.
        '''
        return f"My name is {self.name}."

class Rectangle(Shape):
    '''
    Rectangle class that inherits from shape with width and height.
    '''
    def __init__(self, color, name, width, height):
        '''
        Initialize rectangle with color, name, width and height.
        '''
        super().__init__(color, name)
        self.width = width
        self.height = height
    def say_name(self):
        '''
        Return the name and type of the rectangle.
        '''
        return f"My name is {self.name} and I am a rectangle."
    def area(self):
        '''
        Calculate the area of the rectangle.
        '''
        return self.width * self.height
    def perimeter(self):
        '''
        Calculate the perimeter of the rectangle.
        '''
        return 2 * (self.width + self.height)

class Circle(Shape):
    '''
    Circle class that inherits from shape with radius.
    '''
    def __init__(self, color, name, radius):
        '''
        Initialize circle with color, name and radius.
        '''
        super().__init__(color, name)
        self.radius = radius
    def say_name(self):
        '''
        Return the name and type of the circle.
        '''
        return f"My name is {self.name} and I am a circle."
    def area(self):
        '''
        Calculate the area of the circle.
        '''
        return 3.14 * self.radius ** 2
    def perimeter(self):
        '''
        Calculate the perimeter of the circle.
        '''
        return 2 * 3.14 * self.radius
