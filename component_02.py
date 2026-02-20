# Списки (list)

empty_list = []  # Пустой список

# список может содержать и смешанные типы данных:
my_list = [12, "apple", True, [2, 3, 4], "Alex"]

print(my_list[3][1])# Список с разными типами данных

fruits = ['яблоко', 'груша']
print(fruits)
print(id(fruits))
fruits.append('банан')  # Добавляем элемент "банан" в конец списка

print(fruits) # Вернет измененный список "['яблоко', 'груша', 'банан']"
print(id(fruits))

fruits.insert(2, "qwe")
print(fruits)

# Удаление элементов из списка и его очистка

fruits.remove("банан")
print(fruits)
del fruits[0]
print(fruits)

fruits.pop(1)
print(fruits)

print(len(fruits))
assert len(fruits) == 1

fruits = ['яблоко', 'груша', 'банан', 'банан']

print(fruits.count("банан")) # Получим цифру равную количеству таких элементов в списке

numbers = [1, 2, 3, 4, 5]

sublist = numbers[1:4]  # Получаем подсписок [2, 3, 4]

print(sublist)

# Слияние списков
numbers = [1, 2, 3, 4, 5]
words = ["one", "two", "three"]

result = numbers + words
print(result)
print(id(result)) # Т.е тут создается новый обьект, новый список.

 #Но так же можно расширить какой-то определенный список, для этого существует метод extend(чем расширяем)
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(id(numbers))
words = ["one", "two", "three"]

numbers.extend(words)
print(numbers)
print(id(numbers))


# Поверхностная копия
# Поверхностную копию списка можно сделать несколькими путями, рассмотрим два основных.
# Способ 1 - Метод copy()
original_list = [1, 2, 3, 4, 5]
copy_of_list = original_list.copy() # Создаст копию списка выше (это новый об

# Способ 2 - срез списка [:]
# Да, срезы списка возвращают новый обьект)

original_list = [1, 2, 3, 4, 5]
copy_of_list = original_list[:]


# Оригинальный список с вложенным списком
original_list = [1, 2, [3, 4]]

# Создание поверхностной копии
shallow_copy = original_list[:]

# Изменение вложенного списка в оригинальном списке
original_list[2][0] = 'a'

print("Оригинальный список:", original_list)  # Вывод: [1, 2, ['a', 4]]
print("Поверхностная копия:", shallow_copy)   # Вывод: [1, 2, ['a', 4]]
# Изменив оригинальный список, меняется и копия




# Глубокая копия
# Копию списка можно сделать с помощью модуля copy

import copy

# Оригинальный список с вложенным списком
original_list = [1, 2, [3, 4]]

# Создание глубокой копии
deep_copy = copy.deepcopy(original_list)

# Изменение вложенного списка в оригинальном списке
original_list[2][0] = 'a'

print("Оригинальный список:", original_list)  # Вывод: [1, 2, ['a', 4]]
print("Глубокая копия:", deep_copy)            # Вывод: [1, 2, [3, 4]]
# меняя оригинал, копия не меняется.


fruits = ["grape", "apple", "orange", "kiwi"]
numbers = [2, 4, 6, 10]
combined = fruits + numbers
print(combined)
print(len(combined))
print(combined[-1])

slice = combined[2:5]
print(slice)
