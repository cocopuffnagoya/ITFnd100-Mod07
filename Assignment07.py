# ------------------------------------------------- #
# Title: Homework Grade Management Program
# Description: This program was designed for teachers
# to save students names and grades to file and retrieve the saved data
# ChangeLog: (Who, When, What)
# CJones, 2/26/2023, created the script
# ------------------------------------------------- #

import pickle   # import pickle to be able to dump and load data in the program

# -- Data -- #
name = ''   # Variable to assign student name. String
grade = 0   # Student's grade. Defaulted to 0. Integer
names = []  # List of students names
grades = [] # List of students grades
file = 'studentData.pkl'    # Binary file to save pickled data

# Show Welcome message to the user in the beginning of the program
print("Hello Teacher!\nWelcome to Grade Management Program!\n")

# Error handling 1
# This while Try-Except loop collects a number. It does not accept a non-numeric value.
# Until the user inputs a valid number, the program keeps asking how many students the user has
while True:
    try:
        numStudents = int(input("How many students do you have?: "))    # Ask the user to enter an integer
        print("Thank you for entering the number!") # Message shown if the user enters a valid number
        print("You have "+str(numStudents)+" students in your class.")  # Show the number the user entered
        break   # Break the loop when a valid number is input
    except:
        print("That is not a valid number. Try again!") # Keep asking to try again until a valid number is input

# -- Processing -- #
# Pickling
# Function to save data to binary file
def save_to_binary_file(file):
    with open(file, 'wb') as dataFile: # Open binary file
        pickle.dump(numStudents, dataFile)  # Dump number of students onto dataFile
        pickle.dump(names,dataFile) # Dump students names to dataFile
        pickle.dump(grades,dataFile) # Dump students grades to dataFile
    print("Data saved to File!\n(File Name: studentData.pkl)")  # Show file saved message

# Function to read binary data
def open_file(file):    # Create a open_file function to read binary file
    with open(file,'rb') as readFile:
        a = pickle.load(readFile)   # Load first line and put the data into a
        b = pickle.load(readFile)   # Load second line and put the data into b
        c = pickle.load(readFile)   # Load third line and put the data into a
        print("The file shows:")
        print("Number of your Students: "+str(a))   # Show loaded data
        print("Your Students and Grades:")
        for i in range(0,numStudents):  # Show loaded data
            print(b[i],c[i],sep=' = ')  # Show loaded data

# -- Presentation (I/O) -- #
# Function to input name and grade
def input_name_grade(name, grade):
    for i in range(0,numStudents):  # Loop the following process numStudents times
        name = input("Please enter a student name: ")   # Ask for student name
        names.append(name)  # Put the name to names list
        # Error handling 2 - accepts only a number
        class InvalidGrade(Exception): # Create a custom Exception
            pass
        while True:
            try:
                grade = int(input("Please enter "+name+"'s grade: "))    # grade has to be an integer
                if grade < 0 or grade > 100:    # if grade is outside 0 - 100
                    raise InvalidGrade          # InvalidGrade exception is raised
                grades.append(grade)    # if no error, grade is put into Grades list
                break
            except ValueError:
                print("That is not a number! Try again!") # Value error message shown for string input
            except InvalidGrade:
                print("Please enter a number between 0 and 100!") # InvalidGrade error message displayed

    print("You have entered: ") # Show the data the user has just entered
    for i in range(0,numStudents):  # Loop numStudents times
        print(names[i],grades[i],sep=' = ') # Show ith person's name and grade

# Menu - Menu is shown to the user until 4 is selected to exit the program
while True:
    print('''
    What would you like to do?
    
            1 - Input your students grades
            2 - Save your students grade to file
            3 - Retrieve your students data from file
            4 - Exit
            ''')

    choice = int(input("Select your choice: ")) # Ask user to input a number 1-4
    if choice not in (1,2,3,4): # If user inputs other than 1,2,3,4
        print("Enter 1,2,3 or 4!")  # tell user to input a number 1,2,3 or 4
        continue    # Continue asking
    elif choice == 1:   # if choice is 1
        input_name_grade(name, grade)   # call input_name_grade() function
    elif choice == 2:   # if choice is 2
        save_to_binary_file(file)   # call save_to_binary_file() function
    elif choice == 3:   # if choice is 3
        open_file(file) # call open_file() function
    else:  # if choice is 4
        break   # exit the program
print("Good bye!")








