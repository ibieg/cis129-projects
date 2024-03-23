#ian bieg
#a program that asks for the number of tickets sold in each 
#section and then displays the amount of income generated
#from ticket sales

#main
def main():
    #sections max seating capacity
    A = 300
    B = 500
    C = 200
    #price per seat (dollars)
    APRICE = 20
    BPRICE = 15
    CPRICE = 10
    #welcome message
    print('Welcome there are', A, ' setas in section A',
          B, 'seats in section B and',
          C, 'seats in section C' )
    print('Seats in section A cost $'+str(APRICE)+
          '\nSeats in section B cost $'+str(BPRICE)+
          '\nSeats in section C cost $'+str(CPRICE))
    ARevenue = sectionSubtotal('How many seats were sold in section A?',
                          A, APRICE)
    BRevenue = sectionSubtotal('How many seats were sold in section B?',
                          B, BPRICE)
    CRevenue = sectionSubtotal('How many seats were sold in section C?',
                          C, CPRICE)
    theatreTotal(ARevenue, BRevenue,CRevenue)
    

#function to get the theatre total
def theatreTotal(*args):
    totalRevenue = 0
    for x in args:
        totalRevenue += x
    return totalRevenue


#function to find the amount of money made from each section
def sectionSubtotal(question,section,price):
    seatSold = capacityCheck(question, section)
    total = seatSold * price
    print('You sold', seatSold,'seats earning $'+str(total))
    return total

#checks if seats sold is over allowed amount
def capacityCheck(question,section):
    while True:
        seatSold = getposInteger(question)
        if seatSold <= section:
            break
        else:
            print('You can only sell', section,'seats')
    return seatSold

#getInteger function to get positive integers only
def getposInteger(message):
    while True:
        print(message)
        try:
            userInput = int(input())
            if userInput < 0:
                print('Enter a positive number')
            else:
                return userInput
        except ValueError:
            print('Incorrect data entered, please re-attempt')
        

main()