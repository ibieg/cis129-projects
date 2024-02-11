#Ian Bieg
#Asks the user for a store order and displays the total price

#Aquire user order

print('***********************************')
print('Welcome to Coffee and More\n'
      'How many coffees would you like?')
coffeeQuantity = int(input())

print('How many muffins would you like?')
muffinQuantity = int(input())

print('***********************************\n\n')
print('***********************************')

#Prices and Tax

salesTax = float(.06)
coffeePrice = float(5.00)
muffinPrice = float(4.00)

#Total price calculation

taxlessPrice = coffeeQuantity * coffeePrice + muffinQuantity * muffinPrice

taxPrice = taxlessPrice * salesTax

totalPrice = taxPrice + taxlessPrice

#Display user total and prices per item
#Make floats 2 decimal places somehow!!!!!!!!!!!!!!!!!!!!!
print('Coffee and More reciept')
print(coffeeQuantity,'coffee at $' + str(coffeePrice), 'each: '
      '$' + str(coffeeQuantity * coffeePrice))

print(muffinQuantity,'muffin at $' + str(muffinPrice), 'each: '
      '$' + str(muffinQuantity * muffinPrice))

print(str(salesTax * 100) + '% tax: $' + str(taxPrice))

print('----------------------------')

print('Total: $' + str(totalPrice))

print('***********************************')
