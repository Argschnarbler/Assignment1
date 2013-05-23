"""
    Author: Jacob Meikle
    Date: May 16, 2013
    Program: Adventure_0.4.py
    Description: A text based adventure game with simple choices.
    
    0.3 Changes: Finished final outcomes. Reworded some things. Cleaned up code.
    
    0.2 Changes: Added 3rd descision level. Implemented 8 total final outcomes. One positive outcome is available. 
    Changed wait times to only 1 second. Optimized code structure
    
    0.1 Changes: Added 2nd descision level with 4 total final outcomes. Also created functions to handle most of the program.
                 A 3rd descision level still needs to be added. 
  

"""

import random
import time

def displayIntro():
    print ('You have awoken in a strange laboratory.')
    print ('A thunderstorm rages outside.')
    print ('You are currently in the middle of a long hallway.')
    print ('There are strange human-like footprints travelling (up) the hall.')
    
## Descision Structure ##    
    
def chooseHall():
    hall = ''
    while hall != 'up' and hall != 'down':
        print ('Do you want to go (up) the hallway or (down)?')
        hall = raw_input()
        
    print ('You slowly walk '+ hall +' the hall...')
    time.sleep(1)
    
    if hall == str('up'):
        
        print('You follow the odd-shaped footsteps.')
        time.sleep(1)
        print('You approach a room filled with half-eaten bags of gummy worms.')
        time.sleep(1)
        print('*SCREECH* A four-assed monkey blocks your path.')
    
        chooseMonkey()
    else:
       chooseBachomp()
   

def chooseMonkey():  
    
    monkey =''
    #descision time
    while monkey != 'slap' and monkey != 'call':
        print('Do you (slap) the monkeys buttocks or use an animal (call)?')
        monkey = raw_input()
    
    if monkey == str('slap'):
        chooseSlap()
    else:
        chooseCall()
  
def chooseBachomp(): 
    print('You hear a thumping noise become louder as you walk down.')
    time.sleep(1)
    print('You approach something in the hallway...')
    time.sleep(1)
    print('*EUUUUHHH* ME STAN, BA CHOMP, BA CHEWY CHOMP!')
    time.sleep(1)
    chomp = ''
    #descision time
    while chomp != 'run' and chomp != 'fight':
        print('Do you (run) or (fight) this horrible creature?')
        chomp = raw_input()
        
    if chomp == str('run'):
        chooseRun()
    else:
        chooseFight()

        
def chooseRun():
    print('You are going to attempt to run!')
    time.sleep(1)
    print('Mutant stan is running towards you...')
    time.sleep(1)
    run = ''
    #descision time
    while run != 'sprint' and run != 'zig-zag':
        print('Do you (sprint) or (zig-zag) away?')
        run = raw_input()
        
    if run == str('sprint'):
        resultSprint()
    else:
        resultZigZag()

        
def chooseFight():
    print('You decide to attack mutant stan!')
    time.sleep(1)
    print('You spot a couple weapons at your disposal.')
    time.sleep(1)
    fight = ''
    #descision time
    while fight != 'glass' and fight != 'pillow':
        print('Will you use broken (glass) or  a (pillow)?')
        fight = raw_input()
        
    if fight == str('glass'):
        resultGlass()
    else:
        resultPillow()
    
def chooseSlap():
    print'You attempt to slap the monkeys behind.'
    numSlaps = random.randint(1, 4)
    time.sleep(1)
    print'You manage to slap ' + str(numSlaps) + ' out of 4 assses.'
    time.sleep(1)
    #call next function
    
    if numSlaps == 4:
        print('The monkey pukes out a silver skeleton key.')
        time.sleep(1)
        print('You are able to unlock your way to freedom.')
        time.sleep(1)
        chooseDoor()
    else:
        print('*OUCH*, The monkey scratches your face.')
        time.sleep(1)
        print('You take a step back.')
        time.sleep(1)
        chooseMonkey()

def chooseDoor():
    print('You can see the front door. There is some red liquid oozing from underneath.')
    time.sleep(1)
    print('There might be another exit at the back of the building.')
    door = ''
    #descision time
    while door != 'front' and door != 'back':
        print('Do you want to open the (front) or try the (back) door?')
        door = raw_input()
        
    if door == str('front'):
        resultFrontDoor()
    else:
        resultBackDoor()
    
def chooseCall():
    print'You cup your hands over your mouth and attempt a monkey call.'
    time.sleep(1)
    print'*EAAAEEAHHHEAHHHH DEERRP* *COUGH* *COUGH*'
    time.sleep(1)
    print'The monkey finds you very attractive.'
    time.sleep(1)
    call = ''
    #descision time
    while call != 'pet' and call != 'kick':
        print('Will you (pet) or (kick) the poor monkey?')
        call = raw_input()
        
    if call == str('pet'):
        resultPet()
    else:
        resultKick()
 ## FINAL RESULTS ##
 
 #run
def resultSprint():
    print('Mutant stan runs after you.. *THUMP* *THUMP* *THUMP*')
    time.sleep(1)
    print('He catches you with his long arm and bashes you against the ground 20 times.')
    time.sleep(1)
    print('BA CHOMP, BA CHEWY CHOMP, BA CHEWY CHOMP!')
    time.sleep(1)
    print('You Died.')
    
def resultZigZag():
    print('Mutant stan runs after you.. *THUMP* *THUMP* *THUMP*')
    time.sleep(1)
    print('You zig too hard and *CRACK* your ankle snaps...')
    time.sleep(1)
    print('BA CHOMP, BA CHEWY CHOMP, BA CHEWY CHOMP!')
    time.sleep(1)
    print('Mutant stan eats your head.')
    time.sleep(1)
    print('You Died.')
    
#fight
def resultGlass():
    print('You grab a shard of broken glass from the floor and charge at mutant stan!')
    time.sleep(1)
    print('*EUUUUHHH* mutant stan is bleeding profusely...')
    time.sleep(1)
    print('Mutant stan grabs your neck and crushes it in a single grasp.')
    time.sleep(1)
    print('BA CHOMP, BA CHEWY CHOMP, BA CHEWY CHOMP!')
    time.sleep(1)
    print('You Died.')
    
def resultPillow():
    print('You pick up a nearby pillow and give it to mutant stan.')
    time.sleep(1)
    print('*EUUUUHHH* mutant stan is unsure of what to do with the pillow...')
    time.sleep(1)
    print('PILLOW FIGHT!  *WHOCK!*')
    time.sleep(1)
    print('Mutant stan hits your head clean off with the pillow.')
    time.sleep(1)
    print('You Died.')


#slap
#positive outcome
def resultFrontDoor():
    print('You slip the key into the front door and open it...')
    time.sleep(1)
    print('OHHHH YEAAAAH')
    time.sleep(1)
    print('The Kool-Aid man appears, and hands you a nice frosty grape beverage.')
    time.sleep(1)
    print('You both escape together.')
    time.sleep(2)
    print('yay, you win!.')
    
def resultBackDoor():
    print('You slip the key into the back door and open it...')
    time.sleep(1)
    print('You see an empty backyard before you.')
    time.sleep(1)
    print('You begin walking across the yard, towards the back fence.')
    time.sleep(1)
    print('*RUSTLE*, *RUSTLE*, *SQUEEEK* , A rabid chipmunk with 17 and 1/2 asses springs from a nearby bush!')
    time.sleep(1)
    print('He latches on to your throat, and tears out your esophagus.')
    time.sleep(1)
    print('You Died.')
    
#call
def resultPet():
    print('choosefight!')
    
def resultKick():
    print('choosefight!')
  
  
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
        #Start descision time
        chooseHall()
    
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()
