#The purpose of this program is to create a random password generator

import random
#we import this function to allow us to take variables from the char function

#Lets first name all of the character that will be allowed in the password
chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*'

#Now we want to prompt the user to tell us how many passwords we want to create
number = input('How many passwords do you want to create?')
number =int(number)

#Now we will ask for the length of the passwords
length = input('How long should the password be?')
length = int(length)

#Now we need to generate the passwords
for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
        #this appends a random character for the given length of the passwords
    print(password)
