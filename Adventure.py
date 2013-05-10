"""
    Author: Jacob Meikle
    Date: May 09, 2013
    Program: Adventure.py
    Description: A text based adventure game with simple choices.
    I reccommend you play first before you read any further or you'll spoil it!

"""

import random
import time

def displayIntro():
    print ('You have awoken in a strange laboratory.')
    print ('A thunderstorm rages outside.')
    print ('You are currently in the middle of a long hallway.')
    print ('There are strange human-like footprints travelling (up) the hall.')
def chooseHall():
    hall = ''
    while hall != 'up' and hall != 'down':
        print ('Do you want to go (up) the hallway or (down)?')
        hall = raw_input()
    return hall

def checkHall(chosenHall):
    print ('You slowly walk '+ chosenHall +' the hall...')
    time.sleep(2)
    
    if chosenHall == str('up'):
        return 'monkey'
    else:
        return 'bachomp'

    #friendlyCave = random.randint(1, 2)
def chooseMonkey():
    print('You follow the odd-shaped footsteps.')
    time.sleep(2)
    print('You come to a room and look inside.')
    time.sleep(2)
    print('*SCREECH* A four-assed monkey blocks your path.')
    time.sleep(2)
    monkey =''
    #descision time
    while monkey != 'slap' and monkey != 'call':
        print('Do you (slap) the monkeys buttocks or use an animal (call)?')
        monkey = raw_input()
    # print the final outcomes

def chooseBachomp(): 
    print('You hear a thumping noise become louder as you walk down.')
    time.sleep(2)
    print('You come to a room and look inside.')
    time.sleep(2)
    print('*EUUUUHHH* *ME STAN, BA CHOMP, BA CHEWY CHOMP!*')
    time.sleep(2)
    chomp = ''
    #descision time
    while chomp != 'run' and chomp != 'fight':
        print('Do you (run) or (fight) this horrible creature?')
        chomp = raw_input()
    
    # print the final outcomes
  
"""
    Function Main
    Purpose: This is the main function
    Input: A type of cheese
    Output: A simple message

"""

def main():
    
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        #game procedure
        displayIntro()
        #first descision
        whichHall = chooseHall()
        encounter = checkHall(whichHall)
        #second level descision
        if encounter == str('monkey'):
            chooseMonkey()
        else:
            chooseBachomp()
    
    
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()
