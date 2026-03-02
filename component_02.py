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


combined = ['grape', 'apple', 'orange', 'kiwi', 2, 4, 6, 8]
combined_copy = combined[:]
combined_copy[1] = "яблоко"
print(combined)
print(id(combined))
print(combined_copy)
print(id(combined_copy))


# num = int(input("Введите число: "))
# if num > 0:
#     print("Число положительное")
# else:
#     print("Число отрицательное")
#
#
# num = int(input("Введите число: "))
# if num < 0:
#     print("Число отрицательное")
# elif num == 0:
#     print("Число равно нулю")
# elif 0 < num < 10:
#     print("Число от 1 до 9")
# else:
#     print("Число 10 и больше")


# is_raining = False
# is_sunny = False
#
# if is_raining and is_sunny:
#     print("дождь при солнце, погода-парадокс")
# elif is_sunny and not is_raining:
#     print( "Сегодня солнечная погода, отличный день для прогулки!")
# elif is_raining and not is_sunny:
#     print("Сегодня идет дождь, возьмите зонт!")
# else:
#     print("Сегодня облачно, но без осадков")



# Объявление переменных
is_raining = True   # замените на True/False в зависимости от погоды
is_sunny = False    # замените на True/False в зависимости от погоды

# Определение сценариев погоды
if is_raining and is_sunny:
    result = "Дождь при солнце (погода-парадокс). Может быть радуга!"
elif is_sunny and not is_raining:
    result = "Сегодня солнечная погода, отличный день для прогулки!"
elif is_raining and not is_sunny:
    result = "Сегодня идет дождь, возьмите зонт!"
else:  # не светит солнце и не идёт дождь
    result = "Сегодня облачно, но без осадков"

print(result)

# Объявление переменных
is_raining = True  # заменить на True/False в зависимости от погоды
is_sunny = False  # заменить на True/False в зависимости от погоды

if is_raining and is_sunny:
    result = "Дождь при солнце (погода-парадокс). Может быть радуга!"
elif is_sunny and not is_raining:
    result = "Сегодня солнечная погода, отличный день для прогулки!"
elif is_raining or not is_sunny:
    # дождь без солнца, или когда не солнечно

    if is_raining and not is_sunny:
        result = "Сегодня идет дождь, возьмите зонт!"

else:
    result = "Сегодня облачно, но без осадков"

print(result)

student = {
    "name": "Иван",
    "age": 20,
    "subjects": ["математика", "информатика"],
    "average_score": 4.5
}
# Добавить новый предмет в список предметов студента
student["subjects"].append("физика")
print(student["subjects"])

# удаление ключа "age"
if "age" in student:
    del student["age"]

print(student)

# Получить список всех ключей словаря
for key in ["age", "gender"]:
    print(f"Ключ '{key}' {'существует' if key in student else 'отсутствует'} в словаре.")

keys = list(student.keys())
for k in keys:
    print(k)

# получить список значений
values = list(student.values())
print(values)


student = {
    "name": "Ivan",
    "age": 20,
    "subjects": ["mathimatics", "informatic"],
    "averege_score": 4.5
}
# добавить новый предмет в список предметов
student["subjects"].append("fizics")
print(student["subjects"])

if "age" in student:
    del student["age"]
print(student)

key = list(student.keys())
print(key)

value = list(student.values())
print(values)


response = {
    "cartButtonEnabled": True,
    "conditions": {
        "campaign": {
            "id": "unlimited_burn_99rub_prd",
            "info": "Доставка в пункт выдачи от",
            "link": "https://support.avito.ru/articles/2369"
        },
        "destination": "по Дзержинску",
        "discount": 900,
        "minDays": 1,
        "price": 99,
        "terms": "От 1 дня, от",
        "trustfactors": [
            {
                "helpIcon": False,
                "icon": "cod",
                "label": "",
                "text": "Можно оплатить при получении"
            }
        ]
    },
    "services": [
        {
            "available": True,
            "enabled": True,
            "type": "delivery"
        },
        {
            "available": True,
            "enabled": True,
            "type": "deliveryCourier"
        },
        {
            "available": False,
            "enabled": False,
            "type": "deliveryCourierD2D"
        },
    ]
}

