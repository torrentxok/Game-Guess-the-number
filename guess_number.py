from random import *
from math import *

unknownNum = randint(1, 100)
print("Добро пожаловать в игру \"Угадай число\"")

def is_valid(text):
    if text.isdigit() and 1<=int(text)<=100:
        return True
    else:
        return False

while True:
    n = input()
    if is_valid(n):
        n = int(n)
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
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