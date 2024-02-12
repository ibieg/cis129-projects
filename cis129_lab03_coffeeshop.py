#Ian Bieg
#Asks the user for a store order and displays the total price

#Aquire user order

print('***********************************')
print('Welcome to Coffee and More\n'
      'How many coffees would you like?')
while True:
    try:
        coffeeQuantity = int(input())
    except:
        print('Please put in a positive number')
    else:
        if coffeeQuantity >= 0:
            break
        else:
            print('Please put in a positive number')
                
print('How many muffins would you like?')
while True:
    try:
        muffinQuantity = int(input())
    except:
        print('Please put in a positive number')
    else:
        if muffinQuantity >= 0:
            break
        else:
            print('Please put in a positive number')

print('How many 55ft Yeti would you like?')
while True:
    try:
        yetiQuantity = int(input())
    except:
        print('Please put in a positive number')
    else:
        if yetiQuantity >= 0:
            break
        else:
            print('Please put in a positive number')

print('How many horeshoes would you like?')
while True:
    try:
        shoeQuantity = int(input())
    except:
        print('Please put in a positive number')
    else:
        if shoeQuantity >= 0:
            break
        else:
            print('Please put in a positive number')

print('***********************************\n\n')
print('***********************************')

#Prices and Tax variables

salesTax = float(.06)
coffeePrice = float(5.00)
muffinPrice = float(4.00)
yetiPrice = float(5500)
shoePrice = float(9.50)

#Total price calculation

taxlessPrice = coffeeQuantity * coffeePrice + muffinQuantity * muffinPrice +\
yetiPrice * yetiQuantity + shoePrice * shoeQuantity

taxPrice = taxlessPrice * salesTax

totalPrice = taxPrice + taxlessPrice

#Display user total and prices per item
#Make floats 2 decimal places somehow!!!!!!!!!!!!!!!!!!!!!
print('Coffee and More reciept')
print(coffeeQuantity,'coffee at $' + str(coffeePrice), 'each: '
      '$' + str(coffeeQuantity * coffeePrice))

print(muffinQuantity,'muffin at $' + str(muffinPrice), 'each: '
      '$' + str(muffinQuantity * muffinPrice))

print(yetiQuantity, '55ft Yeti at $' + str(yetiPrice), 'each: '
      '$' + str(yetiQuantity * yetiPrice))

print(shoeQuantity, 'horseshoes at $' + str(shoePrice), 'each: '
      '$' + str(shoeQuantity * shoePrice))

print(str(salesTax * 100) + '% tax: $' + str(taxPrice))

print('----------------------------')

print('Total: $' + str(totalPrice))

print('***********************************')
