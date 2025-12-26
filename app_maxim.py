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
    print("ХРЕСТИКИ-НУЛИКИ 2.0 🎮".center(50))
    print("-" * 50)
    print("Ласкаво просимо до оновленої гри!")
    print("-" * 50)
    print("НОВІ ПРАВИЛА:")
    print("• Кожен гравець може мати лише 3 фігури на полі.")
    print("• Коли ви робите 4-й хід, ваш найстаріший хід зникає!")
    print("-" * 50)
    print(" ЯК ГРАТИ:")
    print("• Введіть номер клітинки (1-9)")
    print("• Схема поля:\n")
    print("     1 | 2 | 3")
    print("     ---------")
    print("     4 | 5 | 6")
    print("     ---------")
    print("     7 | 8 | 9")
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
    player = "X"
    
    # Словник для збереження історії ходів
    # Формат: {'X': [(рядок, колонка)], 'O': [(рядок, колонка)]}
    moves_history = {'X': [], 'O': []}

    while True:
        show_board(board)
        
        # Підказка гравцю, який хід зникне
        if len(moves_history[player]) == 3:
            rem_r, rem_c = moves_history[player][0]
            rem_num = rem_r * 3 + rem_c + 1
            print(f"⚠️ Увага! Цей хід видалить вашу фігуру на позиції {rem_num}")

        coordinates = input(f"Хід {player} (1 ... 9): ")
        
        # Перевірки введення
        if not (coordinates.isdigit() and len(coordinates) == 1):
            print(" Помилка! Введи рівно одну цифру")
            input("Натисніть Enter...")
            continue 
        
        if coordinates not in '123456789':
            print(" Помилка! Тільки цифри 1-9")
            input("Натисніть Enter...")
            continue
        
        num = int(coordinates) 
        column = (num-1) % 3   
        line = (num-1) // 3

        # Перевірка на зайнятість
        if board[line][column] != "":
            print("Ця клітинка вже зайнята!")
            input("Натисніть Enter...")
            continue
        
        # Логіка зникнення старого ходу
        # Якщо у списку вже є 3 ходи, видаляємо найстаріший
        if len(moves_history[player]) == 3:
            old_line, old_col = moves_history[player].pop(0) # Видаляємо перший (найстаріший) запис зі списку
            board[old_line][old_col] = "" # Стирання з дошки

        # Записуємо новий хід
        board[line][column] = player 
        moves_history[player].append((line, column)) # Додаємо нові координати в кінець словника

        winner = check_winner(board)
        if winner:
            show_board(board)
            if winner == 'Draw':
                print("Нічия!") # У цьому режимі нічия майже неможлива
            else:
                print(f"Гра завершена. Переможець: {winner}")
            
            response = input("Бажаєте зіграти ще раз? (так/ні): ").lower()
            if response != 'так':
                print("Дякуємо за гру! До побачення!")
                break
            else:
                board_clear()
                moves_history = {'X': [], 'O': []} # Очищаємо історію для нової гри
                # player залишається тим, хто виграв або програв, або можна скинути на X
        
        player = "O" if player == "X" else "X"


def board_clear():
    """Очищення ігрового поля"""
    for i in range(3):
        for j in range(3):
            board[i][j] = ""


def check_winner(board):
    """Перевірка переможця"""
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    
    for combo in win_combinations:
        s1 = board[combo[0] // 3][combo[0] % 3]
        s2 = board[combo[1] // 3][combo[1] % 3]
        s3 = board[combo[2] // 3][combo[2] % 3]
        if s1 == s2 == s3 and s1 in ['X', 'O']:
            return s1
    
    if all(cell in ['X', 'O'] for row in board for cell in row):
        return 'Draw'
    
    return None


if __name__ == "__main__":
    show_welcome()
    play_game()
    