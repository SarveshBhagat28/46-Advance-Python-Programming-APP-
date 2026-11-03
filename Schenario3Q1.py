import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", default="students.csv")
args = parser.parse_args()


with open(args.file, "r") as file:
    reader = csv.DictReader(file)
    students = list(reader)

print("\n--- Student Records ---")
for student in students:
    print(student)


roll = input("\nEnter Roll Number to search: ")

found = False

for student in students:
    if student["Roll Number"] == roll:
        print("\nStudent Found:")
        print(student)
        found = True
        break

if not found:
    print("Student not found!")