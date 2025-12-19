import time
import os
from statistics import mean

def clear_screen():
    """Очищення екрану консолі"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_welcome():
    """Привітання та пояснення правил"""
    clear_screen()
    print("-" * 50)
    print("🎮  ХРЕСТИКИ-НУЛИКИ  🎮".center(50))
    print("-" * 50)
    print("Ласкаво просимо до гри хрестики-нулики!")
    print("-" * 50)
    print("📋 ПРАВИЛА ГРИ:")
    print("-" * 50)
    print("• Гра для двох гравців")
    print("• Гравець 1: ❌ (X)")
    print("• Гравець 2: ⭕ (O)")
    print("• Мета: вишикувати 3 свої символи в ряд")
    print("  (по горизонталі, вертикалі або діагоналі)")
    print("-" * 50)
    print("📝 ЯК ГРАТИ:")
    print("-" * 50)
    print("• Введіть номер клітинки (1-9) для свого ходу")
    print("• Розташування клітинок на полі:\n")
    print("     1 | 2 | 3")
    print("     ---------")
    print("     4 | 5 | 6")
    print("     ---------")
    print("     7 | 8 | 9")
    print("\n⏱️  Час кожного ходу буде зафіксовано!")
    print("-" * 50)
    input("\n▶️  Натисніть Enter, щоб почати гру...")

    print(f"✅ Чудово! {player1} vs {player2}")
    input("▶️  Натисніть Enter, щоб почати гру...")
    
    return player1, player2

def show_board(board):
    """Відображення ігрового поля"""
    clear_screen()
    print("\n" + "-" * 50)
    print("🎮  ІГРОВЕ ПОЛЕ  🎮".center(50))
    print("-" * 50 + "\n")
    
    # Відображення поля з красивим форматуванням
    for i in range(0, 9, 3):
        row = []
        for j in range(3):
            cell = board[i + j]
            if cell == 'X':
                row.append('❌')
            elif cell == 'O':
                row.append('⭕')
            else:
                row.append(f' {cell} ')
        print("     " + " | ".join(row))
        if i < 6:
            print("    " + "-" * 13)
    print()

def check_winner(board):
    """Перевірка переможця"""
    # Всі можливі комбінації для перемоги
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонталі
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикалі
        [0, 4, 8], [2, 4, 6]               # Діагоналі
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] in ['X', 'O']:
            return board[combo[0]]
    
    # Перевірка на нічию
    if all(cell in ['X', 'O'] for cell in board):
        return 'Draw'
    
    return None

def get_move(board, player, player_num):
    """Отримання ходу від гравця з таймером"""
    while True:
        show_board(board)
        print(f"{'-' * 50}")
        print(f"🎯 Хід гравця {player_num} ({player})".center(50))
        print(f"{'-' * 50}\n")
        
        start_time = time.time()
        try:
            move = input(f"▶️  Введіть номер клітинки (1-9): ")
            end_time = time.time()
            
            if not move.isdigit():
                input("❌ Помилка! Введіть число від 1 до 9. [Enter]")
                continue
            
            move = int(move) - 1
            
            if move < 0 or move > 8:
                input("❌ Помилка! Число має бути від 1 до 9. [Enter]")
                continue
            
            if board[move] in ['X', 'O']:
                input("❌ Ця клітинка вже зайнята! [Enter]")
                continue
            
            move_time = end_time - start_time
            return move, move_time
            
        except (ValueError, IndexError):
            input("❌ Некоректне введення! Спробуйте ще раз. [Enter]")

def replay_game(game_data):
    """Повтор гри - показує кожен хід"""
    clear_screen()
    print("\n" + "-" * 50)
    print("🎬  ПОВТОР ГРИ  🎬".center(50))
    print("-" * 50 + "\n")
    
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    print(f"🎮 {game_data['player1_name']} (❌) vs {game_data['player2_name']} (⭕)\n")
    input("▶️  Натисніть Enter, щоб почати повтор...")
    
    for move_num, move_data in enumerate(game_data['moves'], 1):
        clear_screen()
        print("\n" + "-" * 50)
        print(f"🎬  ХІД #{move_num}  🎬".center(50))
        print("-" * 50 + "\n")
        
        # Показати поле
        for i in range(0, 9, 3):
            row = []
            for j in range(3):
                cell = board[i + j]
                if cell == 'X':
                    row.append('❌')
                elif cell == 'O':
                    row.append('⭕')
                else:
                    row.append(f' {cell} ')
            print("     " + " | ".join(row))
            if i < 6:
                print("    " + "-" * 13)
        
        print("\n" + "-" * 50)
        print(f"👤 {move_data['player_name']} ({move_data['symbol']}) обрав клітинку {move_data['position']}")
        print(f"⏱️  Час ходу: {move_data['time']:.2f} секунд")
        print("-" * 50)
        
        # Оновити поле
        board[move_data['position'] - 1] = move_data['symbol']
        
        input("\n▶️  Натисніть Enter для наступного ходу...")
    
    # Показати фінальне поле
    clear_screen()
    print("\n" + "-" * 50)
    print("🏁  ФІНАЛЬНЕ ПОЛЕ  🏁".center(50))
    print("-" * 50 + "\n")
    
    for i in range(0, 9, 3):
        row = []
        for j in range(3):
            cell = board[i + j]
            if cell == 'X':
                row.append('❌')
            elif cell == 'O':
                row.append('⭕')
            else:
                row.append(f' {cell} ')
        print("     " + " | ".join(row))
        if i < 6:
            print("    " + "-" * 13)
    
    print("\n" + "-" * 50)
    print(f"🎉  Переможець: {game_data['winner']}")
    print("-" * 50)
    
    input("\n▶️  Натисніть Enter, щоб продовжити...")

def show_statistics(game_history):
    """Показати статистику всіх ігор"""
    clear_screen()
    print("\n" + "-" * 50)
    print("📊  СТАТИСТИКА ІГОР  📊".center(50))
    print("-" * 50 + "\n")
    
    for game_num, game in enumerate(game_history, 1):
        print(f"🎮 Гра #{game_num}")
        print("-" * 50)
        print(f"Переможець: {game['winner']}")
        print(f"Загальна тривалість гри: {game['total_time']:.2f} секунд")
        print(f"Кількість ходів: {game['total_moves']}")
        
        if game['move_times']:
            print(f"\n⏱️  Статистика часу ходів:")
            print(f"   • Найшвидший хід: {min(game['move_times']):.2f} сек")
            print(f"   • Найдовший хід: {max(game['move_times']):.2f} сек")
            print(f"   • Середній час ходу: {mean(game['move_times']):.2f} сек")
        
        if game['player1_times']:
            print(f"\n👤 Гравець 1 (❌):")
            print(f"   • Середній час ходу: {mean(game['player1_times']):.2f} сек")
            print(f"   • Найшвидший хід: {min(game['player1_times']):.2f} сек")
            print(f"   • Найдовший хід: {max(game['player1_times']):.2f} сек")
        
        if game['player2_times']:
            print(f"\n👤 Гравець 2 (⭕):")
            print(f"   • Середній час ходу: {mean(game['player2_times']):.2f} сек")
            print(f"   • Найшвидший хід: {min(game['player2_times']):.2f} сек")
            print(f"   • Найдовший хід: {max(game['player2_times']):.2f} сек")
        
        print("\n" + "-" * 50 + "\n")
    
    input("▶️  Натисніть Enter, щоб продовжити...")

def play_game():
    """Основна функція гри"""
    game_history = []
    
    while True:
        show_welcome()
        
        # Ініціалізація гри
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        current_player = 'X'
        player_num = 1
        game_start = time.time()
        move_times = []
        player1_times = []
        player2_times = []
        
        # Ігровий цикл
        while True:
            move, move_time = get_move(board, current_player, player_num)
            board[move] = current_player
            move_times.append(move_time)
            
            if current_player == 'X':
                player1_times.append(move_time)
            else:
                player2_times.append(move_time)
            
            winner = check_winner(board)
            
            if winner:
                show_board(board)
                game_end = time.time()
                total_time = game_end - game_start
                
                print("-" * 50)
                if winner == 'Draw':
                    print("🤝  НІЧИЯ!  🤝".center(50))
                    winner_text = "Нічия"
                else:
                    winner_symbol = '❌' if winner == 'X' else '⭕'
                    winner_num = 1 if winner == 'X' else 2
                    print(f"🎉  ПЕРЕМОЖЕЦЬ: Гравець {winner_num} ({winner_symbol})  🎉".center(50))
                    winner_text = f"Гравець {winner_num} ({winner_symbol})"
                print("-" * 50)
                
                # Збереження статистики гри
                game_history.append({
                    'winner': winner_text,
                    'total_time': total_time,
                    'total_moves': len(move_times),
                    'move_times': move_times,
                    'player1_times': player1_times,
                    'player2_times': player2_times
                })
                
                print(f"\n⏱️  Гра тривала: {total_time:.2f} секунд")
                print(f"🔢 Загальна кількість ходів: {len(move_times)}")
                
                input("\n▶️  Натисніть Enter, щоб побачити детальну статистику...")
                break
            
            # Зміна гравця
            current_player = 'O' if current_player == 'X' else 'X'
            player_num = 2 if player_num == 1 else 1
        
        # Показати статистику всіх ігор
        show_statistics(game_history)
        
        # Запит на повтор гри
        while True:
            choice = input("\n🔄 Бажаєте зіграти ще раз? (так/ні): ").lower()
            if choice in ['так', 'т', 'yes', 'y']:
                break
            elif choice in ['ні', 'н', 'no', 'n']:
                clear_screen()
                print("\n" + "-" * 50)
                print("👋  Дякуємо за гру!  👋".center(50))
                print("-" * 50 + "\n")
                return
            else:
                print("❌ Введіть 'так' або 'ні'")

# Запуск гри
if __name__ == "__main__":
    play_game()
