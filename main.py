import numpy as np
from PIL import Image

# Creating 3D Numpy arrays of  zeros and then rep;ace zeros with yellow pixels.

data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0] # 255 represent full red, green, blue # 0 represent black
print(data)

# make a red patch
data[1:3] = [255, 0, 0]
print(data)

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')

