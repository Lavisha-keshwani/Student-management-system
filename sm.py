import csv
import os
class Student:
    def __init__(self,name,rollno,dob,grades,courses):
        self.name=name
        self.rollno=rollno
        self.dob=dob
        self.grades=grades
        self.courses=set(courses)

    def average_grade(self):
        return sum(self.grades)/len(self.grades) if self.grades else 0
    def passed(self,threshold=40):
        return self.average_grade()>=threshold
    def __str__(self):
        return (f"Name: {self.name}, RollNo: {self.rollno}, Dob: {'/'.join(map(str,self.dob))}, "
                f"Grades: {self.grades}, Courses: {list(self.courses)}, Average grade: {self.average_grade():.2f}")
    
class StudentManager:
    def __init__(self):
        self.students={}

    def add_student(self):
        try:
            name=input("Enter a name: ")
            rollno=input("Enter roll no: ")
            if rollno in self.students:
                print("Student already exists!")
                return
            dob=tuple(map(int,input("Enter DOB (dd mm yy) ").split()))
            grades=list(map(float,input("Enter grades (space sepearted): ").split()))
            courses=set(input("Enter courses (comma-seperated): ").split(","))
            self.students[rollno]=Student(name,rollno,dob,grades,courses)
            print("Student added!")
        except Exception as e:
            print("Invalid Input",e)
    
    def view_student(self):
        if not self.students:
            print("No students found")
            return
        for s in self.students.values():
            print(s)

    def update(self):
        rollno=input("Enter the roll number to update")
        if rollno in self.students:
            choice=input("Update grades or courses (g/c)?")
            if choice=='g':
                grades=tuple(map(float,input("Enter grades: ").split()))
                self.students[rollno].grades=grades
            elif choice=='c':
                courses=set(input("Enter courses: ").split(","))
                self.students[rollno].courses=courses
            print("Student updated")
        else:
            print("Student not found")
     
    def delete(self):
        rollno=input("Enter the rollno to be deleted")
        if rollno in self.students:
            del self.students[rollno]
            print("Student deleted")
        else:
            print("Student not found")
    
    def average_all(self):
        if not self.students:
            print("No students")
            return
        avg=sum(s.average_grade()for s in self.students.values())/len(self.students)
        print(f"Average grade of all students is {avg:.2f}")

    def passedstu(self):
        passed_students=list(filter(lambda s: s.passed(),self.students.values()))
        print("Students who passed: ")
        for x in passed_students:
            print(x)

    def sorted(self):
        sorted_students=sorted(self.students.values(),key=lambda s:s.average_grade(),reverse=True)
        print("Sorted students:")
        for x in sorted_students:
            print(x)
    
    def search(self):
        name=input("Enter the name to be searched: ").lower()
        found=False
        for s in self.students.values():
            if s.name.lower()==name:
                print(s)
                found=True
        if not found:
            print("No student with this name")

    def save(self):
        with open("students_data.csv","w",newline='') as f:
            writer=csv.writer(f)
            for s in self.students.values():
                writer.writerow([
                    s.name,
                    s.rollno,
                    "/".join(map(str,s.dob)),
                    ",".join(map(str,s.grades)),
                    ",".join(s.courses)
                ])
            print("Data saved to students_data.csv")

    def load(self):
        if not os.path.exists("students_data.csv"):
            return
        with open("students_data.csv","r")as f:
            reader=csv.reader(f)
            for row in reader:
                name,rollno,dob_str,grades_str,courses_str=row
                dob=tuple(map(int,dob_str.split("/")))
                grades=list(map(float,grades_str.split(",")))
                courses=set(courses_str.split(","))
                self.students[rollno] = Student(name, rollno, dob, grades, courses)


    
    def menu(self):
        while True:
            print("\n--- Student Management System ---")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Average Grade of All Students")
            print("6. Filter Passed Students")
            print("7. Search Student by Name")
            print("8. Sort by Average Grade")
            print("9. Save & Exit")
            choice = input("Enter choice: ")
            if choice=='1':
                self.add_student()
            elif choice == '2':
                self.view_student()
            elif choice == '3':
                self.update()
            elif choice == '4':
                self.delete()
            elif choice == '5':
                self.average_all()
            elif choice == '6':
                self.passedstu()
            elif choice == '7':
                self.search()
            elif choice == '8':
                self.sorted()
            elif choice=='9':
                self.save()
                break
            else:
                print("Invalid choice!\n") 

if __name__=='__main__':
    s=StudentManager()
    s.menu()  





    