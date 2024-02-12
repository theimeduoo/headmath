from random import randint, choice
from playsound import playsound

#Define the level of difficulty of the equations.
#The two numbers on wich of the lists below represents the range
#of numbers that can be choosen by the computer to make an equation.
easy = [1,20]
medium = [1,100]
hard = [100,1000]

#Saves in a variable the level of difficulty that the user chose.
userLevelChoice = input('Choose a difficulty (easy, medium, hard): ')

#Here the numbers that will be part of the equation will be choosen randomly
#based on the level of difficulty
#Two values will be saved into the variable "numbers". They are chosen inside the range
#of the difficulty (easy, medium or hard).
def setNumbers():
    if(userLevelChoice == 'easy'):
        numbers = [randint(easy[0],easy[1]), randint(easy[0],easy[1])]

    if(userLevelChoice == 'medium'):
        numbers = [randint(medium[0],medium[1]), randint(medium[0],medium[1])]

    if(userLevelChoice == 'hard'):
        numbers = [randint(hard[0],hard[1]), randint(hard[0], hard[1])]

    return numbers

#These variable gets the value returned on setNumbers() just to make
#the code easier to understand :)
args = setNumbers()

#These are the functions that build the equations.
#They will be randomly chosen soon on the code.
#Each one returns two values when called: The result of the equation
#and a string representing the whole equation, eg.: "54 + 30".
def multiply():
    return args[0] * args[1], (str(args[0]) + '*' + str(args[1]))

def divide():
    return args[0] / args[1], (str(args[0]) + '/' + str(args[1]))

def add():
    return args[0] + args[1], (str(args[0]) + '+' + str(args[1]))

def subtract():
    return args[0] - args[1], (str(args[0]) + '-' + str(args[1]))

#Here the program starts to effectively run, it calls the function "setNumbers()"
#and the "args" variable.
#Choose randomly with operation should be done and the two values
#returned on the "equations build" part will be
#called "result" and "text" respectively.
while True:
    setNumbers()
    args = setNumbers()
    result, text = choice([add(),divide(),multiply(),subtract()])
    ask = input('How much is: ' + text + '? ')

    #Checks if the value that user inserted is the result or not
    if(ask==str(result)):
        print('Yeah! The result was ' + str(result))
        playsound('./sounds/right.mp3')

    else:
        print('Oh! The result was not ' + '"' + ask + '"' + ' but ' + str(result)) 
        playsound('./sounds/wrong.mp3')
