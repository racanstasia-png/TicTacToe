def welcome_players():
    print("Ласкаво просимо до гри хрестики-нолики!")
    player1 = input("Введіть ім'я гравця 1 (Х): ")
    player2 = input("Введіть ім'я гравця 2 (О): ")
    return player1, player2
def game_ended(winner):
    print("Гра завершена.")
    print("Переміжець:", winner)
    response = input("Бажаєте зіграти ще раз? (так/ні): ").lower()
    if response!='так':
        print("Дякуємо за гру! До побачення!")
        exit()
while True:
    player1, player2 = welcome_players()
        # Код гри
    winner = player1  # Тимчасовий переможець для прикладу, щоб правильно написати хто переміг треба знати логіку гри
    game_ended(winner)