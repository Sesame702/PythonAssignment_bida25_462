#Section A: Initial Setup - Scaler Objects and Loops
#Prompt the user for the total number of students
num_students = int(input("Enter number of students: "))

#Initialize variables
student_records = []
total_grade = 0.0

#Loop to collect data for each student
for i in range(1, num_students + 1):
    print(f"\n--- Student {i} ---")
    name = input("Enter student name: ")

    #Basic Validation Loop for Grade (between 0 and 100)
    while True:
        try:
            grade = float(input("Enter student grade (0-100):"))
            if 0 <= grade <= 100:
                break    #exits validation loop
            else:
                print("Invalid input. Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    #Store record and accumulate total grade
    student_records.append((name, grade))
    total_grade += grade

#Calculate class average
class_average = total_grade / num_students if num_students > 0 else 0.0

#Display results
print("\n" + "=" * 40)
print(f"Total Class Grade Score: {total_grade:.2f}")
print(f"Class Average Grade: {class_average:.2f}")
print("=" * 40)

print("\nStudent Results:")
for name, grade in student_records:
    print(f"Name: {name:<15} | Grade: {grade:<6.2f} | Class Average: {class_average:.2f}")

#Section B: Expanding with Lists and Tuples
#List of subjects required
subjects = ["Math", "English", "Science"]

#List to hold all student record tuples
students = []

print("==================================")
print("    STUDENT GRADE ENTRY SYSTEM    ")
print("==================================")

num_students = int(input("Enter total number of students: "))

#Step 1: Collect Student Data
for i in range(1, num_students + 1):
    print()
    print("--- Student", i, "---")
    name = input("Enter student name: ")

    #Store grades for this specific students in a list
    student_grades = []

    for subject in subjects:
        grade = float(input("Enter grade for " + subject + " (0-100): "))

        #Validation loop
        while grade < 0 or grade > 100:
            print("Invalide grade! Must be between 0 and 100.")
            grade = float(input("Enter grade for " + subject + " (0-100): "))

        student_grades.append(grade)

    #Store student record as a tuple
    student_tuple = (name, student_grades)
    students.append(student_tuple)

#Step 2: Lists to track all grades per subject across the whole class
math_grades = []
english_grades = []
science_grades = []

for student in students:
    grades = student[1]
    math_grades.append(grades[0])
    english_grades.append(grades[1])
    science_grades.append(grades[2])

#Step 3: Data Display - Summary Table
print()
print("======================================================")
print("                   SUMMARY TABLE                      ")
print("Name           Math      English    Science    Average")
print("------------------------------------------------------")

for student in students:
    name = student[0]
    grades = student[1]

    #Calculate student's overall average
    student_avg = sum(grades) / len(grades)

    #Display formatted row
    print(name, round(grades[0], 1), round(grades[1], 1), round(grades[2], 1), round(student_avg, 2))

#Step 4: Subject Performance (Highest & Lowest)
print()
print("===============================================================")
print("                SUBJECT HIGHEST & LOWEST GRADES                ")
print("===============================================================")

if num_students > 0:
    print("Math:   Highest =", max(math_grades), "| Lowest =", min(math_grades))
    print("English: Highest=", max(english_grades), "| Lowest = ", min(english_grades))
    print("Science: Highest =", max(science_grades), "| Lowest =", min(science_grades))
print("=========================================================")

#Section C:Introduction of Dictionaries
students = {}
subjects = ["Math", "English", "Science"]

while True:
    print()
    print("=========================================")
    print("        STUDENT MANAGEMENT SYSTEM        ")
    print("=========================================")
    print("1. Add a New Student")
    print("2. Update an Existing Student's Grades")
    print("3. Remove a Student")
    print("4. Search Student by Name")
    print("5. View Subject-Specific Grades")
    print("6. Exit")
    print("=========================================")

    choice = input("Enter your choice(1-6): ").strip()

    #1. Add a New Student
    if choice == "1":
        print()
        name = input("Enter a new student name: ")

        if name in students:
            print("Student already exists!")
        else:
            students[name] = {}
            for subject in subjects:
                grade = float(input("Enter grade for" + subject + " (0-100): "))
                while grade < 0 or grade > 100:
                    print("Invalid grade! Must be between 0 and 100.")
                    grade = float(input("Enter a grade for" + subject + " (0-100): "))

                #Each subject stores grades as a list
                students[name][subject] = [grade]

            print("Student", name, "added successfully!")

        #2. Update an Existing Student's Grades
    elif choice == "2":
        print()
        name = input("Enter student name to update: ")

        if name in students:
            print("Select subject to update:")
            for i in range(len(subjects)):
                print(i + 1, ".", subjects[i])

            subj_choice = int(input("Enter choice number: ")) - 1
            if 0 <= subj_choice < len(subjects):
                chosen_subject = subjects[subj_choice]
                new_grade = float(input("Enter new grade for " + chosen_subject + ": "))

                while new_grade < 0 or new_grade > 100:
                    print("Invalud grade! Must be between 0 and 100. ")
                    new_grade = float(input("Enter new grade: "))

                #Update grade lisr for that subject
                students[name][chosen_subject] = [new_grade]
                print("Grade updated successfully!")
            else:
                print("Invalid subject choice")
        else:
            print("Student not found!")

    #3. Remove a Student
    elif choice == "3":
        print()
        name = input("Enter student name to remove: ")

        if name in students:
            del students[name]
            print("Student", name, "has been removed. ")
        else:
            print("Student not found!")

    #4. Data Access/ Search
    elif choice == "4":
        print()
        name = input("Enter a student name to search: ")

        if name in students:
            print()
            print("--- Record for", name, "---")
            total = 0
            count = 0

            for subject, grade_list in students[name].items():
                #Get grade value from the list
                grade = grade_list[0]
                print(subject + ":", grade)
                total = total + grade
                count = count + 1

            avg = total / count
            print("Average Grade:", round(avg, 2))
        else:
            print("Student not found!")

    #5. Subject-Specific Grades Across All Students
    elif choice == "5":
        print()
        print("Select subject to view:")
        for i in range(len(subjects)):
            print(i + 1, ".", subjects[i])

        subj_choice = int(input("Enter choice number: ")) - 1

        if 0 <= subj_choice < len(subjects):
            chosen_subject = subjects[subj_choice]
            print()
            print("--- All Grades for", chosen_subject, "---")

            if len(students) == 0:
                print("No students registered yet.")
            else:
                for name, data in students.items():
                    grades = data[chosen_subject]
                    print("Name:", nam, "| Grade:", grades)
        else:
            print("Invalid subject choice!")

    #6. Exit Program
    elif choice == "6":
        print("Exiting system. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1 through 6.")