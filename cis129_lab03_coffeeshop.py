#Ian Bieg
#Asks the user for a store order and displays the total price

#Prices and Tax variables
PERCENT = 100

salesTax = float(.06)

coffeePrice = float(5)

muffinPrice = float(4)

yetiPrice = float(5500)

shoePrice = float(9.99)

#Aquire user order MUST BE POSITIVE 

print('***********************************')
print('Welcome to Coffee and More\n'
      'How many coffees would you like at $' +\
      str(format(coffeePrice, '.2f')), 'a cup?')
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
                
print('How many muffins would you like at $' +\
      str(format(muffinPrice, '.2f')), 'a muffin?')
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

print('How many 55ft Yeti would you like at $' +\
      str(format(yetiPrice, '.2f')), 'a Yeti?')
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

print('How many horeshoes would you like at $' +\
      str(format(shoePrice, '.2f')), 'a horseshoe?')
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

print('***********************************\n')
print('***********************************')

#Total price calculation

coffeeTotal = coffeeQuantity * coffeePrice

muffinTotal = muffinQuantity * muffinPrice

yetiTotal = yetiQuantity * yetiPrice

shoeTotal = shoeQuantity * shoePrice

taxlessPrice = coffeeTotal + muffinTotal + yetiTotal + shoeTotal

taxPrice = taxlessPrice * salesTax

priceTotal = taxPrice + taxlessPrice

#Display user total and prices per item back to them
#as well as their total

print('Coffee and More reciept')
print(coffeeQuantity,'coffee at $' + str(format(coffeePrice, '.2f')), 'each: '
      '$' + str(format(coffeeTotal, '.2f')))

print(muffinQuantity,'muffin at $' + str(format(muffinPrice, '.2f')), 'each: '
      '$' + str(format(muffinTotal, '.2f')))

print(yetiQuantity, '55ft Yeti at $' + str(format(yetiPrice, '.2f')), 'each: '
      '$' + str(format(yetiTotal, '.2f')))

print(shoeQuantity, 'horseshoes at $' + str(format(shoePrice, '.2f')), 'each: '
      '$' + str(format(shoeTotal, '.2f')))

print(str((salesTax * PERCENT)) + '% tax: $' + str(format(taxPrice, '.2f')))

print('----------------------------')

print('Total: $' + str(format(priceTotal, '.2f')))

print('***********************************\n')
print('***********************************')

print('Thank you for visiting Coffee and More')
