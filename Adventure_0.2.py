"""
    Author: Jacob Meikle
    Date: May 09, 2013
    Program: Adventure_0.2.py
    Description: A text based adventure game with simple choices.
    
    0.1 Changes: Added 2nd descision level with final outcomes. Also created functions to handle most of the program.
                 A 3rd descision level still needs to be added. 
  

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
    #slap
    if monkey == str('slap'):
        print'You attempt to slap the monkeys behind.'
        numSlaps = random.randint(1, 4)
        time.sleep(2)
        print'You manage to slap ' + str(numSlaps) + ' out of 4 assses.'
        time.sleep(2)
        #winning event
        if numSlaps == 4:
            print('The monkey pukes out a silver skeleton key.')
            time.sleep(2)
            print('You are able to unlock your way to freedom.')
            time.sleep(2)
            print('You have escaped the lab due to your impressive ass slapping abilities.')
        else:
            print('The monkey scratches your face off.')
    else:
        #using animal call
        print'You cup your hands over your mouth and attempt a monkey call'
        time.sleep(2)
        print'*EAAAEEAHHHEAHHHH DEERRP* *COUGH* *COUGH*'
        time.sleep(2)
        print'The monkey vigoursly humps your shins.'
        time.sleep(2)
        print'You kick the monkey off, through a plate glass window.'
        time.sleep(2)
        print'You escape the lab through the broken window.'
        time.sleep(2)
        print'Unfortunatly you contracted HIV from the monkey blood on the glass.'
        time.sleep(2)
        print'20 Years late you die.'
def chooseBachomp(): 
    print('You hear a thumping noise become louder as you walk down.')
    time.sleep(2)
    print('You come to a room and look inside.')
    time.sleep(2)
    print('*EUUUUHHH* ME STAN, BA CHOMP, BA CHEWY CHOMP!')
    time.sleep(2)
    chomp = ''
    #descision time
    while chomp != 'run' and chomp != 'fight':
        print('Do you (run) or (fight) this horrible creature?')
        chomp = raw_input()
    
    # print the final outcomes
    if chomp == str('run'):
        time.sleep(2)
        print('Mutant stan runs after you.. *THUMP* *THUMP* *THUMP*')
        time.sleep(2)
        print('He catches you with his long arm and bashes you against the ground 20 times.')
        time.sleep(2)
        print('BA CHOMP, BA CHEWY CHOMP, BA CHEWY CHOMP!')
    else:
        time.sleep(2)
        print('You grab a shard of broken glass from the floor and charge at mutant stan!')
        time.sleep(2)
        print('*EUUUUHHH* mutant stan is bleeding profusely...')
        time.sleep(2)
        print('Mutant stan grabs your neck and crushes it in a single grasp.')
        time.sleep(2)
        print('BA CHOMP, BA CHEWY CHOMP, BA CHEWY CHOMP!')
        
  
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
