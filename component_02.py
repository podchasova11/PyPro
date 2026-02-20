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
