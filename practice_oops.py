from abc import abstractmethod

class Course:
    course_id: int
    name: str
    credits: int
    def __init__(self,i,n,c):
        self.course_id=i
        self.name=n
        self.credits=c

class Student:
    student_id: int
    student_name: str
    # enrolled_courses: []

    def __init__(self,i,n,c):
        self.student_id=i
        self.student_name=n
        self.enrolled_courses=c

class S:
    # @staticmethod
    def credits(self,students,id):
        sum=0
        for x in students:
            if id==x.student_id:
                for c in x.enrolled_courses:
                    sum+=c.credits
        return sum


n=int(input("Enter number students : "))

students=[]

for i in range(n):
    id=int(input("Enter the student id : "))
    name=input("Enter the student name : ")

    c=int(input("Enter the number of the courses : "))

    courses=[]
    for j in range(c):
        c_id=int(input("Enter the course id : "))
        c_name=input("Enter the name of the course : ")
        cr=int(input("Enter the credit : "))
        courses.append(Course(c_id,c_name,cr))
    
    students.append(Student(id,name,courses))


id=int(input("Enter the Student id : "))

s=S()
credi=s.credits(students,id)

print(f"Total credit of the student whose id is {id} : {credi}")

