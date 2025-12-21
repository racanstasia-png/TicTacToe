"""Простий і компактний Tic-Tac-Toe.

Мінімалістична версія: ходи вводяться як 'a1', 'b3' тощо (рядок+стовпець).
Функції: check_winner, is_draw, короткий CLI.
"""

def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def print_board(b):
    print("  1 2 3")
    for i, row in enumerate(b):
        print(chr(ord("a") + i), "", " ".join(row))


def check_winner(b):
    # rows/cols
    for i in range(3):
        if b[i][0] != " " and b[i][0] == b[i][1] == b[i][2]:
            return b[i][0]
        if b[0][i] != " " and b[0][i] == b[1][i] == b[2][i]:
            return b[0][i]
    # diagonals
    if b[0][0] != " " and b[0][0] == b[1][1] == b[2][2]:
        return b[0][0]
    if b[0][2] != " " and b[0][2] == b[1][1] == b[2][0]:
        return b[0][2]
    return None


def is_draw(b):
    return all(cell != " " for row in b for cell in row) and check_winner(b) is None


def parse_move(move):
    move = move.strip().lower()
    if len(move) != 2:
        return None
    r = ord(move[0]) - ord('a')
    c = ord(move[1]) - ord('1')
    if 0 <= r < 3 and 0 <= c < 3:
        return r, c
    return None


def main():
    p1 = input("Ім'я гравця X: ") or "X"
    p2 = input("Ім'я гравця O: ") or "O"
    players = {'X': p1, 'O': p2}
    while True:
        board = create_board()
        turn = 'X'
        while True:
            print()
            print_board(board)
            mv = input(f"{players[turn]} ({turn}) — введіть хід (наприклад a1) або 'q' для виходу: ").strip()
            if mv.lower() in ('q', 'quit'):
                print('Вихід')
                return
            pos = parse_move(mv)
            if not pos:
                print('Невірний хід. Формат: a1..c3')
                continue
            r, c = pos
            if board[r][c] != ' ':
                print('Клітинка зайнята')
                continue
            board[r][c] = turn
            w = check_winner(board)
            if w:
                print_board(board)
                print(f"Переміг {players[w]} ({w})")
                break
            if is_draw(board):
                print_board(board)
                print('Нічия')
                break
            turn = 'O' if turn == 'X' else 'X'
        again = input('Зіграти ще раз? (так/ні): ').strip().lower()
        if again != 'так':
            print('Дякую за гру')
            break


if __name__ == '__main__':
    main()