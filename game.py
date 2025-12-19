#svitlana

from Anastasiia import game
from tkinter import Canvas

occupied = []
player = 'X' # поточний гравець

while True:  # цикл 
    



    # Почати відлік часу
    game.start_turn()

    # 1 крок 
    # хід 
    coordinates = input("Твій хід (наприклад, 11, 23, 32): ")
    
    # 2 крок перевірки
    # перевірка на двоцифрове число
    if not (coordinates.isdigit() and len(coordinates) == 2):
        print(" Помилка Введи рівно дві цифри")
        continue 
    
    # Перевірка на правильність кординат
    if coordinates[0] not in '123' or coordinates[1] not in '123':
        print(" Помилка тільки цифри 1, 2, 3")
        continue
    
    # перевірка на зайнятість
    if coordinates in occupied:
        print(" Ця клітинка вже зайнята спробуй іншу")
        continue
    
    #обробка ходу 
    occupied.append(coordinates) 
    # Зберегти хід
game.save(player, coordinates)
# Змінити гравця
player = 'O' if player == 'X' else 'X'
num = int(coordinates) 
line = num % 10         
column = num // 10      

if len(occupied) == 9:
    print("Всі клітинки зайняті")
    # результат 
    print(f" Колонка {column}, рядок {line}")
    
    # print(f" Зайняті клітинки: {occupied}")
    # print("-" * 40)  # для краси


    #Nathaniel

    # код вiдображеня вiкна (интерфейз) - робе вроде хтось iнший - тому в мене його нема й код мiй не запрацюе без нього
# код внuзу це моi функцii та iнше - що е моim обов'язком у цьому проектi
# як працюе функцii i як з ними працювати - я написав бiля коду

# функцiя що малюе поле
def board_draw(canvas):
    size = int(canvas["width"])
    cell = size // 3

    # Горизонтальнi линii
    for i in range(1, 3):
        canvas.create_line(0, i*cell, size, i*cell)

    # Вертикальнi линii
    for i in range(1, 3):
        canvas.create_line(i*cell, 0, i*cell, size)

# зараз не працюе тому що нема коду що створюе холст, ним вроде як займатся хтось iнший
# код пример з яким вiн може запрацювати (такий код ставиться у самому верху):
# import tkinter as tk
# root = tk.Tk()
# root.geometry("500x500")

# canvas = tk.Canvas(root, width=500, height=500)
# canvas.pack()
# root.title("Хрестики Нулики")

def board_clear(canvas):
    # Очищаемо холст вiD ходiB
    canvas.delete("all")
    board_draw(canvas)



#Ivan

# board = ["O", "X", "O"],      використовував для самоперевірки
#            ["X", "O", "X"],
#            ["X", "O", "O"]]]  

def win_board_Hor(board):
    for row_1 in board[0]:
        print("1",row_1)
        if row_1[0] == "X" and row_1[1] == "X" and row_1[2] == "X":
            return "X"
        elif row_1[0] == "O" and row_1[1] == "O" and row_1[2] == "O":
            return "O"
    return None
            
def win_board_Ver(board):
   for i in range(3):
        if board[0][0][i]=="X" and board[0][1][i]=="X" and board[0][2][i]=="X":
            return "X"
            
            
        elif board[0][0][i]=="O" and board[0][1][i]=="O" and board[0][2][i]=="O":
            return "O"
        
   return None 

def win_board_Dia(board):
    if board[0][0][0]=="X" and board[0][1][1]=="X" and board[0][2][2]=="X" or board[0][0][2]=="X" and board[0][1][1]=="X" and board[0][2][0]=="X":
            return "X"
    elif board[0][0][0]=="O" and board[0][1][1]=="O" and board[0][2][2]=="O" or board[0][0][2]=="O" and board[0][1][1]=="O" and board[0][2][0]=="O":
        return "O"
        
    return None

def free_cell_board(board):
    free_found = False
    for i in range(3):
        for j in range(3):
            cell = board[0][i][j]
            if cell == "":
                free_found = True  
            else:
                pass
    if free_found is True:
        print("free")
    else:
        print("busy")

#Maxim

from Anastasiia import game

def welcome_players():
    print("Ласкаво просимо до гри хрестики-нулики!")
    player1 = input("Введіть ім'я гравця 1 (Х): ")
    player2 = input("Введіть ім'я гравця 2 (О): ")
    game.set_players(player1, player2)
    return player1, player2

def game_ended(winner):
    print("Гра завершена.")
    print("Переміжець:", winner)
    game.ask()
    response = input("Бажаєте зіграти ще раз? (так/ні): ").lower()
    if response!='так':
        print("Дякуємо за гру! До побачення!")
        exit()
while True:
    player1, player2 = welcome_players()
        # Код гри
    winner = player1  # Тимчасовий переможець для прикладу, щоб правильно написати хто переміг треба знати логіку гри
    game_ended(winner)

    #Arian
