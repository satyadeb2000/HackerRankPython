from __future__ import print_function
from collections import namedtuple


NumOfStudents = int(input())
StudentDetails = namedtuple('StudentDetails', input())
sum = 0.00
for counter in range(0, NumOfStudents):
    line = list(input().split())
    student = StudentDetails(*line)
    sum = sum + int(student.MARKS)
print(str(round(sum/NumOfStudents, 2)))


    



