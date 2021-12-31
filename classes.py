"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


r1 = Rectangle(10, 20)
print(r1.width)
r1.width = 100
print(r1.width)
"""

"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width * self.height)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

    def _lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented
"""

""" 
r1 = Rectangle(10, 20)
print(r1.area())
print(r1.perimeter())
print(str(r1))

r2 = Rectangle(10, 20)
print(repr(r2))

r1 is not r2
r1 == r2 - False


r1 = Rectangle(10, 20)
r2 = Rectangle(10,20)

print(r1 == 100) #False


r1 = Rectangle(10, 20)
r2 = Rectangle(100, 200)

print(r1 < r2)
print(r2 < r1)

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        else:
            self._width = width

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self._width, self._height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._width == other._width and self._height == other._height
        else:
            return False

    def _lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented
    
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('width must be positive')
        else:
            self.width = width

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('height must be positive')
        else:
            self.height = height

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

    def _lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


"""
r1 = Rectangle(10, 20)
print(r1.width)
r1.width = 200
print(r1.width)
r1.height = 300
print(r1.height)
print(r1)
"""

r1 = Rectangle(-10, 20)
print(r1)