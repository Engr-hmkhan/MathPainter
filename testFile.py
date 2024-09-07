import numpy as np
from PIL import Image

# Creating 3D Numpy arrays of  zeros and then replace zeros with yellow pixels.

data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0] # 255 represent full red, green, blue # 0 represent black
# print(data)

# make a red patch
# data[1:3] = [255, 0, 0]
# print(data)

#if you want to change all the rows but not all columns
# data[:, 1:3] = [255, 0, 0]
# print(data)

#if you want to change some rows and some columns
data[1:3, 1:3] = [255, 0, 0]
data[0:2, 0:2] = [100, 200, 10]
data[3:, 2:4] = [255, 255, 255]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')

