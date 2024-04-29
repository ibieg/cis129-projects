#ian bieg
#a program that takes a number and returns it as check protected

#global sentinel value
SENTINEL = 'q'
def main():
    userinput = ''
    #while loop until done
    while userinput != SENTINEL:
        userinput = moneyNumChecker('Enter a number ("q" to quit)')#check if num
        if userinput != SENTINEL:
            checkPrinter(userinput)#print check if valid

#checks for valid input type number and chenges to 2 decimal places
def moneyNumChecker(question):
    userinput = ''
    #force number or quit
    while userinput != SENTINEL:
        userinput = input(question)
        if userinput.lower() == SENTINEL:
            return SENTINEL
        try:
            #create a float value with 2 decimal places based off number
            userinput = float(userinput)
            #do not allow negative numbers or 0
            if userinput <= 0:
                print('That is not a valid check amount')
                continue
            #money format the float
            return str(f'{userinput:,.2f}')
        except ValueError:
            print('That is not a number')
        
#prints number if it would fit on check in style of a check
def checkPrinter(userinput):
    #get length of number
    inputLength = len(userinput)
    #filter checks that are too
    if inputLength > 10:
        print('We do not cash checks that large')
        return
    else:
        #show end result of check in check protected format
        userinput = f'{userinput:*>10}'
        print(userinput)

main()
