students = {}


def add_student():
    name = input("Enter student's name: ")
    if name not in students:
        grade = float(input(f"Enter {name}'s grade: "))
        students[name] = grade
        print(f"{name}'s grade added successfully.")
    else:
        print(f"{name} already exists in the tracker.")


def update_grade():
    name = input("Enter student's name: ")
    if name in students:
        new_grade = float(input(f"Enter new grade for {name}: "))
        students[name] = new_grade
        print(f"{name}'s grade updated successfully.")
    else:
        print(f"{name} not found in the tracker.")


def calculate_average():
    if students:
        average = sum(students.values()) / len(students)
        print(f"Average grade: {average:.2f}")
    else:
        print("No students in the tracker.")


def display_top_students():
    if students:
        top_students = sorted(
            students.items(), key=lambda x: x[1], reverse=True)
        print("Top Performing Students:")
        for i, (name, grade) in enumerate(top_students, start=1):
            print(f"{i}. {name}: {grade}")
    else:
        print("No students in the tracker.")


while True:
    print("\nStudent Grade Tracker")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Calculate Average Grade")
    print("4. Display Top Performing Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        update_grade()
    elif choice == '3':
        calculate_average()
    elif choice == '4':
        display_top_students()
    elif choice == '5':
        print("Exiting Student Grade Tracker.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
