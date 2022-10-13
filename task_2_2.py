# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

user_number = int(input("Введите ваше число: "))

x = 1
result = 1
result_list = []

while x < user_number + 1:
    result = result * x
    result_list.append(result)
    x += 1

for element in result_list:
    print(element, end=" - ")