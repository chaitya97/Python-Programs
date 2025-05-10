class StudentGradeSystem:
    def __init__(self):
        self.students = {
            "Alice": [85, 90, 78],
            "Bob": [70, 60, 65],
            "Charlie": [95, 88, 92]
        }

    
    def getMarks(self, subject):
        while True:
            try:
                marks = int(input(f"Enter the marks for {subject}: "))
                return marks  # Return valid marks
            except ValueError:
                print("Invalid input. Please enter integer marks.")


    def showDatabase(self):
        print("")
        print("Student Grade System:")
        print("Student data in the database:")
        print("")

        if not self.students:
            print("No student records found.")
            return

        for name,marks in self.students.items():
            print("-----------------------------")
            print(f"Name of the student: {name}")
            print(f"Marks in Maths: {self.students[name][0]}")
            print(f"Marks in Physics: {self.students[name][1]}")
            print(f"Marks in Chemistry: {self.students[name][2]}")
    
    def addStudent(self,newStudent):
        
        if newStudent in self.students:
            print("Student Already exist into DB.")
            return False
        
        else:
                
            Mark1 = self.getMarks("Maths")
            Mark2 = self.getMarks("Physics")
            Mark3 = self.getMarks("Chemistry")

            self.students[newStudent] = [Mark1,Mark2,Mark3]
        
        print("Details are added into the database.")

        return True
    

    def removeStudent(self,removeStudentName):
        if removeStudentName in self.students.keys():
            print(f"Data found for student: {removeStudentName}")
            print(f"Student Name: {removeStudentName} and Marks: {self.students[removeStudentName]}")
            self.confirmation = str(input("Are you sure you want to delete the data of this student? Y|N: ")).upper() == 'Y'
            if self.confirmation:
                self.students.pop(removeStudentName)
                print (f"\nData deleted for student:  {removeStudentName}")

                return True
            else:
                print("Didn't confirm the operation. Not deleting your data.")

                return False
        
        else:
            print(f"No data found for: {removeStudentName}")

            return False
    
    def searchStudent(self,searchStudentName):
        if searchStudentName in self.students.keys():
            print("")
            print(f"Data found for student: {searchStudentName}")
            print(f"Name of the student: {searchStudentName}")
            print(f"Marks in Maths: {self.students[searchStudentName][0]}")
            print(f"Marks in Physics: {self.students[searchStudentName][1]}")
            print(f"Marks in Chemistry: {self.students[searchStudentName][2]}")

            return True
        
        else:
            print(f"No data found for: {searchStudentName}")
            return False
    
    def editStudent(self, editStudentName):
        if self.searchStudent(editStudentName):
            subjects = ['maths', 'physics', 'chemistry']
            print("")
            print("Subjects: Maths, Physics, Chemistry")
            while True:
                print("")
                nameOfSubject = input("Enter the subject you want to change: ").strip().lower()
                if nameOfSubject in subjects:
                    subjectIndex = subjects.index(nameOfSubject)
                    newMark = self.getMarks(nameOfSubject.capitalize())
                    print("")
                    confirmation = input(f"Confirm update of {nameOfSubject.capitalize()} marks to {newMark} for Student- {editStudentName}? (Y/N): ").upper()
                    if confirmation == 'Y':
                        self.students[editStudentName][subjectIndex] = newMark
                        print("")
                        print(f"{nameOfSubject.capitalize()} marks updated.")
                        break
                else:
                    print("Invalid subject name. Please enter Maths, Physics, or Chemistry.")
        else:
            print(f"Can't edit data for {editStudentName}, as it is not in the database.")

    
    def findPercentage(self):
        print("")
        print("Average of all students")
        for name,marks in self.students.items():
            print("-----------------------------")
            print(f"Name of the student: {name}")
            average = sum(marks)/len(marks)
            print(f"Average Marks: {average:.2f}")


s1 = StudentGradeSystem()
print("")
print("STUDENT GRADE SYSTEM")
while True:
    print("")
    print("-------------------------------------")
    print("\nPlease choose from the below options: ")
    print("1. Show database")
    print("2. Add Student")
    print("3. Remove Student")
    print("4. Search Student Record")
    print("5. Edit the marks")
    print("6. Average of all students")
    print("7. Exit")
    print("")

    try:
        optionShow = int(input("Enter your option from above: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    match optionShow:
        
        case 1:
            s1.showDatabase()
        
        case 2:
            print("")
            newStudent = str(input("Enter the name of the student: ")).strip().title()
            s1.addStudent(newStudent)
        
        case 3:
            print("")
            removeStudentName = str(input("Enter the name of the student whose data you want to remove: ")).strip().title()
            s1.removeStudent(removeStudentName)
        
        case 4:
            print("")
            searchStudentName = str(input("Enter the name of the student whose data you want to search: ")).strip().title()
            s1.searchStudent(searchStudentName)
        
        case 5:
            print("")
            editStudentName = str(input("Enter the name of the student whose data you want to change: ")).strip().title()
            s1.editStudent(editStudentName)
        
        case 6:
            s1.findPercentage()
        
        case 7:
            print("Exiting the application. Goodbye!")
            break
        
        case _:
            print("Invalid option. Please try again.")
    