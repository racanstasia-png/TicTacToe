import os

board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

# Імена гравців
players = {}

# Статистика
stats = {"X": 0, "O": 0, "Draw": 0}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_welcome():
    clear_screen()
    print("-" * 50)
    print("ХРЕСТИКИ-НУЛИКИ  🎮".center(50))
    print("-" * 50)
    print("Ласкаво просимо до гри хрестики-нулики!")
    print("-" * 50)
    # Запитуємо імена
    players["X"] = input("Введіть ім'я гравця для Хрестиків (X): ")
    players["O"] = input("Введіть ім'я гравця для Нуликів (O): ")
    print("-" * 50)
    print("ПРАВИЛА ГРИ:")
    print("-" * 50)
    print(f"• Гравець 1: (X) = {players['X']}")
    print(f"• Гравець 2: (O) = {players['O']}")
    print("• Мета: вишикувати 3 свої символи в ряд")
    print("  (по горизонталі, вертикалі або діагоналі)")
    print("-" * 50)
    input("\nНатисніть Enter, щоб почати гру...")

def show_board(board):
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
    player = "X"
    while True:
        show_board(board)
        coordinates = input(f"Хід {players[player]} ({player}) (1 ... 9): ")

        if not (coordinates.isdigit() and len(coordinates) == 1):
            print("Помилка: введи рівно одну цифру")
            continue
        if coordinates not in '123456789':
            print("Помилка: тільки цифри 1-9")
            continue

        num = int(coordinates)
        column = (num - 1) % 3
        line = (num - 1) // 3

        if board[line][column] != "":
            print("Ця клітинка вже зайнята, спробуй іншу")
            continue

        board[line][column] = player
        winner = check_winner(board)
        if winner:
            show_board(board)
            if winner == 'Draw':
                print("Гра завершена. Нічия!")
                stats["Draw"] += 1
            else:
                print(f"Гра завершена. Переможець: {players[winner]} ({winner})")
                stats[winner] += 1

            response = input("Бажаєте зіграти ще раз? (так/ні): ").lower()
            if response != 'так':
                show_stats()
                print("Дякуємо за гру! До побачення!")
                break
            else:
                board_clear()
        player = "O" if player == "X" else "X"

def board_clear():
    for i in range(3):
        for j in range(3):
            board[i][j] = ""

def check_winner(board):
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

def show_stats():
    print("\nСТАТИСТИКА ІГОР:")
    print("-" * 50)
    print(f"Перемог {players['X']} (X): {stats['X']}")
    print(f"Перемог {players['O']} (O): {stats['O']}")
    print(f"Нічиї: {stats['Draw']}")
    print("-" * 50)

if __name__ == "__main__":
    show_welcome()
    play_game()
