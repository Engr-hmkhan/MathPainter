import numpy as np
from PIL import Image

class Canvas:
    """Object where all shapes are going to be drawn"""

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        # Creating 3D Numpy arrays of  zeros and then replace zeros with given pixels.

        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, image_path):
        """convert the current array into an image file"""

        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)

class Square:
    """A square shape, can be made on a canvas object"""

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """Draws itself into the canvas object"""
        # changing a slice of the array with the new values
        canvas.data[self.x : self.x + self.side, self.y : self.y + self.side] = self.color

class Rectangle:
    """A Rectangle shape, can be drawn on a canvas object"""

    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        """Draws itself into the canvas object"""
        # changing a slice of the array with the new values
        canvas.data[self.x : self.x + self.height, self.y : self.y + self.width] = self.color

# instantiating the class canvas
canvas = Canvas(30, 40, color = (255, 255, 255))

# instantiating the square in the canvas
square = Square(5,5,10, color = (0,255,0))
square.draw(canvas)

# instantiating the Rectangle in the canvas
rectangle = Rectangle(15, 20, 10, 15, color = (255, 0, 0))
rectangle.draw(canvas)

canvas.make('canvas.png')



