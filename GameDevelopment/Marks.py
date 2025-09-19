from random import randint
students = []
for i in range(20):
        students.append(randint(0,100))

sets = [[],[],[]]

for student in students:
    if student <= 30:
        sets[0].append(student)
    elif student <= 69 and student >= 31:
        sets[1].append(student)
    else:
         sets[2].append(student)

print(sets)
