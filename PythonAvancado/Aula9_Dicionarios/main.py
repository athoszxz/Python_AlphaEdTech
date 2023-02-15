from typing import Dict


def studentSituation(name: str, grade: int) -> Dict:
    if grade > 7:
        return {'name': name, 'grade': grade, 'situation': 'Approved'}
    else:
        return {'name': name, 'grade': grade, 'situation': 'Disapproved'}


def main():
    inputName = input('Enter the name of the student: ')
    inputGrade = int(input('Enter the grade of the student: '))
    print(studentSituation(inputName, inputGrade))


if __name__ == '__main__':
    main()
