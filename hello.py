print("    ___SCHOOL MARKING RESULT PLATFORM___")

def get_grade(marks):
    if marks > 100 or marks < 0:
        return "Invalid input!"
    elif marks > 90:
        return "A+ pass (Outstanding)"
    elif marks > 75:
        return "A pass (Excellent)"
    elif marks >= 65:
        return "B pass (Good)"
    elif marks >= 55:
        return "C pass (Credit)"
    elif marks >= 35:
        return "S pass (Satisfactory)"
    else:
        return "fail (Needs Improvement)"

num_students = int(input("Enter the number of students: "))

results = []

for i in range(num_students):
    print(f"\n--- Student {i+1} ---")
    name = input("Enter your name: ")
    while True:
        try:
            marks = int(input("Enter your marks: "))
        except ValueError:
            print("Invalid marks! Please enter an integer.")
            continue

        grade = get_grade(marks)
        if grade == "Invalid input!":
            print("Marks should be between 0 and 100. Please try again.")
            continue  # Ask again
        else:
            print(f"{name}, you have {grade}")
            results.append((name, marks, grade))
            break  # Exit the loop and go to the next student

print("\n--- All Students' Results ---")
for idx, (name, marks, grade) in enumerate(results, 1):
    print(f"{idx}. {name}: {marks} marks - {grade}")
