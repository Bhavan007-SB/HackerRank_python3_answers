student_mark_list = []
grade_list = []

for i in range(int(input())):
    name = input()
    score = float(input())
    student_mark_list.append([name,score])
    grade_list.append(score)

grade = sorted(set(grade_list))
second_lowest_grade = grade[1]

second_lowest_student_name = []

for value in student_mark_list:
      if second_lowest_grade == value[1]:
        second_lowest_student_name.append(value[0])
second_lowest_student_name.sort()

for student in second_lowest_student_name:
    print(student)
