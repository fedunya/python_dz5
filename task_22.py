# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

def user_input(name, n):    
    _ = 0
    while _ == 0:
        num = input(f'{name}, введи сколько конфет ты возьмешь: ')
        if not num.isdigit() or num == '0': print('Неверный ввод!')
        elif int(num) > n: print(f'На столе осталось только {n} конфет')
        elif int(num) > 28: print(f'{name}, не жадничай, можно взять не более 28 конфет')
        else:
            _ = 1
            num = int(num)
    return num
def lottery(name1, name2):
    _ = random.randint(0, 1)
    if _ == 0: return name1
    else: return name2
def player_vs_bot(candies):
    player1 = 'Vanya_bot'
    print(f'Меня зовут {player1}')    
    player2 = input('А как зовут тебя?: ')
    key = input('Давай узнаем кто будет ходить первым. Нажми Enter ')
    _ = random.randint(0, 1)
    if _ == 0:
        print('Ура! Мой ход первый!')
    else:
        print(f'{player2}, тебе ходить первым((')
    while candies > 0:
        if _ == 0:
            if candies % 29 == 0:
                move = random.randint(1, 28)
            else: move = candies % 29
            candies-= move
            _ = 1
            print(f'Я взял {move} конфет, на столе осталось {candies}. Твой ход')
        else:
            move = user_input(player2, candies)
            candies-= move
            print(f'{player2} взял {move} конфет, на столе осталось {candies}. Теперь мой ход')
            _ = 0
    print('Все))). Конфеты закончились!')
    if _ == 1: print('Ура!!! Я победил. Vanya_bot самый умный')
    else: print(f'{player2}, поздравляю тебя с победой')    
def player_vs_player(candies):
    player1 = input('Первый игрок, введи свое имя: ')        
    player2 = input('Второй игрок, введи свое имя: ')
    key = input('Давай узнаем кто будет ходить первым. Нажми Enter ')
    _ = random.randint(0, 1)
    if _ == 0:
        print(f'{player1}, твой ход первый!')
    else:
        print(f'{player2}, тебе ходить первым')
    while candies > 0:
        if _ == 0:
            move = user_input(player1, candies)
            candies-= move
            print(f'{player1} взял {move} конфет, осталось {candies}. Теперь ход {player2}')            
            _ = 1
        else:
            move = user_input(player2, candies)
            candies-= move
            print(f'{player2} взял {move} конфет, осталось {candies}. {player1}, твой ход')
            _ = 0
    print('Все))). Конфеты закончились!')
    if _ == 1: print(f'{player1} Ты победил. Ты самый умный')
    else: print(f'{player2}, поздравляю тебя с победой')
    return None

import os, random
os.system("cls")
candies = 2021
print('''Вас приветствует игра CANDIES.
Правила игры:
На столе 2021 конфета. За ход можно брать не более 28 конфет.
Выиграет тот кто сделает последний ход и заберет последние конфеты со стола.
''')
_ = input('Будете играть с компьютером(введите 1) или с другом(введите 2): ')
while _ not in ['1', '2']:
    _ = input('Ошибка, повторите ввод: ')
if _ == '1': player_vs_bot(candies)
else: player_vs_player(candies)
