
double = lambda x: x*2

multiply = lambda x, y: x*y

divide = lambda x, y: x/y

students_list = ["pradeep", "aadhya", "udayani", "vinay"]
students_list.sort(reverse=True)
print('list.sort(): ', end=":")
for student in students_list:
    print(student, end=", ")
print()

students_tuple = tuple(students_list)
print('sorted(tuple): ' + str(sorted(students_tuple)))

students =  [("pradeep","A",41),
             ("udayani","D",21),
             ("vinay","C",31),
             ("aadhya","Z",71)]


sort_key = lambda stu: stu[1]


students.sort(key=sort_key, reverse=True)

for student in students:
    print(student, end=", ")
print()
