import random

def card_check(first_card, second_card):
    if cards[first_card] == cards[second_card] and cards[first_card] not in found_cards and cards[second_card] not in found_cards:
        print(f"Correct! Both were {cards[first_card]} and {cards[second_card]}")
        card_location(guessed_cards, cards, X_list)
        found_cards.append(cards[first_card])
        found_cards.append(cards[second_card])
    elif cards[first_card] in found_cards or cards[second_card] in found_cards:
        print("Try again! One of the cards was already found!")
    else:
        print(f"Try again! They were {cards[first_card]} and {cards[second_card]}")


def check_first_card(index):
    if 0 <= index <= len(cards) - 1:
        return True
    else:
        print(f"Choose a number between 0 and {len(cards) - 1}")
        return False

def check_second_card(index):
    if 0 <= index <= len(cards) - 1:
        return True
    else:
        print(f"Choose a number between 0 and {len(cards) - 1}")
        return False


def card_location(guessed_cards, cards, X_list):
    for i in cards:
        for x in guessed_cards:
            if i == cards[x]:
                X_list[x] = i + " "


if __name__ == '__main__':
    quit = False
    while quit == False:
        cards = ["A", "A", "B", "B", "C", "C", "D", "D", "E", "E", "F", "F"]

        found_cards = []

        cards_length = len(cards)
        empty_space = "X "
        X_list = []
        for i in range(cards_length):
            X_list.append(empty_space)

        restart = False
        main_menu = str(input("Would you like to play? y/n ").lower())
        if main_menu == "y":
            random.shuffle(cards)
            while True:
                guessed_cards = []
                print(*X_list)
                first_choise = input("First card: ('Q' will Quit the game. 'R' Will restart it )").lower()
                if first_choise.isdigit():
                    first_choise = int(first_choise)
                    second_choise = int(input("Second card: "))
                    if first_choise != second_choise:
                        if 0 <= first_choise <= len(cards) - 1 and 0 <= second_choise <= len(cards) - 1:
                            guessed_cards.append(first_choise)
                            guessed_cards.append(second_choise)
                            card_check(first_choise, second_choise)
                        else:
                            print("Make sure the card is in range!")
                    else:
                        print("You cant guess the same card twice")
                elif first_choise == "q":
                    quit = True
                    break
                elif first_choise == "r":
                    break
    print("Goodbye!")