


def main():
    with open('grades.txt', mode='r') as grades:
        print(f'{"Grades":>5}')
        for grade in grades:
            print(f'{float(grade):>5.1f}%')