# Databases
# https://www.py4e.com/lessons/database
tu=(1,2,3,4,45.67,'REVA',56,89)
print(tu[::-2])
print(tu[::2])
print(tu[2:7])

student=dict()
n=int(input("number of students"))
for i in range(n):
    student_id=str(input('enter sudent_id'))
    age=int(input('enter age'))
    percentage=int(input('enter percentage'))
    student[student_id]=[age,percentage]
print(student)
for i in student:
    if student[i][1]>50:
        print((student[i][0],student[i][1]))