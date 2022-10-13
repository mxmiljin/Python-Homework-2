# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

from os import remove


user_number = list(input("Введите ваше число: "))

for i in user_number:
    if i == "," or i == ".":
        user_number.remove(i)

result = 0
for element in user_number:
    result = result + int(element)
    
print(result)