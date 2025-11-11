# Создай класс Vehicle с методом move, который печатает "Moving...".
# Затем создай класс Car, который наследуется от Vehicle и переопределяет метод move, чтобы он печатал "Driving on the road".
#
# После создания классов, создай экземпляр класса Car и вызови у него метод move.
from Словари import student


class Vehicle:

    def move(self):
        print("Moving...")

class Car(Vehicle ):

    def move(self):
        print("Driving on the road")

car = Car()
car.move()

# Создай класс Phone с методом call, который печатает "Calling...".
# Затем создай класс SmartPhone, который наследуется от Phone и добавляет новый метод browse_internet (печатает "Browsing the internet").
#
# После создания классов, создай экземпляр класса SmartPhone, вызови у него метод call, а затем метод browse_internet.

class Phone:
    def call(self):
        print("Calling...")

class SmartPhone(Phone):
    def browse_internet(self):
        print("Browsing the internet")


telefon = SmartPhone()
telefon.browse_internet()
telefon.call()  # Выведет: Calling...

# Создай базовый класс Person с методом __init__, который принимает и сохраняет в свойство name (имя).
#
# Создай класс Student, который наследуется от Person.
# В его методе __init__ должен вызываться родительский конструктор (для сохранения имени) и добавляться новое свойство student_id
# (идентификатор студента).
#
# После создания классов, создай экземпляр класса Student с именем "Alice" и идентификатором "A123". Затем выведи его имя и идентификатор.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):  # метод принимает оба аргумента
        super().__init__(name)  # вызов родительского конструктора
        self.student_id = student_id  # сохранение своего свойства

student_object = Student("Alice", "A123")
print(student_object.name)
print(student_object.student_id)