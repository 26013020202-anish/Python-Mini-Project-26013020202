
# ==========================================
# STUDENT ATTENDANCE MANAGEMENT SYSTEM
# Designed by: Anish Prashant Topalmode
# PRN: 26013020202
# ==========================================

import csv
import os

FILE_NAME = "attendance.csv"


def add_student():
    name = input("Enter student name: ")
    prn = input("Enter student PRN: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([prn, name, "Not Marked"])

    print("Student added successfully!")


def mark_attendance():
    students = []

    if not os.path.exists(FILE_NAME):
        print("No student records found!")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        students = list(reader)

    prn = input("Enter PRN of student: ")
    found = False

    for student in students:
        if student[0] == prn:
            status = input("Enter attendance (Present/Absent): ")
            student[2] = status.capitalize()
            found = True
            break

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(students)

        print("Attendance marked successfully!")
    else:
        print("Student not found!")


def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records available!")
        return

    print("\n------ STUDENT RECORDS ------")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for student in reader:
            print("PRN:", student[0],
                  "| Name:", student[1],
                  "| Attendance:", student[2])


def search_student():
    prn = input("Enter PRN to search: ")

    if not os.path.exists(FILE_NAME):
        print("No records available!")
        return

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for student in reader:
            if student[0] == prn:
                print("\nStudent Found!")
                print("PRN:", student[0])
                print("Name:", student[1])
                print("Attendance:", student[2])
                found = True
                break

    if not found:
        print("Student not found!")


def main():
    while True:
        print("\n================================")
        print(" STUDENT ATTENDANCE MANAGEMENT")
        print("================================")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View All Students")
        print("4. Search Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            mark_attendance()

        elif choice == "3":
            view_students()

        elif choice == "4":
            search_student()

        elif choice == "5":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice! Try again.")


# Project execution starts here
if __name__ == "__main__":
    main()

