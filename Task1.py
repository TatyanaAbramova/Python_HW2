# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = float(input('Введите число: '))
def res_nums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

print(f'Сумма цифр числа = {res_nums(num)}')