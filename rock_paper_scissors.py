#This is a game to simulate rock paper scissors game

from random import randint
#We are importing randint from the random module that the computer will play with

#First we need to create a list of play options the options are as follows
t = ["Rock", "Paper", "Scissors"]
#For each turn now you can make three possible plays

#Now we need to set up the players, you will be playing aganist the computer

#The goal now is to assign a random play to the computer
computer_player = t[randint(0,2)]

#The randint function returns an integer wihtin a given range paramters
#We assign it to t because now all of these integers will be represented by integers 0 to 2

player = False
#We intitally set the player equal to false becuase we want to perform a function First

#Now we will create a while loop, the computer waits for you to decide

while player == False:
#this will run as soon as you choose your play
    player = raw_input("Rock, Paper, Scissors?")
    if player == computer_player:
        print("You tied!")
    elif player == "Rock":
        if computer_player == "Paper":
            print("You lose!", computer_player, "covers", player)
        else:
            print("You win!", player, "smashes", computer_player)
    elif player == "Paper":
        if computer_player == "Scissors":
            print("You loose!", computer_player, "cuts", player)
        else:
            print("You win!", player, "covers", computer_player)
    elif player == "Scissors":
        if computer_player == "Rock":
            print("You loose!", computer_player, "smashes", player)
        else:
            print("You win!", player, "cut", computer_player)
    else:
        print("Check the spelling of the play!")
    #We set the player equal to false again so that the game continues forever
    player = False
    computer_player = t[randint(0,2)]
    #rename the variable so that its in the while loop
