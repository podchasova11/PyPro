

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


