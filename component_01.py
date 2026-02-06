
text = "Python_0001"
print(text[1])  # первый символ строки text
print(text[-1])  # последний символ строки text
print(text[2:4])  # срез строки text, который содержит второй и третий символы
print(len(text))  # Выведите длину строки text

name = "Mila"
age = "10"
message = "Меня зовут "  + name  +  " и мне " + age + " лет."
print(message)

text = "Python - лучший язык для автоматизации!"
contains = "Python" in text  # содержит ли строка text слово "Python"
print(contains)
text_modified = text.replace(" ", "*")# В строке text, замените все пробелы на *
print(text_modified)
print(text[-1] == "!")  # Проверьте, заканчивается ли строка text на восклицательный знак.
print(text.upper())
print(text.lower()) # Преобразуйте всю строку в нижний или верхний регистр

