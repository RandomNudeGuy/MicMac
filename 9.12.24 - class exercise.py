



if __name__ == '__main__':
    end = None
    while True:
        if end == 0:
            break
        else:
            menu = input("Which game would you like to play? Blackjack, Memory Game, or Roulette? :").lower()
            fullname = input("Whats your full name?").lower()
            print("Welcome to the game " + str(menu) + str(fullname))
            while True:
                end = int(input("Would you like to keep playing? 0 = end game and program \n"
                            "1 = end game and return to main menu\n"
                            "everything else will play again"))
                if end == 0:
                    break

                elif end == -1:
                    break



