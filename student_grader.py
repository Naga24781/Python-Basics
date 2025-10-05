def grade_calculator(marks):
    """Decide the grade based on the Marks"""
    if marks >= 95:
        return "A+"
    elif marks >= 85:
        return "A"
    elif marks >=75:
        return "B"
    elif marks >=60:
        return "C"
    elif marks >=50:
        return "D"
    elif marks >=45:
        return "E"A
    else:
        return "F"

students = {}
n=int(input("Number of students:"))
for i in range(n):
    name=input(f"\nEnter a student name {i+1} :")
    marks=int(input("Enter student marks (out of 100):"))
    grade=grade_calculator(marks)
    students[name]={"Marks":marks,"Grade":grade }
print("\nClass Study Report")
print("------------------------------")
for name,info in students.items():
    print(f"Name :{name} | Marks:{info["Marks"]} |Grade:{info["Grade"]} ")
    
avg= sum(info["Marks"] for info in students.values())/n
print(f"The Total class avg is :{avg:.2f}")
topper = max(students, key=lambda k: students[k]["Marks"])
print(f"Topper: {topper} ({students[topper]['Marks']})")
