#ianbieg   
#dice game lab
#a game where the winner needs to roll a higher number than their opponent
#to win based of random numbers 

#getting random numbers
import random

def main():
    print('WELCOME TO A GAME OF DICE!')
    #variable creation
    endProgram = 'no'
    playerOne = 'NO NAME'
    playerTwo = 'NO NAME'
    #ask for names of players
    playerOne, playerTwo = inputnames(playerOne, playerTwo)
    #while loop to run program again
    while endProgram == 'no':
        #variables for game
        winnerName = 'NO NAME'
        p1number = 0
        p2number = 0
        winnerName = rollDice(p1number, p2number, playerOne, playerTwo, 
                              winnerName)#runs game simulation
        displayInfo(winnerName) #shows winner
        endProgram = input('Do you want to end program? (yes/no): ')
    
#this function gets the players names
def inputnames(playerOne, playerTwo):
    playerOne = input('Enter your name player one: ')
    playerTwo = input('Enter your name player two: ')
    return playerOne, playerTwo

#this function will get the random values
def rollDice(p1number, p2number, playerOne, playerTwo, winnerName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)
    if p1number == p2number:
        winnerName = 'TIE'
    elif p1number > p2number:
        winnerName = playerOne
    elif p2number > p1number:
        winnerName = playerTwo
    print(f'{playerOne} rolled {p1number}')
    print(f'{playerTwo} rolled {p2number}')
    return winnerName

#this function displays the winner
def  displayInfo(winnerName):
    if winnerName == 'TIE':
        print('ITS A TIE')
    else:
        print(winnerName, 'IS THE WINNER')

#calls main
main()
