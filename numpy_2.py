#This program will go over some more numpy functions
#Remember this is the faster way to do operations on arrays!

#Again first import the library
from numpy import *
import numpy as np

#Let's initalize an array
array = np.array([[1,2], [2,4]])
print(array)

#Let's find the max and the sum of the array
a = array.max()
b = array.sum()
print(a)
print(b)


#We can also create a histogram  (num, bins) = histogram(x, bins=None, range=None)
(number, bins) = histogram(array, bins = 10, range = (0,6))
print(number)
print(bins)

#its a lot like R because it allows us to directly perform operations on matricies/arrays

array_2 = np.array([[10, 20],[40, 50]])
c = array + array_2
print(c)
d = array - array_2
print(d)

#This means we can also perform for loop functions on it

for i in array_2:
    print(i * 2)

#This is a siumple for loop that doubles the numbers in the array !
