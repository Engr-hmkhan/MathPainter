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
        canvas.data[self.x : self.x + self.side, self.y : self.side] = self.color


# instantiating the class canvas

canvas = Canvas(30, 40, color = (255, 255, 255))
canvas.make('canvas.png')



