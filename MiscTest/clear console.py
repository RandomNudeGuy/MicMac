import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Example usage
print("This will be cleared soon!")
input("Press Enter to clear the console...")
clear_console()
print("Console cleared!")
