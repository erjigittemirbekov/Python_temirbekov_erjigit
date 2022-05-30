class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self, full_name, age, is_married):
        print(f"fullname: {full_name} \n age: {age} \n is_married: {is_married}")

    def output(self,):
        return f"full name {self.full_name}\n" \
               f"age {self.age}\n" \
               f"is married {self.is_married}\n" \



class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        Person.__init__(self, full_name, age, is_married)
        self.marks = marks

    def average(self):
        print(sum(self.marks) / 5)

class Teacher(Person):
    salary = 1800
    def __init__(self, full_name, age, is_married, experience=3):
        Person.__init__(self, full_name, age, is_married)
        self.experience = experience


    def Teacher_cash(self):
        if self.experience > 3:
            new_salary = self.salary + ((self.salary/100*5) * (self.experience-3))
            return new_salary



def create_students():
    student1 = Student(full_name="Эсен", age=19, is_married=True, marks={
        "биология": 5,
        "история": 2,
        "математика": 5,
        "физика": 3,
        "русский-язык": 5,
    })
    student2 = Student(full_name="Бексултан", age=15, is_married=False, marks={
        "биология": 5,
        "история": 4,
        "математика": 3,
        "физика": 3,
        "русский-язык": 5,
    })
    student3 = Student(full_name="Алексей", age=34, is_married=False, marks={
        "биология": 5,
        "история": 5,
        "математика": 4,
        "физика": 4,
        "русский-язык": 2,
    })

    resultu = [student1, student2, student3]
    return resultu

students = create_students()
for i in students:
    list = []
    for marks in i.marks.values():
        list.append(marks)
    print(f"Name: {i.full_name}\n"
          f"Age: {i.age}\n"
          f"Maried: {i.is_married}\n"
          f"Average marks: {sum(list)/len(list)}\n")