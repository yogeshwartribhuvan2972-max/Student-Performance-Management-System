import csv
import os

filename = "students.csv"


def load_students():
    students = []

    if os.path.exists(filename):
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["marks"] = int(row["marks"])
                row["attendance"] = int(row["attendance"])
                students.append(row)

    return students


def save_students(students):
    with open(filename, mode="w", newline="") as file:
        fieldnames = ["name", "marks", "attendance", "grade", "status"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for student in students:
            writer.writerow(student)


def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "D"


def pass_fail(marks):
    if marks >= 35:
        return "Pass"
    return "Fail"


students = load_students()


def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    attendance = int(input("Enter attendance %: "))

    student = {
        "name": name,
        "marks": marks,
        "attendance": attendance,
        "grade": calculate_grade(marks),
        "status": pass_fail(marks)
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No student records found.\n")
        return

    print("\n--- Student List ---")

    for student in students:
        print(student)

    print()


def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found:")
            print(student)
            print()
            return

    print("Student not found.\n")


def update_marks():
    name = input("Enter student name to update marks: ")

    for student in students:
        if student["name"].lower() == name.lower():
            new_marks = int(input("Enter new marks: "))

            student["marks"] = new_marks
            student["grade"] = calculate_grade(new_marks)
            student["status"] = pass_fail(new_marks)

            save_students(students)
            print("Marks updated successfully!\n")
            return

    print("Student not found.\n")


def delete_student():
    name = input("Enter student name to delete: ")

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)

            save_students(students)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


def find_topper():
    if not students:
        print("No student records found.\n")
        return

    topper = max(students, key=lambda x: x["marks"])

    print("\n--- Topper Student ---")
    print(topper)
    print()


def average_marks():
    if not students:
        print("No student records found.\n")
        return

    total = 0

    for student in students:
        total += student["marks"]

    avg = total / len(students)

    print(f"Average Marks: {avg}\n")


while True:
    print("====== Student Performance Management System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Find Topper")
    print("7. Average Marks")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        find_topper()

    elif choice == "7":
        average_marks()

    elif choice == "8":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.\n")