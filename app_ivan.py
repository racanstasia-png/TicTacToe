import os

board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

def clear_screen():
    """Очищення екрану консолі"""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_welcome():
    """Привітання та пояснення правил"""
    clear_screen()
    print("-" * 50)
    print("ХРЕСТИКИ-НУЛИКИ  🎮".center(50))
    print("-" * 50)
    print("Ласкаво просимо до гри хрестики-нулики!")
    print("-" * 50)
    print("ПРАВИЛА ГРИ:")
    print("-" * 50)
    print("• Гра для двох гравців")
    print("• Гравець 1: (X)")
    print("• Гравець 2: (O)")
    print("• Мета: вишикувати 3 свої символи в ряд")
    print("  (по горизонталі, вертикалі або діагоналі)")
    print("-" * 50)
    print(" ЯК ГРАТИ:")
    print("-" * 50)
    print("• Введіть номер клітинки (1-9) для свого ходу")
    print("• Розташування клітинок на полі:\n")
    print("     1 | 2 | 3")
    print("     ---------")
    print("     4 | 5 | 6")
    print("     ---------")
    print("     7 | 8 | 9")
    print("\nЧас кожного ходу буде зафіксовано!")
    print("-" * 50)
    input("\nНатисніть Enter, щоб почати гру...")


def show_board(board):
    """Відображення ігрового поля"""
    clear_screen()
    print("Поточне ігрове поле:\n")
    for i, row in enumerate(board):
        print(" ", end="")
        for j, cell in enumerate(row):
            print(cell if cell != "" else " ", end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print("-----------")
    print()

def play_game():
    """Основна логіка гри"""
    player="X"
    while True:  # цикл 
      show_board(board)
      # 1 крок 
      # хід 
      coordinates = input(f"Хід {player} (1 ... 9): ")
      
      # 2 крок перевірки
      # перевірка на двоцифрове число
      if not (coordinates.isdigit() and len(coordinates) == 1):
          print(" Помилка Введи рівно одну цифру")
          continue 
      
      # Перевірка на правильність кординат
      if coordinates not in '123456789':
          print(" Помилка тільки цифри 1, 2, 3, 4, 5, 6, 7, 8, 9")
          continue
      
      num = int(coordinates) 
      column = (num-1) % 3   
      line = (num-1) // 3

      # перевірка на зайнятість
      if board[line][column] != "":
          print("Ця клітинка вже зайнята спробуй іншу")
          continue
      
      #обробка ходу 
      board[line][column] = player  # або "O" в залежності від гравця
      winner = win_board_Hor(board) or win_board_Ver(board) or win_board_Dia(board)
      if winner:
        show_board(board)
        print("win ", winner)
        response = input("Бажаєте зіграти ще раз? (так/ні): ").lower()
        if response != 'так':
          print("Дякуємо за гру! До побачення!")
          break
        else:
          board_clear()
          player="X"
          continue

      if not free_cell_board((board)):
        show_board(board)
        print("Нічия")
        response = input("Бажаєте зіграти ще раз? (так/ні): ").lower()
        if response != 'так':
          print("Дякуємо за гру! До побачення!")
          break
        else:
          board_clear()
          player="X"
          continue
          
      # переміна гравця
      player = "O" if player == "X" else "X"


def board_clear():
    """Очищення ігрового поля"""
    for i in range(3):
        for j in range(3):
            board[i][j] = ""


def win_board_Hor(board):
    for row in board:  

        if row[0] == "X" and row[1] == "X" and row[2] == "X":
            return "X"
        
        elif row[0] == "O" and row[1] == "O" and row[2] == "O":
            return "O"
        
    return None
            
            
    

def win_board_Ver(board):
   for i in range(3):
        if board[0][i]=="X" and board[1][i]=="X" and board[2][i]=="X":
            return "X"
            
            
        elif board[0][i]=="O" and board[1][i]=="O" and board[2][i]=="O":
            return "O"
            
        
   return None
            
   

def win_board_Dia(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] in ("X", "O"): 
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] in ("X", "O"): 
        return board[0][2] 
    

    return None





    

    



def free_cell_board(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                return True  
    return False
        









if __name__ == "__main__":
    show_welcome()
    play_game()
