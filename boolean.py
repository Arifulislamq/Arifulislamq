def check_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"

# Main program
students = {"Arif": 85, "karim": 92, "Rahim": 58}

for name, marks in students.items():
    grade = check_grade(marks)  # Function call
    print(f"{name} scored {marks} marks and got grade {grade}")
  
