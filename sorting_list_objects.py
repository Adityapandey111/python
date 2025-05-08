class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self):
        return f"{self.name} - Age: {self.age}, Marks: {self.marks}"

# Create a list of Student objects
students = [
    Student("Alice", 22, 88),
    Student("Bob", 20, 75),
    Student("Charlie", 23, 95),
    Student("David", 21, 80)
]

print("Before Sorting:")
for student in students:
    print(student)

# Sort the list by 'age'
students.sort(key=lambda student: student.age)

print("\nAfter Sorting by Age:")
for student in students:
    print(student)

# Sort the list by 'marks'
students.sort(key=lambda student: student.marks, reverse=True)

print("\nAfter Sorting by Marks (Descending):")
for student in students:
    print(student)
