number = int(input('Введите пятизначное число: '))

tens_of_thousands = number // 10000
thousands = (number // 1000) % 10 
hundreds = (number // 100) % 10 
tens = (number // 10) % 10 
units = number % 10

step1 = tens ** units
step2 = step1 * hundreds
step3 = step2 / (tens_of_thousands - thousands)

print('Результат:', step3)