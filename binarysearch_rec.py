#This demonstrates my knowledge of binary search trees, however this method does the search recursively
#The recursive function is defined as a routine that calls itself directly or indirectly
#I first define a base case that defines the point of termination

def rec_binarysearch (array, first_el, last_el, value):
    if first_el <= last_el:
        #now we need to define the base case, the based case is what mid is defined as

        mid_el = 1 + ((last_el- 1)//2)
        #now we define the middle index!

        if array[mid_el] == value:
            return mid_el

        elif array[mid_el] > value:
            return rec_binarysearch(array, first_el, mid_el - 1, value)
            #everytime we recall the function and it iterates down until the first and last element equal each other

        else:
            return rec_binarysearch(array, mid_el + 1 , last_el, value)
    else:
        return -1

#We can use the same test case that was used in binary_search_it.py
