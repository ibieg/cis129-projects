#ian bieg

def main():
    SENTINEL = 'q'
    gradeList = []
    userinput = ''
    with open('grades.txt', mode='w') as grades:
        while userinput != SENTINEL:
            userinput = getInteger('Enter a grade "q to quit"')
            if userinput != 'q':
                gradeList.append(userinput)
            if userinput == 'q':
                print(sum(gradeList)/len(gradeList))
                for score in gradeList:
                    grades.write(str(score)+'\n')

def getInteger(message):
    while True:
        print(message)
        try:
            userInput = input()
            userInput = int(userInput)
            return userInput
        except ValueError:
            if userInput == 'q':
                return 'q'
            else:
                print('That is not a number, try again.')

main()