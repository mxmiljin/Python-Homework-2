# Реализуйте алгоритм перемешивания списка.

from random import randint 


user_list = list("It seems that the program is working")
i = 0

while i < len(user_list):
    x = randint(0, len(user_list) - 1)
    y = user_list[i]
    user_list[i] = user_list[x]
    user_list[x] = y
    i += 1

for element in user_list:
    print(element, end=" - ")




    