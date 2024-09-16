class Student:
    def __init__(self, age, grade):
        self.age = age
        self.grade = grade

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.age == other.age

class Teacher():
    def __init__(self, age):
        self.age = age

    def __lt__(self, other):
        if isinstance(other, Teacher):
            return self.age < other.age


student1 = Student(10, 100)
student2 = Student(9, 101)
teacher1 = Teacher(20)

if student1 < teacher1:
    print('student 1 is younger')