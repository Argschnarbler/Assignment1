"""
    Author: Jacob Meikle
    Date: May 23, 2013
    Last Modified by: Jacob Meikle
    Date last Modified: May 23, 2013
    Program: Adventure_0.5.py
    
    Description: 
        A comedy text based adventure game with simple choices. You must escape from south park's "Mephesto's laboratory"
        Known for cloning people and mutating animals. If you don't know what this is, 
        you should google it before playing or it wont make any sense at all.
        
    Revision History:
    
    0.4 Changes: Cleaned up code. Added a couple more comments. Increased success rate for random events.
    
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
    
"""
 ## Descision Structure ##    
 
 The functions below handle each individual 
 descision and progress through the story to the next.

"""   
    
def chooseHall():
    #descision time
    hall = ''
    while hall != 'up' and hall != 'down':
        print ('Do you want to go (up) the hallway or (down)?')
        hall = raw_input()
        
    print ('You slowly walk '+ hall +' the hall...')
    time.sleep(1)
    
    if hall == str('up'):
        # The intro was moved here so it only displays the first time.
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
    while monkey != 'slap' and monkey != 'call' and monkey != 'back':
        print('Do you (slap) the monkeys buttocks or use an animal (call)? Or go (back).')
        monkey = raw_input()
    
    if monkey == str('slap'):
        chooseSlap()
    #The player may go back from the monkey
    elif monkey == str('back'):
        print('You head back to the start...')
        chooseHall()
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
    while chomp != 'run' and chomp != 'fight' and chomp != 'save me santa!':
        print('Do you (run) or (fight) this horrible creature?')
        chomp = raw_input()
        
    if chomp == str('run'):
        chooseRun()
    elif chomp == str('save me santa!'):
        santaCheat()
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
    # 4 asses but a 50% chance go get either 2 or 4
    numSlaps = random.randrange(2, 6, 2)
    time.sleep(1)
    print'You manage to slap ' + str(numSlaps) + ' out of 4 assses.'
    time.sleep(1)
    #if failed, you may step back and try again.
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
        
"""
 ##FINAL RESULTS ##
 
 The functions below simply display the final outcomes when needed.

"""
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
    time.sleep(1)
    print('yay, you win!.')
    time.sleep(1)
    print('The End!')
    
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
    print('The monkey rips your face off!')
    time.sleep(1)
    print('You Died.')
    
def resultKick():
    time.sleep(1)
    print'You kick the monkey off, through a plate glass window.'
    time.sleep(1)
    print'You escape the lab through the broken window.'
    time.sleep(1)
    print'Unfortunatly you contracted HIV from the monkey blood on the glass.'
    time.sleep(1)
    print'20 Years later, you die.'
    time.sleep(1)
    print('You Died.')
# special santa win cheat. 
def santaCheat():
    time.sleep(1)
    print'Suddenly, a massive explosion rings your ears and a hole open up in the ceiling.'
    time.sleep(1)
    print'You see a rope drop down through the ceiling.'
    time.sleep(1)
    print'*EUUUHHH* Mutant stan is paralyzed with fear.'
    time.sleep(1)
    print'Santa slides down the rope with one hand and an M4 carbine in the other.'
    time.sleep(1)
    print('*BAM, BAM, BAM* Mutant stan falls to the ground, and you jump onto santa\'s waist.')
    time.sleep(1)
    print('A helicopter above flies you both to the safety of the north poll.')
    time.sleep(1)
    print('You enjoy blankets and coco...')
    time.sleep(1)
    print('The End!')
  
"""
    Function: main
    Purpose: This is the main function that intiates the game.
    Input: Text
    Output: Messages

"""

def main():
    
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        #game procedure
        displayIntro()
        #Start descision tree.
        chooseHall()
    
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()
