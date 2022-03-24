from random import *
from math import *

print("Добро пожаловать в игру \"Угадай число\"")

def is_valid(text, level):
    if text.isdigit() and 1<=int(text)<=level:
        return True
    else:
        return False

def level_is_valid(text):
    if text.isdigit() and int(text)>=100:
        return True
    else:
        return False

print('Введите уровень сложности (введите число, не меньше 100)')

unknownNum = None
levelNum = None

while True:
    levelNum = input()
    if level_is_valid(levelNum):
        levelNum = int(levelNum)
        unknownNum = randint(1, levelNum)
        break
    else:
        print('Ведите корректный уровень')


print('Введите число!')

while True:
    n = input()
    if is_valid(n, levelNum):
        n = int(n)
    else:
        print(f'А может быть все-таки введем целое число от 1 до {levelNum}?')
        continue
    if n > unknownNum:
        print('Ваше число больше загаданного, попробуйте еще разок')
        continue
    elif n < unknownNum:
        print('Ваше число меньше загаданного, попробуйте еще разок') 
        continue
    else:
        print('Вы угадали, поздравляем!')
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')