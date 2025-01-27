alice_in_wonderland = ("Would you tell me, please, which way I ought to go from here?\n"
                       "That depends a good deal on where you want to get to,said the Cat.\n"
                       "I don't much care where —— said Alice.\n"
                       "Then it doesn't matter which way you go, said the Cat.\n"
                       "—— so long as I get somewhere, Alice added as an explanation.\n"
                       "Oh, you're sure to do that, said the Cat, if you only walk long enough.")
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
area_black_sea = 436402
area_azov_sea = 37800
total_area = area_black_sea + area_azov_sea
print("Total area of Black and Azov see is:", total_area)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
sum_first_and_second_store = 250449
sum_second_and_third_store = 222950
total_amount = 375291
third_store = total_amount - sum_first_and_second_store
second_store = sum_second_and_third_store - third_store
first_store = sum_first_and_second_store - second_store
print("На першому склади було:", first_store, "товарів\n"
      "На другому складі було:", second_store, "товарів\n"
      "На третьому складі було:", third_store, "товарів")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
total_month = 18
payment_each_month = 1179
total_price = total_month * payment_each_month

print("Вартість комп’ютера дорівнює", total_price, "грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
result_a = 8019 % 8
result_b = 9907 % 9
result_c = 2789 % 5
result_d = 7248 % 6
result_e = 7128 % 5
result_f = 19224 % 9

print("Остача від ділення чисел а =", result_a, "\n"
"Остача від ділення чисел b =", result_b, "\n"
"Остача від ділення чисел c =", result_c, "\n"
"Остача від ділення чисел d =", result_d, "\n"
"Остача від ділення чисел e =", result_e, "\n"
"Остача від ділення чисел f =", result_f)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_big_quantity = 4
pizza_big_price = 274
total_big_pizza = pizza_big_quantity * pizza_big_price
pizza_medium_quantity = 2
pizza_medium_price = 218
total_medium_pizza = pizza_medium_quantity * pizza_medium_price
juice_quntity = 4
juice_price = 35
total_juice = juice_quntity * juice_price
cake_quantity = 1
cake_price = 350
total_cake = cake_quantity * cake_price
water_quantity = 3
water_price = 21
total_water = water_quantity * water_price
total_payment = total_water + total_cake + total_juice +total_medium_pizza + total_big_pizza

print("Для покупки всіх товарів знадобиться", total_payment, "грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photo = 232
one_page = 8

if total_photo % one_page == 0:
     total_page = total_photo / one_page
else:
    total_page = total_photo // one_page + 1

print("Що б вклеїти всі фото знадобиться", total_page, "сторінок")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
trip_distance = 1600
fuel_loss_100_km = 9
tank_size = 48

total_gas = trip_distance / 100 * fuel_loss_100_km
number_of_stops = total_gas // tank_size

print(total_gas, "літрів бензину знадобиться для подорожі\n",
      number_of_stops," зупинок знадобиться, щою кожного разу заправляти повний бак")
