# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

quantity = random.randint(5, 10)
number_list = []
count = quantity * -1 
print(quantity)

while count < quantity + 1:
    number_list.append(count)
    count += 1
print(number_list)

result_list = []
count = 0

while count < quantity + 1:
    result_list.append(number_list[count] * number_list[- 1 - count])
    count += 1

with open("task_2_4.txt", "w") as data:
    for item in result_list:
        data.write(f'{str(item)} \n')
    data.close()


