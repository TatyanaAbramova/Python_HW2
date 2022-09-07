# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def compos(n):
    if n == 1:
        return 1
    else:
        return n * compos(n - 1)

num = int(input('Введите число N: '))
list = []
for a in range(1, num + 1):
    list.append(compos(a))

print(f'N = {num}, тогда {list}')