"""
Question:
Write a Python program to determine whether a student has passed or failed.

Conditions:
- The overall percentage must be at least 40%.
- The student must score at least 33 marks in each subject.
If both conditions are satisfied, print "Passed"; otherwise, print "Failed".
"""

marks1 = int (input("Enter Marks 1: "))
marks2 = int (input("Enter Marks 2: "))
marks3 = int (input("Enter Marks 3: "))

total_percentage = 100 * (marks1 + marks2 + marks3)/300

if (total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33) :
    print("You are Passed", total_percentage)

else:
    print("You're Failed", total_percentage)