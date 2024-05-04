#Imani Hollie 04.30.2024
#This program takes rock, paper, or scissors and generates
#a random choice to compare and displays a win, tie, or an
#error message.

#Module 1 - main() [Imports random and Calls playGame()]
import random

#Function 1 - getScores() [Outputs]
def compMove():
    compMoves = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    return compMoves[random.randint(1, 3)]
#End Function 1

#Function 2
def userMove():
    while True:
        userMoves = input('Enter Move (Rock, Paper, Scissors): ')
        if userMoves.lower() not in ['rock', 'paper', 'scissors']:
            print('ERROR! Valid Input Includes: Rock, Paper, or Scissors')
        else:
            return userMoves.capitalize()
#End Function 2

#Function 3
def winCondition(user, comp):
    #Inputs
    winCon = {'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock',}
    #Calculations
    #IF-THEN-ELSE decisions structure will 
    if user == comp:
        return 'TIE: Try Again'
    elif winCon[user] == comp:
        return f'USER WINS: {user.lower()} beats {comp.lower()}'
    else:
        return f'COMP WINS: {comp.lower()} beats {user.lower()}'
#End Function 3

#Function 4
def rpsGame():
    #Call Functions and Declare Variables
    compSign = compMove()
    userSign = userMove()
    #Outputs
    print(f"COMP: {compSign}")
    print(f'USER: {userSign}')
    print(winCondition(userSign, compSign))
#End Function 4

#Call Function 4
rpsGame()

#End Module 1