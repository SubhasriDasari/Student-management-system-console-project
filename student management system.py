# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 09:57:59 2025

@author: subhasri
"""

import csv
import os

FILENAME = "students.csv"

# Load students from file
def load_students():
    students = []
    if os.path.exists(FILENAME):
        with open(FILENAME, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    return students

# Save students to file
def save_students(students):
    with open(FILENAME, mode="w", newline="") as file:
        fieldnames = ["Roll", "Name", "Course", "Marks"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

# Add a student
def add_student(students):
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    student = {"Roll": roll, "Name": name, "Course": course, "Marks": marks}
    students.append(student)
    save_students(students)
    print("✅ Student added and saved.\n")

# Display all students
def display_students(students):
    if not students:
        print("⚠️ No student records found.\n")
        return
    print("🎓 Student Records:")
    for student in students:
        print(student)

# Search student by roll number
def search_student(students):
    roll = input("Enter Roll Number to search: ")
    for student in students:
        if student["Roll"] == roll:
            print("🎯 Student Found:", student)
            return
    print("❌ Student not found.\n")

# Update student info
def update_student(students):
    roll = input("Enter Roll Number to update: ")
    for student in students:
        if student["Roll"] == roll:
            student["Name"] = input("Enter new name: ")
            student["Course"] = input("Enter new course: ")
            student["Marks"] = input("Enter new marks: ")
            save_students(students)
            print("✅ Student updated and saved.\n")
            return
    print("❌ Student not found.\n")

# Delete student
def delete_student(students):
    roll = input("Enter Roll Number to delete: ")
    for i, student in enumerate(students):
        if student["Roll"] == roll:
            del students[i]
            save_students(students)
            print("🗑️ Student deleted and file updated.\n")
            return
    print("❌ Student not found.\n")

# Main menu
def main():
    students = load_students()
    while True:
        print("\n🎓 STUDENT MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            update_student(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.\n")

# Run the program
main()
