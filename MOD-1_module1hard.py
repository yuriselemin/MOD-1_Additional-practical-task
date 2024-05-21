
# Дополнительное практическое задание по модулю: "Базовые структуры данных."




stud_dict = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
stud_list = list(students)
stud_list.sort()

stud_dict[stud_list[0]] = sum(grades[0]) / len(grades[0])
stud_dict[stud_list[1]] = sum(grades[1]) / len(grades[1])
stud_dict[stud_list[2]] = sum(grades[2]) / len(grades[2])
stud_dict[stud_list[3]] = sum(grades[3]) / len(grades[3])
stud_dict[stud_list[4]] = sum(grades[4]) / len(grades[4])

# print(stud_list)
print(stud_dict)




