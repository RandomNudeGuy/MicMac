

def play_game():


def start_game():
    while True:
        finished_game = play_game()
        if finished_game:
            play_again = input("Do you want to play again? Y for yes, everything else for no").lower()
            if play_again != "y":
                break
    print("Game ended")



if __name__ == '__main__':
    start_game()