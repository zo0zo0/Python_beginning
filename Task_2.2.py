'''
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
'''

s = int(input('Задай сумму двух чисел \n'))
p = int(input('Задай произведение чисел \n'))
for _ in range(s):
    for y in range(p):
        if s == _ + y and p == _ * y:
            print(f'первое число ="{_}", второе число ="{y}"')
