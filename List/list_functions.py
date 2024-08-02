"""
students_name = ["student1", "student2", "student3", "student4"]

# access items
first_student = students_name[0]
print("first student name: ", first_student)

# add student
students_name.append("student5")

print(students_name)  # ['student1', 'student2', 'student3', 'student4', 'student5']

# remove
students_name.remove("student3")

# insert
students_name.insert(0, "student3")

print(students_name)  # ['student3', 'student1', 'student2', 'student4', 'student5']

students_number = len(students_name)
print("Total Student Number:", students_number)

# remove specific index
students_name.pop(0)

print(students_name)  # ['student1', 'student2', 'student4', 'student5']

# Loop
for name in students_name:
    print(name)


students_name.clear()
print(students_name)  # []
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
first_3 = numbers[:3]
print(first_3)  # [1, 2, 3]

last_3 = numbers[-3:]
print(last_3)  # [13, 14, 15]

middle_3 = numbers[6:9]
print(middle_3)  # [7, 8, 9]

print(numbers[7:11])  # [8, 9, 10, 11]

city_ranking = ['dhaka', 'paris', 'ny', 'london', 'delhi']
worst_city_ranking = city_ranking[-1:]
print(worst_city_ranking)  # ['delhi']

worst_city_ranking_name = worst_city_ranking[0]
print(worst_city_ranking_name)  # delhi
