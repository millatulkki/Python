# http://nbviewer.jupyter.org/gist/manujeevanprakash/7e47301f0b50a98232ca
# Numpy tutorial
import numpy as np

# creating array using an array function
scores = [89,56, 34, 76, 89, 98]
first_arr = np.array(scores)
print(first_arr)
print(first_arr.dtype)

# nested list w/ equal lengths will be converted into a nultidimensional array
scores_l = [[34,56,23,89], [11,45,76,34]]
second_arr = np.array(scores_l)
print(second_arr)
print(second_arr.ndim) # nr of dimensions
print(second_arr.shape) # nr of rows and nr of columns
print(second_arr.dtype)

x = np.zeros(10) # an array of zeros
print(x)
print(np.zeros((4,3)))

print(np.arange(15))

print(np.eye(6)) #identity matrix

# using vectorization to perform batch operations without for loops whaaaaat
print(first_arr*first_arr)
