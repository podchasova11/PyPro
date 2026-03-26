

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




# Нахождения самого частого элемента в списке [1, 2, 2, 3, 4, 7, 5, 6, 7, 7]



# Проверка слова/фразы на полиндром!




