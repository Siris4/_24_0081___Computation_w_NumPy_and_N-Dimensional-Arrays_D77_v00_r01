import numpy as np
import matplotlib.pyplot as plt
from scipy import misc  # contains an image of a raccoon!
from PIL import Image  # for reading image files

# Create new ndarray from scratch
my_array = np.array([1.1, 9.2, 8.1, 4.7])

# Show shape of the array (number of elements in each dimension)
print("Shape of my_array:", my_array.shape)

# Accessing elements by index
print("Element at index 2:", my_array[2])

# Show dimensions of the array (number of dimensions)
print("Number of dimensions of my_array:", my_array.ndim)
