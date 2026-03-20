

for fruit in ["apple", "mango", "banana"]:
    print(fruit)

cookies = ["one", "two", "three", "fore", "five"]
for cookie in cookies:
    print(cookie)

message = "Hi today is fine day!"
for char in message:
    print(char.upper())

# Например если надо пройти по списку и удалить пробелы в каждой строке списка

# Иттерация по словарю

person = {
     "name" : "Alice",
     "age" : 35,
     "city" : "New York"

 }

for key, value in person.items():
    print(f"{key} : {value}")

for _ in range(5):
    print("Hello")

# Печать квадратов четных чисел от 0 до 8
for i in range(0, 10, 2):
    print(i**2)

# Печать чисел от 0 до 4
for i in range(5):
    print(i)

#  цикл while

count = 0 # Изначально переменная счетчика = 0
while count < 5: # Пока переменная меньше 5, то выполняй блок кода ниже
    print("Счетчик:", count) # Выводи значение переменной count
    count += 1 # Добавь к ней 1

secret_number = 7
guess = None

while secret_number != guess:
    guess = int(input("Input mark from 1 to 10 : "))
    if guess > secret_number:
        print("Mark bigger then you write")
    elif guess < secret_number:
        print("Mark smaller then you write")
    elif guess == secret_number:
        print("You all right!")

total = 0 # Изначальное значение суммы чисел 0
while total < 100: # Цикл будет выполнятся пока сумма меньше 100
    num = int(input("Введите число: "))
    total += num # Приваляет введенное число в переменную
    print("Сумма:", total)


# Для остановки цикла используется оператор break
# конструкция while True, говорит,
# что цикл будет выполняться пока внутри блока не будет вызван break.

while True:
    answer = input("Хотите продолжить? (да/нет): ")
    if answer.lower() == "нет":
        break

numbers = [1, 2, 3, 4, 5] # Создаем список
for num in numbers: # Перебор элементов
    if num == 3: # Если встретился элемент со значением 3, то останавливай цикл
        break
    print(num)


# Напишите программу, используя цикл for и функцию range(),
# чтобы напечатать все целые числа от 1 до 10 включительно и их квадраты.
# Формат вывода для каждого числа должен быть
# 'Число: X, Квадрат: Y', где X - текущее число, а Y - его квадрат.

for num in range(1, 11):
    print(f"Число : {num}, Квадрат : {num**2}")


secret_number = 55
guess = None

while guess != secret_number:
    guess = int(input("Введите число от 1 до 100: "))
    if guess < secret_number:
        print("Слишком мало")
    elif guess > secret_number:
        print("Слишком много")
    elif guess == secret_number:
        print("Поздравляю! Вы угадали!")
        break        # break аккуратно завершает цикл при совпадении

# Создать пустой список и заполнить его числами от 0 до 100

# Создаем пустой список
numbers = []

# Заполняем числами от 0 до 100 включительно
for num in range(1, 101):
    numbers.append(num)

print(numbers)


# Создаем пустой список
numbers = []

# Заполняем числами от 0 до 100 включительно
for num in range(101):
    numbers.append(num)

print(numbers)


numbers = list(range(101))  # 0..100
while len(numbers) > 51:
    numbers.pop()
print(numbers)


# Работа с файлами чтение
file = open("message.txt", "r")
print(file.read())

# Работа с файлами: перезапись write, когда предыдущая запись стирается
file = open("message.txt", "w")
print(file.write("Yello"))

# Работа с файлами добавление к прежней записи
file = open("message.txt", "a")  # append
print(file.write("\nYes --------------"))
file.close()

file = open("message.txt", "r+")  # + работает на комбинацию действий: чтение и запись одновременно
file.write("Hello")
file.seek(0) # установит курсор на начало строки и то читает строки с начала
print(file.read())
file.close()

# Напишите программу, которая открывает файл,
# читает его построчно и принтит каждую строку.
con = None
file = open("data.txt", "r")
content = file.readlines()
for con in content:
    print(con)

# Примечание: сделайте все через контекстный мененджер!
#
# Напишите скрипт, который запрашивает у пользователя его имя и возраст, а затем записывает эту информацию в файл userinfo.txt.
# Каждая запись должна быть отдельной строкой в файле.

name = input("Input you name :")
age = input("Input you age :")

with open("userinfo.txt", "w+") as file:
    content = file.write(f"{name}\n{age}")
    print(content)

# Примечание: сделайте все через контекстный мененджер!
#
# Создайте original.txt и запишите в него любую информацию.
# Напишите программу, которая копирует
# все содержимое файла original.txt в copy.txt



with (open("original.txt", "w+") as original):
    lines = ["gthdfdfbdb\n",
             "122344455"]
    original.writelines(lines)
    print("Its Okey file original.txt is create and full")

    try:
        with open("copy.txt", "w+") as destination:
            content = original.read()
            destination.write(content)

            print("Its OKEY ALL!")
    except FileNotFoundError:
        print("Error! file original.txt not found")


with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

        name = input("Input your name: ")
        age = input("Input your age: ")

        with open("userinfo.txt", "w", encoding="utf-8") as file:
            file.write(f"{name}\n")
            file.write(f"{age}\n")


name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")

data_line = f"{name}:{age}\n"  # Форматируем строку без лишних слов

with open('userinfo.txt', 'a') as file:
    file.write(data_line)

print("Информация успешно записана в файл userinfo.txt")





with open("original.txt", "w+") as original:
    lines = [
        "gthdfdfbdb\n",
        "122344455\n"
    ]
    original.writelines(lines)
    print("Its Okey file original.txt is created and full")

    original.seek(0)  # вернуться в начало, чтобы читать

    with open("copy.txt", "w+") as destination:
        content = original.read()
        destination.write(content)
        print("Its OKEY ALL!")
