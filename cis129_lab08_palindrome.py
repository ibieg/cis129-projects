#ian bieg  
#determines if a word or expression can be considered a palindrome
def main():
    SENTINEL = 'q'
    palindrome = ''
    #loop question
    while palindrome != SENTINEL:
        userpalindrome = input('Enter a possible palindrome ("q" to quit)\n')
        palindrome = createFilteredPalindrome(userpalindrome)
        if palindrome != SENTINEL:
            #check for palindrome
            if isPalindrome(palindrome) == 'Invalid':
                print(isPalindrome(palindrome))
            elif isPalindrome(palindrome):
                print(f'{palindrome} is a palindrome')
            else:
                print(f'{palindrome} is not palindrome')
    #program end message
    print('Goodbye')

#determine if a word or expression can be considered a palindrome
def isPalindrome(palindrome):
    #create a list of the letters and numbers in palindrome
    palindromeList = palindromeListFiltered(palindrome)
    #checks for subjective invalid input
    if palindrome.replace(' ','') == '' or palindrome == '' \
        or palindrome.replace('\t','') == '':
        return 'Invalid'
    #check for word symmetry
    for item in range(len(palindromeList)//2):
        if palindromeList.pop() == palindromeList[item]:
            continue
        else:
            return False
    return True

#creates a list of acceptable characters for a palindrome
#lowercase alpha numeric characters
def palindromeListFiltered(palindrome):
    palindromeList = [letter for letter in (palindrome.lower()) if letter.isalnum()]
    return palindromeList

#creates a string of lowercase characters or numbers from a list
def createFilteredPalindrome(userpalindrome):
        palindrome = ''
        for letter in palindromeListFiltered(userpalindrome):
            palindrome += letter
        return palindrome

main()
