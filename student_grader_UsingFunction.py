

def grade_calculator(marks):
    """Decide the grade based on the Marks"""
    if marks >= 95:
        return "A+"
    elif marks >= 85:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    elif marks >= 45:
        return "E"
    else:
        return "F"


students = {}
n = int(input("Enter number of students: "))

# Input student data
for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    marks = int(input("Enter marks (out of 100): "))
    grade = grade_calculator(marks)
    students[name] = {"Marks": marks, "Grade": grade}

# Print report header
print("\n Class Study Report")
print("-" * 35)

# Display each student's data
for name, info in students.items():
    print(f"Name: {name} | Marks: {info['Marks']} | Grade: {info['Grade']}")

# Calculate average marks
avg = sum(info["Marks"] for info in students.values()) / n
print("-" * 35)
print(f"Class Average: {avg:.2f}")

# Find topper
topper = max(students, key=lambda k: students[k]["Marks"])
print(f"Topper: {topper} ({students[topper]['Marks']} Marks, Grade: {students[topper]['Grade']})")

print("-" * 35)
print(" Report Generated Successfully!")
