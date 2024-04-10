#ian bieg  
#determines if a word or expression can be considered a palindrome
def main():
    SENTINEL = 'q'
    palindrome = str()
    #loop question
    while palindrome != SENTINEL:
        palindrome = input('Enter a possible palindrome ("q" to quit)\n')
        if palindrome != SENTINEL:
            isPalindrome(palindrome)
    print('Goodbye')

#determine if a word or expression can be considered a palindrome
def isPalindrome(palindrome):
        palindromeList = []
        #remove formatting characters for numbers
        modPalindrome = palindrome.replace(' ','')
        modPalindrome = modPalindrome.replace(',','')
        modPalindrome = modPalindrome.replace('.','')
        #create list of letters in palindrome(lowercase)
        palindromeList += modPalindrome.lower()
        #triggers if user enters nothing or formatting only
        if modPalindrome == '':
            print('The nothingness awaits')
            return
        #triggers if word or expression is a questionable palindrome
        if len(palindromeList) == 1:
            print('Can a singular letter or number really be considered a palindrome?')
        #checks if the last letter of the word is the same as the first until the middle
        for item in range(len(palindromeList)//2):
            if palindromeList.pop() == palindromeList[item]:
                continue
            else:
                print(f'{palindrome} is not a palindrome')
                return
        print(f'{palindrome} is a palindrome')


main()