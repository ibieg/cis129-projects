#Ian Bieg
'''a program to total up the amount of bottles 
collected on a weekly basis and display the results as 
well as the amount of money made in the process'''

#Create variables
#Bottle price was stated at 10 cents
BOTTLEPRICE = .1
totalBottles = 0
todayBottles = 0
counter = 1
totalPayout = 0
keepGoing = 'y'

#While loop to continue using program user choice y or any other input
while keepGoing == 'y':
    
    #Aquire weekly amount of bottles
    while counter < 8:
        #gathers bottles each day
        todayBottles = int(input(f'Enter number of bottles on day #{counter}: '))
        #calculates weekly bottles
        totalBottles += todayBottles
        counter += 1
    
    #find weekly payout
    totalPayout = totalBottles * BOTTLEPRICE
    #display results
    print('The total number of bottles collected is', totalBottles)
    print(f'The total payed out is ${totalPayout:.1f}!')
    #ask user to continue or not
    keepGoing = input('Would you like to put in another week of bottles?(y or n): ')
    
    #reset values that are used weekly if y
    if keepGoing == 'y':
        counter = 1
        totalPayout = 0
        totalBottles = 0
