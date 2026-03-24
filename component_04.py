

def summa(a, b):
    return a + b

print(summa(3, 5))

# # nums = [1, 2, 3, 4]
# def max_i_mal(nums):
#     if not nums:
#         raise ValueError("Список пустой")
#     maximal = nums[0]
#
#     for x in nums[1:]:
#         if x > maximal:
#             maximal = x
#     return maximal
# nums = [1, 2, 3, 4]
# print(max_i_mal())

    # for c in range(list):
    #     if a > b:
    #         return maximal() == a
    #     else a < b:
    #         return maximal() == b


nums = [1, 2, 100500]
def max_in_list(nums):
    if not nums:
        raise ValueError("Список пустой")

    m = nums[0]
    for x in nums[1:]:
        if x > m:
            m = x
    return m


print(max_in_list(nums))


# def buy_ticket(full_name, age, adult=False):
#     if age >= 18:
#         print("Билет продан")
#     else:
#         if adult:
#             print("Билет продан под присмотром взрослого")
#         else:
#             print("Нельзя продать билет")


full_name = None
age = None


def buy_ticket(full_name, age, adult=False):
    if age >= 18:
        print("Билет продан")
    elif age < 18 and adult == True:
        print("Билет продан под присмотром взрослого")
    else:
        print("Нельзя продать билет")


buy_ticket("Mila", 25, True)
print(buy_ticket("Mila", 25, True))

numbers = [1, 2, 3, 4, 5, 6, 100500]
def square_numbers(numbers):
    return [x ** 2 for x in numbers]

print(square_numbers(numbers))



class Book:

    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow_book(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

    def get_status(self):
        if self.is_borrowed in True:
            return print("Взята")
        elif self.is_borrowed in False:
            return print("Доступна")


class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow_book(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

    def get_status(self):
        return "Взята" if self.is_borrowed else "Доступна"

    def __str__(self):
        return f"{self.title} — {self.author} ({self.get_status()})"


# Пример использования
book = Book("Война и мир", "Лев Толстой")

print(book)                 # ожидается: Доступна
book.borrow_book()
print(book)                 # ожидается: Взята
book.return_book()
print(book)                 # ожидается: Доступна


class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow_book(self):
        if self.is_borrowed:
            raise ValueError("Книга уже взята")
        self.is_borrowed = True

    def return_book(self):
        if not self.is_borrowed:
            raise ValueError("Нельзя вернуть книгу: она не была взята")
        self.is_borrowed = False

    def get_status(self):
        return "Взята" if self.is_borrowed else "Доступна"

    def __str__(self):
        return f"{self.title} — {self.author} ({self.get_status()})"


# Пример использования
book = Book("Война и мир", "Лев Толстой")

print(book)                 # ожидается: Доступна
book.borrow_book()
print(book)                 # ожидается: Взята
book.return_book()
print(book)                 # ожидается: Доступна



class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow_book(self):
        if self.is_borrowed:
            raise Exception("Книга уже взята")
        self.is_borrowed = True

    def return_book(self):
        if not self.is_borrowed:
            raise Exception("Книга не была взята")
        self.is_borrowed = False

    def get_status(self):
        return "Взята" if self.is_borrowed else "Доступна"

    def __str__(self):
        return f"{self.title} — {self.author} ({self.get_status()})"


book = Book("1984", "Джордж Оруэлл")

print(book)

try:
    book.return_book()   # здесь будет исключение
except Exception as e:
    print("Ошибка:", e)

# сюда уже можно не печатать, чтобы после исключения сценарий не продолжался


class AdvancedBankAccount:
    BANK_NAME = "JP Morgan"

    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Недостаточно средств")

    @property
    def get_balance(self):
        return self._balance

    def transfer_to(self, other_account, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            other_account._balance += amount
            print("Перевод выполнен успешно")
        else:
            print("Недостаточно средств для перевода")

    def __str__(self):
        return f"Владелец: {self.name}, Баланс: {self._balance}"


account1 = AdvancedBankAccount('Алексей', 1000)
account2 = AdvancedBankAccount('Иван', 500)

account1.transfer_to(account2, 300)
print(account1)
print(account2)


class Pets:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("животное издаёт звук")


class Dog(Pets):

    def speak(self):
        return print("Woof")


class Cat(Pets):

    def speak(self):
        print("Meow")


def make_it_speak(pets):
    pets.speak()


dog = Dog("DGFD", 3)
cat = Cat("dfv", 5)


print(make_it_speak(dog))
print(make_it_speak(cat))

class Pets:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("животное издаёт звук")


class Dog(Pets):
    def speak(self):
        print("Woof")


class Cat(Pets):
    def speak(self):
        print("Meow")


# Создаём экземпляры и вызываем speak напрямую
dog = Dog("Биг", 3)
cat = Cat("Персик", 5)

dog.speak()  # → Woof
cat.speak()  # → Meow

class Pets:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}"


class Dog(Pets):
    def speak(self):
        print("Woof")


class Cat(Pets):
    def speak(self):
        print("Meow")


# Пример использования
baron = Dog("Биг", 3)
murka = Cat("Персик", 2)

baron.speak()  # → Woof
murka.speak()  # → Meow

print(baron)   # → Имя: Биг, Возраст: 3
print(murka)   # → Имя: Персик, Возраст: 2
