import os.path
from os import path

def welcome_screen():
    """Print welcome screen with HANGMAN_ASCII_ART
    :return: None"""
    HANGMAN_ASCII_ART = """
            Welcome to the game Hangman
              _    _                                         
             | |  | |                                        
             | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
             |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
             | |  | | (_| | | | | (_| | | | | | | (_| | | | |
             |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                  __/ |                      
                                 |___/
            """
    print(HANGMAN_ASCII_ART)
def choose_word(file_path, index):
    """Picks one word from a list of words, read from a file, according to a given index in the list
    :param: file_path: the path of the file that contains a word list
    :param: index: the position of the word to be picked
    :type: file_path: string
    :type: index: int
    :return: The picked word
    :rtype: String
    """
    file = open(file_path, 'r')
    str_file = file.read()
    list_of_words = str_file.split(' ')
    num_of_words = len(set(list_of_words))
    while index > len(list_of_words):
        index = index - len(list_of_words)
    word = list_of_words[index - 1]
    file.close()
    return word
def hangman(secret_word):
    """create a list of space-separated underscores of the selected word
    :param: secret_word: the selected word
    :type: secret_word: string
    :return: list of space-separated underscores of the selected word
    :rtype: String
    """
    display_word = secret_word.zfill(len(secret_word) * 2)
    display_word = display_word[0:len(secret_word)]
    display_word = display_word.replace('0', '_')
    return " ".join(display_word)
def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks the validation of input (character)
    :param: letter_guessed: user's guess
    :type: string
    :return: Whether the input was valid
    :rtype: boolean
    """
    if letter_guessed in old_letters_guessed or letter_guessed.lower() in old_letters_guessed:
        return False
    elif len(letter_guessed) == 1 and letter_guessed.isalpha():
        return True
    else:
        return False
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Checks validation of user’s input (as in previous task).
    if so, adds it to "old_letters_guessed" and returns True. Otherwise returns
    False.
    :param letter_guessed: user’s input
    :param old_letters_guessed: previous (valid) inputs
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: True if input is valid, False if not.
    :rtype: boolean
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed += letter_guessed.lower()
        return True
    else:
        print('X')
        print(" -> ".join(sorted(old_letters_guessed)))
        return False
def show_hidden_word(secret_word, old_letters_guessed):
    """Displays guessed letters in the secret word, and '_' for letters that were
    not guessed yet
    :param: secret_word: the word to be guessed
    :param: old_letters_guessed: the letters that were guested (user's input)
    :type secret_word: list
    :type old_letters_guessed: list
    :return: the updated list, with all guessed letters
    :rtype: list
    """
    new_str = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            new_str = new_str + letter + ' '
        else:
            new_str = new_str + "_ "
    return new_str[:-1]
def print_hangman(num_of_tries, HANGMAN_PHOTOS):
    """Prints the hangman according to the number of tries
    :param: num_of_tries: number of tries
    :param: HANGMAN_PHOTOS: All situations of the hangman
    :type num_of_tries: int
    :type HANGMAN_PHOTOS: String
    :return: None
    """
    print(HANGMAN_PHOTOS["picture " + str(num_of_tries)] + "\n")
def check_win(secret_word, old_letters_guessed):
    """Checks if the whole secret word was guested correctly
    :param: secret_word: the word to be guessed
    :param: old_letters_guessed: the letters that were guested (user's input)
    :type secret_word: list
    :type old_letters_guessed: list
    :return: True if the secret word was guessed, False if not
    :rtype: boolean
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True
def letter_guessed_in_secret_word(letter_guessed, secret_word, old_letters_guessed):
    """Checks if the guessed letter is in the word
    :param: letter_guessed: the letter guessed
    :param: secret_word: the word to be guessed
    :param: old_letters_guessed: the letters that were guested
    :type letter_guessed: string
    :type secret_word: list
    :type old_letters_guessed: list
    :return: True if the guessed letter is in the word, False if not
    :rtype: boolean
    """
    old_letters_guessed += letter_guessed.lower()
    if letter_guessed.lower() in secret_word:
        return True
    return False
def main():

    HANGMAN_PHOTOS = {
        "picture 0": "x-------x",
        "picture 1": """x-------x
|
|
|
|
|""",
        "picture 2": """x-------x
|       |
|       0
|
|
|""",
        "picture 3": """x-------x
|       |
|       0
|       |
|
|""",
        "picture 4": """x-------x
|       |
|       0
|      /|\\
|
|""",
        "picture 5": """x-------x
|       |
|       0
|      /|\\
|      /
|""",
        "picture 6": """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""}
    MAX_TRIES = 6
    want_to_play = "yes"

    while want_to_play != "no":  # The game runs as long as you don't explicitly write that you want to stop
        old_letters_guessed = []
        num_of_tries = 0
        welcome_screen()
        path_file = input("Enter path file: ")
        while not path.exists(path_file):
            path_file = input("Path file does not exist. Enter path file: ")
        index = input("Enter index: ")
        while index == '0' or index.isalpha():
            index = input("An index can only be an integer greater than zero. Enter index: ")
        index = int(index)
        file = open(path_file, 'r')
        if len(file.read()) == 0:
            continue
        secret_word = choose_word(path_file, index)
        print("\nLet's start!\n")
        print_hangman(0, HANGMAN_PHOTOS)
        print(hangman(secret_word))
        while not check_win(secret_word, old_letters_guessed) and num_of_tries < MAX_TRIES:  # The game runs as long
            # as the player has not won or lost
            letter_guessed = input("Guess a letter: ")
            while not check_valid_input(letter_guessed, old_letters_guessed):
                try_update_letter_guessed(letter_guessed, old_letters_guessed)
                letter_guessed = input("Guess a letter: ")
            if letter_guessed_in_secret_word(letter_guessed, secret_word, old_letters_guessed):
                print(show_hidden_word(secret_word, old_letters_guessed))
            else:
                print(":(")
                num_of_tries += 1
                print_hangman(num_of_tries, HANGMAN_PHOTOS)
                print(show_hidden_word(secret_word, old_letters_guessed))
        if num_of_tries == MAX_TRIES:
            print("LOSE")
        else:
            print("WIN")
        want_to_play = input("Want to play again? (yes / no): ")
        while want_to_play != "yes" and want_to_play != "no":
            want_to_play = input("Enter yes or no: ")
    print("\nThank you for choosing Gordon!")


if __name__ == "__main__":
    main()
