# def is_even(number):
#     return number % 2 == 0

# number = int(input("Введите число: "))

# Тернарный оператор
# print("Число четное" if is_even(number) else "Число нечетное")

# Используя целочисленную арифметику (не строки), 
# переставить местами цифры в записи числа трехзначного числа
# Введите число: 276
# Ответ: 672

# number = int(input("Введите число: "))

# number1 = number % 10
# number2 = number // 10 % 10 
# number3 = number // 10 // 10 % 10
# print(number1, number2, number3, sep='')

###

# Введите число: 23673
# В этом числе цифр: 5

# Введите число: 23673
# В этом числе "чётных цифр": 2
number = int(input("Введите число: "))
digits = 0

while number > 0:
    
    if number % 2 == 0:
        digits += 1
    number //= 10

print(f"В этом числе четных цифр: {digits}")
