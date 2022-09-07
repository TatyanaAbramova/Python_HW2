# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

k = int(input("Введите число n: "))
i = 0
for i in range(1, k+1):
    print(f'{i}: {round((1+1/i)**i,3)}', end=', ')
    
res = [(1+1/i)**i for i in range(1, k+1)]
print(f'Сумма последовательности (1+1/k)^k = {round(sum(res),3)}')