#ian bieg

import csv

def main():
    SENTINEL = 'q'
    fileHeader = ['firstname','lastname','scores']
    studentList = []
    userinput = ''

    #with open('grades.csv', mode='w', newline = '') as grades:
        #while userinput != SENTINEL:
            #userinput = getStudentInfo()
            #if userinput != 'q':
                #studentList.append(userinput)
        #csv.writer(grades).writerow(fileHeader)
        #for item in studentList:
                #csv.writer(grades).writerow(item.values())

    with open('grades.csv', mode='r', newline ='') as grades:
        t = '\t'
        print(f'{"firstname":>15}{t}{"lastname":>15}{t}{"scores":>15}')
        next(grades)
        for grade in csv.reader(grades):
            for item in grade:
                item = f'{item:>15}'
                print(item, end = t)
                
            print('')

            

def getStudentInfo():
    SENTINEL = 'q'
    userinput = ''
    while userinput != SENTINEL:
        print('Would you like to input a student "q" to quit '\
              'press anything to continue')
        userinput = input()
        if userinput == SENTINEL:
            return SENTINEL
        student = {'firstname':'','lastname':'','scores':[]}
        student['firstname'] = input('Enter the students first name ')
        student['lastname'] = input('Enter the students last name ')
        for x in range(3):
            userinput = getInteger('Enter a test score up to 3 attempts "q" to quit')
            if userinput == SENTINEL and x > 0:
                break
            elif userinput == SENTINEL:
                print('You must enter one score')
            else:
                student['scores'] += [userinput]
        return student


#def checkname

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