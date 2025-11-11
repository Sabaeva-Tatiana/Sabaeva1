# Создание класса: Создайте простой класс с именем Book. Пока что он может быть пустым.
from symtable import Class


class _Book():
    author = "Пушкин"

# Общие атрибуты: Добавьте в класс Book атрибут класса library_name со значением "Central Library".

class Book():
    library_name = "Central Library"


# Конструктор класса init: Добавьте конструктор __init__ в класс Book,
# который будет принимать параметр title и сохранять его в атрибут объекта с тем же именем.

class Book():
    def __init__(self, title):
        self.title = title


# Методы класса: Добавьте в класс Book метод get_title, который возвращает значение атрибута title конкретного объекта.


# Объект класса: Создайте экземпляр (объект) класса Book с названием "1984" и сохраните его в переменную my_book.



# Понимание параметра self: В классе Book создайте метод show_library, который печатает значение атрибута класса library_name.
# Убедитесь, что правильно используете параметр self.

class Book():
    def __init__(self, show_library:
    self.show_library =