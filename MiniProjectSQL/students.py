import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks INTEGER NOT NULL
)
""")

def add_student(name, marks):
    cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", (name, marks))
    conn.commit()
    print(f"Student added successfully.")

def show_students():
    cursor.execute("SELECT * FROM students")
    row = cursor.fetchall()
    print("\n ========== Student List ========== ")
    for student in row:
        print(f"ID: {student[0]}, Name: {student[1]}, Marks: {student[2]}")

def update_student(student_id, new_marks):
    cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (new_marks, student_id))
    conn.commit()
    print(f"Student ID updated successfully.")

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print(f"Student ID deleted successfully.")


def menu():
    while True:
        print("\n ========== Student Management System Via SQLLite DB ========== ")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice(1-5): ")

        if choice == '1':
            name = input("Enter student name: ")
            marks = input("Enter student marks: ")
            add_student(name, marks)
        elif choice == '2':
            show_students()
        elif choice == '3':
            student_id = input("Enter student ID to update: ")
            new_marks = input("Enter new marks: ")
            update_student(student_id, new_marks)
        elif choice == '4':
            student_id = input("Enter student ID to delete: ")
            delete_student(student_id)
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
conn.close()