student_mark =(input("Please enter the mark: "))
student_mark =(student_mark)
if student_mark <= 100 and student_mark >= 80:
    print("Gred A")

elif student_mark <= 79 and student_mark >= 60:
    print("Gred B")
elif student_mark <= 59 and student_mark >= 40:
    print("Gred C")
elif student_mark <= 39 and student_mark >= 0:
    print("Failed")
else:
    print("You have input invalid mark.")
