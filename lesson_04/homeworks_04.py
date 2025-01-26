adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

one_line_advanture_text = adwentures_of_tom_sawer.replace("\n", " ")
print(one_line_advanture_text)

# task 02 ==
""" Замініть .... на пробіл
"""
advanture_text_without_four_dots = one_line_advanture_text.replace("....", " ")
# for better visibility and to check correctness of code has been added print fuction
# print(advanture_text_without_four_dots)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
advanture_one_space_text = " ".join(advanture_text_without_four_dots.split())
# for better visibility and to check correctness of code has been added print fuction
# print(advanture_one_space_text)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = advanture_one_space_text.count("h")
print(f"Літера 'h' зустрічається {count_h} разів")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = advanture_one_space_text.split()
count_capitalize = 0
for word in words:
    if word[0].isupper():
        count_capitalize += 1
print(f"Кількість слів, що починаються з великої літери: {count_capitalize}")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
index_Tom = advanture_one_space_text.find("Tom")
second_index_Tom = advanture_one_space_text.find("Tom", index_Tom+1)
print(f"Позиція на якій слово Tom зустрічається вдруге {second_index_Tom}")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = advanture_one_space_text.split(". ")
# for better visibility and to check correctness of code has been added print fuction
# print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
print(fourth_sentence)


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
text_to_string = '. '.join(adwentures_of_tom_sawer_sentences)
print(text_to_string)
index = text_to_string.find("By the time")
if index != -1:
    print("Є речення, що починається з 'By the time'")
else:
    print("Немає речення, яке починається з 'By the time'")


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
print(last_sentence)
last_sentence_split = last_sentence.split()
last_sentece_count = len(last_sentence_split)
print("Word count in the last sentence:", last_sentece_count)
