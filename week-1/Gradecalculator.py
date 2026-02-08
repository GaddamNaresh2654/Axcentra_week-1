def calculate_grade(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 40:
        grade = "D"
    else:
        grade = "Fail"
    return avg, grade
marks = []
n = int(input("Enter number of subjects: "))
for i in range(n):
    marks.append(int(input(f"Enter marks for subject {i+1}: ")))
average, grade = calculate_grade(marks)
print("\nAverage Marks:", average)
print("Grade:", grade)
