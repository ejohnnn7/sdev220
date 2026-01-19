'''
Student Name: Elizabeth John
File Name: gpaChecker.py
Description:
The purpose of this program is to create an app that will ask for students names and GPAs and determine whether the student made the Dean's List or the Honor Roll.
The program stops when the user enters "ZZZ" as the student's name.
'''

while True:
    # Ask for the student's name
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")

    # Stop the program if the user enters "ZZZ"
    if last_name == "ZZZ":
        print("Program ended.")
        break

    # Ask for the student's first name
    first_name = input("Enter the student's first name: ")

    # Ask for the student's GPA
    gpa = float(input("Enter the student's GPA: "))

    # Check for Dean's List
    if gpa >= 3.5:
        print(f"{first_name} {last_name} made the Dean's List.")

    # Check for Honor Roll
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} made the Honor Roll.")

    else:
        print(f"{first_name} {last_name} did not qualify for honors.")

    print() # Blank line for readability between entries