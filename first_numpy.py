#This is my first day in the data science part of the coding challenge
#This section will introduce me to the numpy package
#It will go over basic array construction and tomorrow will focus on array operations

import numpy as np

#Now we will create out very first array
first_arr = np.array([[1,2,3], [4,5,6]])
#this is a 2 by 3 array
#lets try to print this array
print("My first array\n", type(first_arr))
#we can also print the dimensions of the array
print("Number of dimensions", first_arr.ndim)
#now we can print the shape of an array, this has the rows and the columns
print("Shape", first_arr.shape)
#lastly let's print the size of rthe array, which in the total number of elements
print ("Number of elements", first_arr.size)

#the numpy package is helpful because we often don't know the elemnts in the array
zero_arr = np.zeros((2,3))
print("Zeros", zero_arr)
#this would print a 2 by 3 array with only zeros

#say we wanted to make an array with only one other number
six_arr = np.full((3,3), 6, dtype ="complex")
#we can also do an random array
random_arr = np.random.random((2,3))

#a really cool way to index is with creating conditions for arrays
condition_arr = random_arr > 5
#will only now have elements in the array that are greater than 5
new_arr = arr[condition_arr]
