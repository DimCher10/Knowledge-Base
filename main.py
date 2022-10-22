info = input("Введите данные: ").split()
# info - список ['Иван', 'Семёнов']

for i in range(len(info)):
    info[i] = info[i].capitalize()

length = len(info)
second_name = None

if length == 2:
    name, surname = info
elif length == 3:
    name, second_name, surname = info
else:
    print("Введите корректное значение")
    
print(f"Имя: {name}")
if second_name:
    print(f"Отчество: {second_name}")
print(f"Фамилия: {surname}")
