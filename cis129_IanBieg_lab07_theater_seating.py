#ian bieg
#a program that asks for the number of tickets sold in each 
#section and then displays the amount of income generated
#from ticket sales

def main():
    #sections max seating capacity
    A = 300
    SECA = 'A'
    B = 500
    SECB = 'B'
    C = 200
    SECC = 'C'
    #price per seat (dollars)
    APRICE = 20
    BPRICE = 15
    CPRICE = 10
    #pack sections into tuples for function
    sectionA = (A, SECA, APRICE)
    sectionB = (B, SECB, BPRICE)
    sectionC = (C, SECC, CPRICE)
    #welcome message
    print('Welcome to our theatre our seating options are as follows')
    seatPrice(sectionA, sectionB, sectionC)
    #returns a list of subtotals and sections and amount of seats sold
    #along with total income
    money = seatsSold(sectionA, sectionB, sectionC)
    #displays sales information based on seats sold
    incomeOverview(money)

#function to display relevant information about sales
def incomeOverview(money):
    totalPrice, seatSection, allSoldSeats, subtotals = money
    for section in range(len(seatSection)):
        print('You made $'+ str(subtotals[section])+' in section', 
              seatSection[section], 'selling',
                allSoldSeats[section], 'seats.')
    print(f'That comes out to a total of ${totalPrice}')

#function to get amount of seats sold and show price so far
def seatsSold(*args):
    subtotals = []
    allSoldSeats = []
    seatSection = []
    totalPrice = int()
    for x in args:
        seats, section, price = x
        soldSeats = capacityCheck(f'How many seats were sold in section {section}',
                   seats)
        subtotal = (price *soldSeats)
        totalPrice += subtotal
        print(f'You\'ve made ${totalPrice} total so far')
        allSoldSeats.append(soldSeats)
        subtotals.append(subtotal)
        seatSection.append(section)
    return totalPrice, seatSection, allSoldSeats, subtotals 

#function to give seat prices and capacity
def seatPrice(*args):
    for x in args:
        seats, section, price = x
        print('There are', seats, 'seats in section', section,
          'each seat costs $' +str(price))

#checks if seats sold is over allowed amount
def capacityCheck(question,sectionseats):
    while True:
        seatSold = getposInteger(question)
        if seatSold <= sectionseats:
            break
        else:
            print('You can only sell', sectionseats,'seats')
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

#run main
main()