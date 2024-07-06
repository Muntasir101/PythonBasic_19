student_marks = int(input("Enter Your Marks: "))

if student_marks >=90 and student_marks <=100:
    print("Grade A+")
elif student_marks >=80 and student_marks <=89:
    print("Grade A")
elif student_marks >=70 and student_marks <=79:
    print("Grade A-")
elif student_marks >=60 and student_marks <=69:
    print("Grade B")
elif student_marks >=50 and student_marks <=59:
    print("Grade C")
elif student_marks >=40 and student_marks <=49:
    print("Grade D")
else:
    print("Fail")