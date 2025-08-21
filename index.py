# # using dynamic concept of classes, identify alteast 7 classes with atleast with atleast 7  attributes  and  atleast 7 objects
#class Student:
#Example: Dynamic Concept of Classes in Python
# 1. Class: Student
class Student:
    def __init__(self, name, age, gender, student_id, course, year, gpa):
        self.name = name
        self.age = age
        self.gender = gender
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa

# 2. Class: Teacher
class Teacher:
    def __init__(self, name, subject, employee_id, age, gender, department, salary):
        self.name = name
        self.subject = subject
        self.employee_id = employee_id
        self.age = age
        self.gender = gender
        self.department = department
        self.salary = salary

# 3. Class: Course
class Course:
    def __init__(self, code, title, credits, department, lecturer, duration, level):
        self.code = code
        self.title = title
        self.credits = credits
        self.department = department
        self.lecturer = lecturer
        self.duration = duration
        self.level = level

# 4. Class: Book
class Book:
    def __init__(self, title, author, isbn, publisher, year, pages, category):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.category = category

# 5. Class: Hospital
class Hospital:
    def __init__(self, name, location, capacity, director, departments, established_year, rating):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.director = director
        self.departments = departments
        self.established_year = established_year
        self.rating = rating

# 6. Class: Patient
class Patient:
    def __init__(self, name, age, gender, patient_id, diagnosis, doctor, admission_date):
        self.name = name
        self.age = age
        self.gender = gender
        self.patient_id = patient_id
        self.diagnosis = diagnosis
        self.doctor = doctor
        self.admission_date = admission_date

# 7. Class: Vehicle
class Vehicle:
    def __init__(self, brand, model, year, color, engine, fuel_type, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.engine = engine
        self.fuel_type = fuel_type
        self.price = price



# Creating at least 7 Objects
student1 = Student("Alice", 20, "Female", "S101", "Computer Science", 2, 3.8)
teacher1 = Teacher("Mr. John", "Mathematics", "T001", 40, "Male", "Science", 12000)
course1 = Course("CS101", "Intro to Programming", 3, "Computer Science", "Dr. Smith", "3 months", "Beginner")
book1 = Book("Python Basics", "Jajja Ozzy", "9781234567", "TechPress", 2021, 350, "Programming")
hospital1 = Hospital("Good Care Hospital", "Kampala", 500, "Dr. Jane", ["Surgery", "Pediatrics"], 1995, 4.5)
patient1 = Patient("Michael", 32, "Male", "P001", "Malaria", "Dr. Adams", "2024-06-10")
vehicle1 = Vehicle("Toyota", "Corolla", 2022, "White", "1.8L", "Petrol", 25000)


# Display Objects
print(student1.__dict__)
print(teacher1.__dict__)
print(course1.__dict__)
print(book1.__dict__)
print(hospital1.__dict__)
print(patient1.__dict__)
print(vehicle1.__dict__)
