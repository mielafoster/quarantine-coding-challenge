#This python program will demonstrate my knowledge of different search algorithms


#First I will implement a random searching, this is one of the least efficient algorithms
#These are good for small datasets

import random

def find(elements, value):
    while True:
        random_element = random.choice(elements)
        if random_element == value:
            return random_element
#This function loops until some element choosen at random matches the value given as input


#Now I will implement a linear search, its much more systematic looking at every item in sequence
#The enumerrate function in Python allows you to keep track of the current elements index

def find_index(elements, value):
    for index, element in enumerate(elements):
        #enumerate prints an index and the value
        if element == value:
            return index
