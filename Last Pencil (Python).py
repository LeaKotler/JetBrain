import random


def init_pencils():
    pencils = input("How many pencils would you like to use: ")
    while not pencils.isnumeric() or int(pencils) == 0:
        if not pencils.isnumeric():
            print("The number of pencils should be numeric")
        elif int(pencils) == 0:
            print("The number of pencils should be positive")
        pencils = input()
    return int(pencils)


def init_player(player_1, player_2):
    player_ = input(f"Who will be the first ({player_1}, {player_2}): ")
    while player_ not in (player_1, player_2):
        print(f"Choose between '{player_1}' and '{player_2}'")
        player_ = input()
    return player_


def player_choice(c_pencils):
    chosen_pencils = input()
    while not chosen_pencils.isnumeric() or int(chosen_pencils) not in moves or int(chosen_pencils) > c_pencils:
        if not chosen_pencils.isnumeric() or int(chosen_pencils) not in moves:
            print(f"Possible values: '{moves[0]}', '{moves[1]}' or '{moves[2]}'")
        elif int(chosen_pencils) > c_pencils:
            print("Too many pencils were taken")
        chosen_pencils = input()
    return int(chosen_pencils)


def bot_choice(c_pencils):
    is_winning = c_pencils % (len(moves) + 1) != 1
    if is_winning:
        chosen_pencils = (c_pencils - 1) % (len(moves) + 1)
    else:
        chosen_pencils = random.choice(moves)
        while chosen_pencils > c_pencils:
            chosen_pencils = random.choice(moves)
    print(chosen_pencils)
    return chosen_pencils


def game(c_pencils, c_player):
    while c_pencils > 0:
        print("|" * c_pencils)
        print(f"{c_player}'s turn:")
        if c_player == player:
            chosen_pencils = player_choice(c_pencils)
        else:
            chosen_pencils = bot_choice(c_pencils)
        c_pencils -= chosen_pencils
        c_player = player if c_player == bot else bot
    print(f"{c_player} won!")


if __name__ == '__main__':
    player = "John"
    bot = "Jack"
    moves = (1, 2, 3)
    current_pencils = init_pencils()
    current_player = init_player(player, bot)
    game(current_pencils, current_player)
