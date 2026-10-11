import random

# к — камень, н — ножницы, б — бумага
NAMES = {"к": "камень", "н": "ножницы", "б": "бумага"}
# Кто кого побеждает: камень тупит ножницы, ножницы режут бумагу, бумага накрывает камень
BEATS = {"к": "н", "н": "б", "б": "к"}


def get_winner(player: str, computer: str) -> str:
    """Возвращает 'player', 'computer' или 'draw'."""
    if player == computer:
        return "draw"
    if BEATS[player] == computer:
        return "player"
    return "computer"


def main():
    player_score = 0
    computer_score = 0

    while True:
        print("""Введите к (камень), н (ножницы) или б (бумага).
Если хотите выйти, напишите 0!""")
        choice = input().strip().lower()
        if choice == "0":
            break
        if choice not in NAMES:
            print("Не понял ход, попробуйте ещё раз.\n")
            continue

        computer = random.choice(list(NAMES))
        print(f"Вы: {NAMES[choice]}, компьютер: {NAMES[computer]}")

        winner = get_winner(choice, computer)
        if winner == "player":
            player_score += 1
            print("Вы победили!")
        elif winner == "computer":
            computer_score += 1
            print("Победил компьютер!")
        else:
            print("Ничья!")
        print(f"Счёт — вы {player_score} : {computer_score} компьютер\n")

    print(f"Игра окончена! Итоговый счёт — вы {player_score} : {computer_score} компьютер")


if __name__ == "__main__":
    main()
