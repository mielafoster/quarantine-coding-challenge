#Binary search is a classic algorithm in computer science
#First we will do the binary search iteratively

#From a high level conceptual standpoint this is how the code works
#The binary search tree takes in four arguements: the array , the first and last index of the array, and the value you're looking for value in variable:
#The function works by updating the first or last index number, splitting the array in half each time

def binary_search(array, first, last, value):
    while first <= last:
        mid = first + (last-first)//2;

        if array[mid] == value:
            return mid

        elif array[mid] < value:
            first = mid + first #Now we want to update the the new index for the first number in the array, because we are spliting the array in half

        else:
            last = mid - first #Now we update the upper bound of the index of the array

    return -1 #we will return this if the element is not at all in our array


#Now we want to be able to test this

#let's first may an array
array = [1,2,3,4,5,6,7,8,9,10,11]
value = 3

#Now we are going to call our function and define it!
result = binary_search(array, 0, len(array) -1, value)

if result != -1 :
    print("Element is  in the array")
else:
    print("Element is not in the array")
