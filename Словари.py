# Задача 1 (Создание словаря):
# Создай словарь fruit_colors, где ключами будут названия фруктов ('apple', 'banana', 'grape'),
# а значениями — их цвета ('red', 'yellow', 'purple').

# fruit_colors = {
# "apple": "red",
# 'banana': 'yellow',
# 'grape': 'purple'
# }
#
# Задача 2 (Доступ к элементам словаря по ключу):
# В словаре student = {"name": "Alex", "age": 20, "grade": "A"} получи значение по ключу "age" и выведи его.
# Напиши решение, а я подскажу, если нужно будет что-то исправить.

# student = {
#     "name": "Alex",
#     "age": 20,
#     "grade": "A"
# }
# print(student["age"])
#
# Задача 3 (Добавление и обновление элементов словаря):
# Дан словарь car = {"brand": "Toyota", "model": "Camry"}.
# Добавь новый ключ "year" со значением 2020.
# Обнови значение ключа "model" на "Corolla".

# car = {
#     "brand": "Toyota",
#     "model": "Camry"
# }
#
# car["year"] = 2020
# car ["model"] = "Corolla"
# print(car)
#
# Задача 4 (Удаление элементов словаря):
# Дан словарь book = {"title": "1984", "author": "Orwell", "year": 1949}.
# Удали ключ "year" с его значением.
# Попробуй удалить несуществующий ключ "pages" с помощью .pop() так,
# чтобы программа не сломалась, а вернула строку "Ключ не найден" (используй второй аргумент метода).
#
# book = {
#     "title": "1984",
#     "author": "Orwell",
#     "year": 1949
# }
#
# del book["year"]
# print(book)
#
# result = book.pop("pages", "Ключ не найден")
# print(result)

# Задача 5 (Получение элементов, ключей и значений словаря):
# Дан словарь country = {"name": "Japan", "capital": "Tokyo", "population": 126_500_000}.
# Выведи список всех ключей словаря
# Выведи список всех значений словаря
# Выведи список всех пар "ключ-значение"
# Напиши решение, а я подскажу, если нужно будет что-то исправить.
# Когда будешь готов, скажи "Следующая задача"!
# P.S. Для этой задачи тебе понадобятся методы .keys(), .values() и .items().

# country = {
#     "name": "Japan",
#     "capital": "Tokyo",
#     "population": 126_500_000
# }
# print (country.keys())
# print(country.values())
# print(country.items())
#
# Задача 6 (Проверка на наличие ключей и значений):
# Дан словарь inventory = {"apples": 5, "bananas": 3, "oranges": 2}.
# Проверь, есть ли ключ "bananas" в словаре (вернет True/False)
# Проверь, есть ли значение 2 среди значений словаря (вернет True/False)
# Напиши решение, используя:
# оператор in для проверки ключа
# метод .values() и оператор in для проверки значения
# P.S. Не забудь про двойные скобки при проверке значения (например, 2 in inventory.values()).
#
# inventory = {
#     "apples": 5,
#     "bananas": 3,
#     "oranges": 2
# }
#
# print("bananas" in inventory)  # True
# print(2 in inventory.values())  # True

contacts = {
"Alice": "alice@mail.com",
"Bob" : "bob123@mail.com",
"Charlie": "charlie.blue@mail.com"
}
contacts ["Diana"] = "diana99@mail.com"
del contacts ["Bob"]
contacts ["Alice"] = "alice2023@mail.com"
print ("Eve" in contacts)
print(contacts)




