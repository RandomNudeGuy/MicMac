import random


def prepare_deck():
    cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F']
    random.shuffle(cards)
    return cards


def print_board(cards, correct_guesses, previse_guesses):
    print("\nBoard:")
    for i, card in enumerate(cards):
        if i in correct_guesses:
            print(f"[{card}]", end=" ")
        elif i in previse_guesses:
            print(f"[{card}]", end=" ")
        else:
            print(f"[ ]", end=" ")
        if(i + 1) % 4 == 0:
            print()


def guess_pair(cards, correct_guesses):
    previse_guesses = []
    print_board(cards, correct_guesses, previse_guesses)

    guess1 = guess_card(correct_guesses, previse_guesses)
    if guess1 == 'R':
        return 'R'

    previse_guesses.append(guess1)
    print_board(cards, correct_guesses, previse_guesses)

    guess2 = guess_card(correct_guesses, previse_guesses)
    if guess2 == 'R':
        return 'R'
    previse_guesses.append(guess2)
    print_board(cards, correct_guesses, previse_guesses)

    if cards[guess1] == cards[guess2]:
        print("\nYou have found a pair!")
        correct_guesses.append(guess1)
        correct_guesses.append(guess2)
    else:
        print("\nNo pair :(")

    return correct_guesses


def guess_card(correct_guesses, previse_guesses):
    while True:
        try:
            guess = input("\nEnter the index of your guessed card (0-11) or 'R' for restart")
            if guess == 'R':
                return guess
            guess = int(guess)
            if guess < 0 or guess > 11 or guess in correct_guesses or guess in previse_guesses:
                raise Exception("Invalid index")
            else:
                return guess
        except Exception as e:
            print("\nOops! Invalid index. Try again...")



def play_game():
    print("\nWelcome to the memory game!")
    cards = prepare_deck()
    correct_guesses = []

    while len(correct_guesses) < len(cards):
        user_selection = guess_pair(cards, correct_guesses)
        if user_selection == 'R':
            return False

    print("\nCongratulations! you won the game!")
    return True



def start_game():
    while True:
        won_game = play_game()
        if won_game:
            play_again = input("Do you want to play again? press Y for yes and anything else for no")
            if not play_again == "Y":
                break
    print("Game ended")


if __name__ == '__main__':
    start_game()