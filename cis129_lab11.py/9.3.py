#ian bieg
#creates a csv file of students and their scores for 3 attempts at a test
#and calculates the average of the 3 scores or less
import csv

def main():
    SENTINEL = 'q'
    fileHeader = ['firstname','lastname','scores','average']
    studentList = []
    userinput = ''

    #writes the csv file of student information
    with open('grades.csv', mode='w', newline = '') as grades:
        while userinput != SENTINEL:
            userinput = getStudentInfo() #get name and scores
            if userinput != 'q':
                studentList.append(userinput)
        csv.writer(grades).writerow(fileHeader)
        for item in studentList:
                csv.writer(grades).writerow(item.values())

    #reads the csv file that we created and prints in a readable format
    with open('grades.csv', mode='r', newline ='') as grades:
        t = '\t'
        print(f'{"firstname":>15}{t}{"lastname":>15}{t}'\
              f'{"scores":>15}{t}{"average":>15}')
        next(grades)
        for grade in csv.reader(grades):
            for item in grade:
                item = f'{item:>15}'
                print(item, end = t)
                
            print('')

            
#obtains first and last name of student as well as their test scores
#then calculates the average returns dictionary of student
def getStudentInfo():
    SENTINEL = 'q'
    userinput = ''
    while userinput != SENTINEL:
        print('Would you like to input a student "q" to quit '\
              'press anything to continue')
        userinput = input()
        if userinput == SENTINEL:
            return SENTINEL
        #aquire student identifiers
        student = {'firstname':'','lastname':'','scores':[],\
                   'average':''}
        student['firstname'] = input('Enter the students first name ')
        student['lastname'] = input('Enter the students last name ')
        #aquire student grades
        for x in range(3):
            userinput = getInteger('Enter a test score '\
                                   'up to 3 attempts "q" to quit')
            if userinput == SENTINEL and x > 0:
                break
            elif userinput == SENTINEL:
                print('You must enter one score')
            else:
                student['scores'] += [userinput]
        #calculates average score
        newScore = 0
        for score in student['scores']:
            newScore += score
        student['average'] = \
            f'{newScore / len(student["scores"]):.1f}%'
        return student

#get integer value only
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
