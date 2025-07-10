class Student:
    all_students = []
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    
    def update_marks(self, new_marks):
        self.marks = new_marks
    
    def show_details(self):
        print(f"\n Student Details:")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
    
    @classmethod
    def find_student_by_roll(cls, roll):
        for student in cls.all_students:
            if student.roll_number == roll:
                return student
        return None

    @classmethod
    def add_students(cls):
        name = input("Enter student name: ")
        roll = input("Enter student roll number: ")
        marks = int(input("Enter student marks: "))
        student = cls(name, roll, marks)
        cls.all_students.append(student)
        print(f"Student {name} added successfully!")

    @classmethod
    def update_student_marks(cls):
        roll = input("Enter student roll number to update marks: ")
        student = cls.find_student_by_roll(roll)
        if student:
            new_marks = int(input("Enter new marks: "))
            student.update_marks(new_marks)
            print(f"Marks for {student.name} updated successfully!")
        else:
            print("Student not found.")

    @classmethod
    def show_all_students(cls):
        if not cls.all_students:
            print("No students found.")
            return
        for student in cls.all_students:
            student.show_details()
