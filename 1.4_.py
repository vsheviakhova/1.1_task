a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

a_safe = a
a = b
b = c
c = a_safe

print(f'Число а: {a}')
print(f'Число b: {b}')
print(f'Число c: {c}')
