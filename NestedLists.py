from __future__ import print_function


if __name__ == '__main__':
    gradeList = []
    for _ in range(int(input("Enter number of students: "))):
        name = input("Enter Name: ")
        score = float(input("Enter grade: "))
        gradeList.append([name, score])
        

    secondLowest = sorted(set([marks for name, marks in gradeList]))[1]
    print('\n'.join([a for a,b in sorted(gradeList) if b == secondLowest]))
    
