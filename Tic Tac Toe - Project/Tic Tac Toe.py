import random

def switch_players(turn, is_win_or_tie):
    if is_win_or_tie == "W":
        return turn
    else:
        turn[0], turn[1] = turn[1], turn[0]
        return turn

def check_win_or_tie(is_win_or_tie, player_turn, board):
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
    elif is_win_or_tie == 0:
        return "NoWin"

def condition_win_or_tie(board):
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
            if board[index1] == 'X':
                mark = 'X̶'
                board[index1] = board[index2] = board[index3] = mark
            else:
                mark = 'O̶'
                board[index1] = board[index2] = board[index3] = mark
            return "W"

    counter = 0 #check tie
    for i in board:
        if i != ' ':
            counter += 1
    if counter == 9:
        return "T"
    return 0

def cpu_choice(board):
    while True:
        index_random = random.randint(1,9)
        for index, value in enumerate(board):
            if (index + 1) == index_random and value == ' ':
                return index_random - 1

def print_board(board):
    print("\nBoard:")
    for index, value in enumerate(board):
            print(f"[{value}]", end=" ")
            if (index + 1) % 3 == 0:
                print()

def pick_place(board, turn, P1, P2):
    game_status = "NoWin"
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
                if (man_v_machine == 'PC') and (turn == [False, True]):
                    board[cpu_choice(board)] = P2
                    is_win_or_tie = condition_win_or_tie(board)
                    break
                try:
                    print(f"\nTurn is: {player_turn}")
                    chosen_index = input("Choose a place 1-9\n'Q' to quit: ").upper()
                    if chosen_index.isdigit():
                        chosen_index_int = int(chosen_index)
                        chosen_index_int -= 1
                    elif chosen_index == "Q":
                        return "Q"
                    else:
                        raise Exception("Make sure to only give numbers between 1 - 9!")
                    if 1 <= chosen_index_int + 1 <= 9:
                        break
                    else:
                        raise Exception("Make sure to only give numbers between 1 - 9!")
                except Exception as e:
                    print("\nAn error has occurred!")
                    print("\nMake sure to only give numbers between 1 - 9!")
            if (man_v_machine == 'PC') and (turn == [False, True]):
                game_status = check_win_or_tie(is_win_or_tie, player_turn, board)
                turn = switch_players(turn, is_win_or_tie)
                return game_status
            else:
                for index, value in enumerate(board):
                    if index == chosen_index_int and value == ' ':
                        if player_turn == p1_name:
                            board[index] = P1
                            is_win_or_tie = condition_win_or_tie(board)
                            turn = switch_players(turn, is_win_or_tie)
                        elif player_turn == p2_name:
                            board[index] = P2
                            is_win_or_tie = condition_win_or_tie(board)
                            turn = switch_players(turn, is_win_or_tie)
                        game_status = check_win_or_tie(is_win_or_tie, player_turn, board)
                    elif index == chosen_index_int and value != ' ':
                        raise Exception("Place is already taken!")
        except Exception as e:
            print("\nAn error has occurred!")
            print(e)
            print()
        if game_status != "NoWin":
            return game_status

def choose_symbol():
    player1_symbol = input(f"\n{p1_name}, Choose Symbol. X or O \nAny other input will choose your symbol at random: ").upper()
    if (player1_symbol == 'X') or (player1_symbol == 'O'):
        return player1_symbol
    else:
        if random.randint(1,2) == 1:
            player1_symbol = 'X'
        else:
            player1_symbol = 'O'
        print("\nInvalid input. A symbol has been chosen for you.")
        return player1_symbol

def play_game():
    board_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] #the board
    symbol_p1 = choose_symbol()
    print(f"\n{p1_name}'s Symbol is: {symbol_p1}")
    if symbol_p1 == 'X':
        symbol_p2 = 'O'
        player_turns = [True, False]
    else:
        symbol_p2 = 'X'
        player_turns = [False, True]

    while True:
        user_choise = pick_place(board_list, player_turns, symbol_p1, symbol_p2)
        if user_choise == "Win":
            print(f"\n{player_won} has Won!")
            return True
        elif user_choise == "Tie":
            print("It's a Tie! No one earns a point!")
            return True
        elif user_choise == "Q":
            return True

def choose_name():
    global p1_name
    global p2_name
    global man_v_machine
    while True: #name input with checks if letters only
        try:
            p1_name = input("\nPlayer 1 what's your Name? ")
            if not p1_name.isalpha():
                raise Exception("Make sure the name consists of letters only!")
            else:
                break
        except Exception as e:
            print("\nAn error has occurred!")
            print(f"{e}\n")
    print(f"Hey {p1_name}!\n")
    while True:
        valid_p2_name = False
        try:
            man_v_machine = input(f"Would you like to play with another player or against the pc?\nInput 'P' for player or 'PC' only: ").upper()
            if man_v_machine == 'P':
                while True:
                    p2_name = input("\nPlayer 2 what's your Name? ")
                    try:
                        valid_p2_name = False
                        if p2_name.isalpha() and p2_name != p1_name:
                            valid_p2_name = True
                            break
                        else:
                            raise
                    except:
                        print("Make sure the name is different from Player 1's name, and consists of letters only!")
            elif man_v_machine == 'PC':#sets player 1 to play against the PC
                p2_name = "CPU"
                break
            else:
                raise Exception("Invalid Input")
        except Exception as e:
            print("\nAn error has occurred!")
            print(f"{e}\n")
        if valid_p2_name:
            break

def start_game():
    print("Welcome to Tic Tac Toe!")
    choose_name() #name choice
    global game_score
    game_score = [0, 0]
    while True:
        finished_game = play_game()
        if finished_game:#checks if game is finished or not
            play_again = input("\nDo you want to play again? Y for yes, everything else for no: ").lower()
            if play_again != "y":
                break
    print(f"\nGame ended. Final score:")
    print(f"{p1_name}: {game_score[0]} Points\n{p2_name}: {game_score[1]} Points")
    if game_score[0] > game_score[1]:
        print(f"\n{p1_name} is the winner!")
    elif game_score[1] > game_score[0]:
        print(f"\n{p2_name} is the winner!")
    else:
        print("\nTie! No one won!")

if __name__ == '__main__':
    start_game()
