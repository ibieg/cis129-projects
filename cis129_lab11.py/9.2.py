#ian bieg   
#reads a text file named grades.txt and displays the average of those 
#values 
def main():
        with open('grades.txt', mode='r') as grades:
            print(f'{"Grades":>5}')
            classGrade = 0
            counter = 0
            #read each line and print the result
            for grade in grades:
                print(f'{float(grade):>5.1f}%')
                classGrade += float(grade)
                counter += 1
            #calculate average
            classGrade = classGrade / counter
            print(f'Class average {classGrade:.1f}%')

main()
