#ian bieg
#a program that asks for the number of tickets sold in each 
#section and then displays the amount of income generated
#from ticket sales

def main():
    #sections and their max seating capacity
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
    money = seatsSold(sectionA, sectionB, sectionC)
    #displays sales information 
    moneyOverview(money)

#function to print seat prices and capacity
def seatPrice(*sections):
    #prints for each section data
    for x in sections:
        seats, section, price = x
        print('There are', seats, 'seats in section', section,
          'each seat costs $' +str(price))
    
#function to display relevant information about sales
def moneyOverview(money):
    #unpack tuple of lists
    totalPrice, seatSection, allSoldSeats, subtotals = money
    for section in range(len(seatSection)):
        #displays the section data for each section from the lists in order
        print('You made $'+ str(subtotals[section])+' in section', 
              seatSection[section], 'selling',
                allSoldSeats[section], 'seats.')
    #prints the total income of sales
    print(f'That comes out to a total of ${totalPrice}.')

#function to find amount of seats sold and money made per section
def seatsSold(*sections):
    #lists for storage
    subtotals = []
    allSoldSeats = []
    seatSection = []
    totalPrice = int()
    #runs for amount of sections in theatre
    for x in sections:
        #unpack section data
        seats, section, price = x
        soldSeats = capacityCheck(f'How many seats were sold in section {section}?',
                   seats)#checks if a positive number then if it is over seat limit
        #section subtotal
        subtotal = (price * soldSeats)
        #total cumulative
        totalPrice += subtotal
        print(f'You\'ve made ${totalPrice} total so far.')
        #store input into lists and subtotals and their respective sections
        allSoldSeats.append(soldSeats)
        subtotals.append(subtotal)
        seatSection.append(section)
    #returns total money made and lists
    return totalPrice, seatSection, allSoldSeats, subtotals 

#checks if seats sold is over allowed amount
def capacityCheck(question,sectionseats):
    while True:
        seatSold = getposInteger(question)
        if seatSold <= sectionseats:
            break
        else:
            print('You can only sell', sectionseats,'seats.')
    return seatSold

#getInteger function to get positive integers only
def getposInteger(message):
    while True:
        print(message)
        try:
            userInput = int(input())
            if userInput < 0:
                print('Enter a positive number.')
            else:
                return userInput
        except ValueError:
            print('That is not a number, try again.')

#run main
main()
