#ian bieg
#a program to find the total number of packages needed to feed attendents
#hot dogs at an event and tell the amount left 

def main():
    total = int()
    #ask for total hot dogs needed
    total = getTotalHotdogs() 
    #amount of product per package
    BUNS = 8
    DOGS = 10
    #remaining food variables
    dogsLeft = int()
    bunsLeft = int()
    #variables to show min amount of packages needed
    minDogs = int()
    minBuns = int()
    #find leftover dogs and buns
    import math
    dogsLeft = (DOGS - total % DOGS) % DOGS
    bunsLeft = (BUNS - total % BUNS) % BUNS
    #find minimm amount of packages needed
    minDogs = math.ceil(total / DOGS)
    minBuns = math.ceil(total / BUNS)
    showResult(dogsLeft, minDogs, bunsLeft, minBuns)

#getTotalHotdogs will get the amount of people attending the event and
#the amount of hotdogs you will be serving each person
def getTotalHotdogs():
    people = int()
    hotdogs = int()
    people = int(input('Enter the number of people attending the cookout: '))
    hotdogs = int(input('Enter the number of hotdogs for each person: '))
    #finds the total amount of hotdogs needed
    total = people * hotdogs
    return total

#showResult tells the user how many buns and hotdogs are needed and how many will be leftover
def showResult(dogsLeft, minDogs, bunsLeft, minBuns):
    print('Minimum packages of hotdogs needed: ',minDogs)
    print('Minimum packages of hotdog buns needed: ', minBuns)
    print('Hotdogs left over: ', dogsLeft)
    print('Hotdog buns left over: ', bunsLeft)

#run main
main()
