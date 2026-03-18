

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


