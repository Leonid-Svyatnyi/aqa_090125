# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""
alien_color = "red"
colour_green = "green"
colour_red = "red"
colour_yellow = "yellow"

if alien_color in colour_green:
    print('Ви тільки що заробили 5 балів')

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
alien_color = "red"
colour_green = "green"
colour_red = "red"
colour_yellow = "yellow"

if alien_color in colour_green:
    print('Ви тільки що заробили 5 балів')
else:
    print("Ви щойно заробили 10 балів")

# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""
alien_color = ['green', 'red', 'yellow']
colour_green = "green"
colour_red = "red"
colour_yellow = "yellow"

for color in alien_color:
    if color == colour_green:
        print('Ви тільки що заробили 5 балів')
    elif color == colour_red:
        print("Ви щойно заробили 15 балів")
    else:
        print("Ви щойно заробили 10 балів")
# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
pizza_topping = []

while True:
    topping_name = input("Ведіть назву начинки, або напишіть 'quit' для завершення:")
    if topping_name == 'quit':
        break
    else:
        pizza_topping.append(topping_name)
        print(f"Ми додали {topping_name} до Вашої піцци")

print("Загалом ви додали такі начинки:")
for topping_name in pizza_topping:
    print(topping_name)

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""
number = input("Введіть натуральне число: ")
sum_digits = 0

for digit in number:
    sum_digits += int(digit)

print(f"Сума цифр числа {number}: {sum_digits}")

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""
sum_calculation = 0
number_from_user = int(input("Ведіть число:"))
while number_from_user != 0:
    sum_calculation = sum_calculation + number_from_user
    print(sum_calculation)
    number_from_user = int(input("Ведіть число:"))
print(f"Загальна сумма введених чисел: {sum_calculation}")

# task 8
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""
import random
secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 5
print("Вгадайте число від 1 до 20 за 5 спроб!")

while guesses < max_guesses:
    player_gues = int(input("Ведіть ваше значення від 1 до 20:"))
    guesses += 1

    if player_gues == secret_number:
        print("Вітаю ви вгадали!")
        break
    elif player_gues > secret_number:
        print("Ваше число завелике")
    else:
        print("Ваше число замале")

if player_gues != secret_number:
    print(f"Нажаль, ви не вгадали, було загадано: {secret_number}")


# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]

for fruit in fruits:
    if fruit == "orange":
        continue
    print(fruit)

# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [num**2 for num in numbers if num % 2 == 0]
print(result)  #  [4, 16, 36, 64, 100]
