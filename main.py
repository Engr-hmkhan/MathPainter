import numpy as np
from PIL import Image

class Canvas:
    """Object where all shapes are going to be drawn"""

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        # Creating 3D Numpy arrays of  zeros and then replace zeros with yellow pixels.

        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    # Creating 3D Numpy arrays of  zeros and then rep;ace zeros with yellow pixels.



