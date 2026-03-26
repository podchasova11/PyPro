

# Найти среднее количество символов в словах любой строки

line_words = "Найти среднее количество символов"
words = line_words.split()
print(words)
total_symbols = sum(len(word) for word in words)
middle_value = total_symbols/len(words)
print(middle_value)



# Написать пример декоратора
def my_decorator(func):  # Создание декоратора
    def wrapper():  # Обертка для функции
        print("Что-то происходит перед вызовом функции")  # Предусловие
        func()  # Вызов функции
        print("Что-то происходит после вызова функции")  # Постусловие
    return wrapper


@my_decorator  # Вызов декоратора
def say_hello():
    print("Привет, мир!")


say_hello() # Вызов продекорированной функции



# Найти самую длинную строку в списке ["hi", "intelegent", "world", "indigo"]

words = ["hi", "intelegent", "world", "indigo"]
maximum = max(len(word) for word in words)
print(maximum)


words = ["hi", "intelegent", "world", "indigo"]
maximum = max(len(word) for word in words)
longest_word = [word for word in words if len(word) == maximum]
print(longest_word)



# Нахождения самого частого элемента в списке [1, 2, 2, 3, 4, 7, 5, 6, 7, 7]

# numbers = [1, 2, 2, 3, 4, 7, 5, 6, 7, 7]
#
# counts = {}
# most_frequent = numbers[0]
# max_count = 0
#
# for num in numbers:
#     # Считаем количество вхождений
#     if num in counts:
#         counts[num] += 1
#     else:
#         counts[num] = 1
#
#     # Сразу проверяем, стал ли этот элемент самым частым
#     if counts[num] > max_count:
#         max_count = counts[num]
#         most_frequent = num
#
# print(most_frequent)  # Выведет 7


numbers = [1, 2, 2, 3, 4, 7, 5, 6, 7, 7]

most_frequent = numbers[0]

for num in numbers:
    if numbers.count(num) > numbers.count(most_frequent):
        most_frequent = num

print(most_frequent) # Выведет 7


numbers = [1, 2, 2, 3, 4, 7, 5, 6, 7, 7]

often_number = numbers[0]

for num in numbers:
    if numbers.count(num) > numbers.count(often_number):
        often_number = num

print(often_number) # Выведет 7





# Проверка слова/фразы на полиндром!

line_words = " роза упала на лапу Азора"
new = line_words.replace(" ", "").lower()
print(new)
palindrom = new[::-1]
print([palindrom])


line_words = "Шалаш"
word = line_words.replace(" ", "").lower()
palindrome = word[::-1]
assert word == palindrome, "Не является палиндромом"
print(f"Строка: '{word}'")
print(f"Палиндром: '{word[::-1]}'")




