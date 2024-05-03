

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
                    grades.write(score+'\n')
    with open('grades.txt', mode='r') as grades:
        print(grades.readlines())

def getInteger(message):
    while True:
        print(message)
        try:
            userInput = int(input())
            return userInput
        except ValueError:
            if userInput.lower() == 'q':
                return 'q'
            else:
                print('That is not a number, try again.')
