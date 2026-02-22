m = int(input('Введите максимальную массу лодки (кг) : '))
n = int(input('Введите количество рыбаков: '))

weights = []

print(f'Введите вес каждого рыбака (в кг) : ')
for i in range(n):
    weight = int(input())
    weights.append(weight)

weights.sort()

boats = 0

left = 0 
right = n - 1 

while left <= right:
    if weights[left] + weights[right] <= m:
        left += 1
        right -= 1
    else:
        right -= 1

    boats += 1

print(f'Минимальное количество лодок: {boats}')
