import random


def switch_players(turn):
    if turn[0] == True and turn[1] == False:
        turn = [False, True]
        return turn
    elif turn[0] == False and turn[1] == True:
        turn = [True, False]
        return turn

def cpu_choise(board):
    while True:
        index_random = random.randint(1,9)
        for index, value in enumerate(board):
            if index == index_random and value == ' ':
                return index_random

def pick_place(board, turn, P1, P2):
    while True:
        if turn[0]: # checks which player turn is it
            player_turn = p1_name
        elif turn[1]:
            player_turn = p2_name
        elif turn[0] and turn[1] == False:
            player_turn = 'CPU'

        try:
            print_board(board)
            while True: #loop to check valid input
                if (man_v_machine == 'PC') and (player_turn == p2_name):
                    board[cpu_choise(board)] = P2
                    is_win_or_tie = check_win_or_tie(board)
                    turn = switch_players(turn)
                    break
                try:
                    print(f"\nTurn is: {player_turn}")
                    chosen_index = int(input("Choose Place 1-9: ")) - 1
                    if 1 <= chosen_index + 1 <= 9:
                        break
                    else:
                        raise Exception("Make sure to only give numbers between 1 - 9!")
                except Exception as e:
                    print("\nAn error has occured!")
                    print("\nMake sure to only give numbers between 1 - 9!")

            for index, value in enumerate(board):
                if index == chosen_index and value == ' ':
                    if player_turn == p1_name:
                        board[index] = P1
                        is_win_or_tie = check_win_or_tie(board)
                        turn = switch_players(turn)
                    elif player_turn == p2_name:
                        board[index] = P2
                        is_win_or_tie = check_win_or_tie(board)
                        turn = switch_players(turn)
                elif index == chosen_index and value != ' ':
                    raise Exception("Place is already Taken!")
        except Exception as e:
            print("\nAn error has occured!")
            print(e)
            print()
        if is_win_or_tie == "W":
            global player_won
            player_won = player_turn
            if player_won == p1_name:
                game_score[0] += 1
            elif player_won == p2_name:
                game_score[1] += 1
            print_board(board)
            return "Win"
        elif is_win_or_tie == "T":
            print_board(board)
            return "Tie"

def print_board(board):
    print("\nBoard:")
    for index, value in enumerate(board):
            print(f"[{value}]", end=" ")
            if (index + 1) % 3 == 0:
                print()

def check_win_or_tie(board):
    win_conditions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for index1, index2, index3 in win_conditions:#check win
        if board[index1] == board[index2] == board[index3] and board[index1] != ' ':
            # if index1
            return "W"

    counter = 0 #check tie
    for i in board:
        if i != ' ':
            counter += 1
    if counter == 9:
        return "T"

def play_game():
    board_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    symbol_p1 = choose_symbol()
    print(f"\n{p1_name} Symbol is: {symbol_p1}")
    if symbol_p1 == 'X':
        symbol_p2 = 'O'
        player_turns = [True, False]
    else:
        symbol_p2 = 'X'
        player_turns = [False, True]

    while True:
        user_choise = pick_place(board_list, player_turns, symbol_p1, symbol_p2)
        if user_choise == "Win":
            print(f"\n{player_won} Has Won!")
            return True
        elif user_choise == "Tie":
            print("Its a Tie! No one earns a point!")
            return True

def start_game():
    print("Welcome to Tic Tac Toe!")
    choose_name()
    global game_score
    game_score = [0, 0]
    while True:
        finished_game = play_game()
        if finished_game:
            play_again = input("Do you want to play again? Y for yes, everything else for no: ").lower()
            if play_again != "y":
                break
    print(f"\nGame ended. Final Score:")
    print(f"{p1_name}: {game_score[0]} Points\n{p2_name}: {game_score[1]} Points")
    if game_score[0] > game_score[1]:
        print(f"\n{p1_name} is the Winner!")
    elif game_score[1] > game_score[0]:
        print(f"\n{p2_name} is the Winner!")
    else:
        print("\nTie! No one Won!")

def choose_symbol():
    player1_symbol = input(f"\n{p1_name}, Choose Symbol. X or O \nAny other input will choose your symbol at random: ").upper()
    if (player1_symbol == 'X') or (player1_symbol == 'O'):
        return player1_symbol
    else:
        random_num = random.randint(1,2)
        if random_num == 1:
            player1_symbol = 'X'
            return player1_symbol
        elif random_num == 2:
            player1_symbol = 'O'
            return player1_symbol

def choose_name():
    global p1_name
    global p2_name
    global man_v_machine
    p1_name = input("Player 1 Whats your Name? ")
    while True:
        try:
            man_v_machine = input("Would you like to play with another player or against the pc? P or PC only: ").upper()
            if man_v_machine == 'P':
                p2_name = input("Player 2 Whats your Name? ")
                break
            elif man_v_machine == 'PC':
                p2_name = "CPU"
                break
            else:
                raise Exception("Invalid Input")
        except Exception as e:
            print("\nAn error has occured!")
            print(f"{e}\n")

if __name__ == '__main__':
    start_game()

