# Hangman CLI Game

A clean, interactive command-line implementation of the classic **Hangman** word-guessing game built with Python. Load words dynamically from custom text files, test your vocabulary, and track your progress through visual ASCII art representations.

---

## 📸 Overview

The game picks a secret word from a user-supplied text file based on a target index. Players guess letters one by one to reveal the hidden word before running out of attempts.

```text
            Welcome to the game Hangman
              _    _                                         
             | |  | |                                        
             | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
             |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
             | |  | | (_| | | | | (_| | | | | | | (_| | | | |
             |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                  __/ |                      
                                 |___/                       

```

---

## ✨ Features

* 🎯 **Dynamic Word Selection:** Reads words directly from external text files using 1-based indexing (with automatic index wrap-around).
* 🎨 **ASCII Visual Progress:** Displays detailed stage-by-stage ASCII visual hangman graphics for each incorrect guess.
* 🛡️ **Robust Input Validation:** Automatically handles invalid characters, multi-letter inputs, and duplicate guesses without penalty.
* 🔄 **Replayability:** Play multiple rounds consecutively without restarting the application.
* ⚡ **Zero External Dependencies:** Built entirely with Python's standard library modules (`os`).

---

## 🚀 Getting Started

### Prerequisites

* Python **3.6** or higher installed on your system.

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/hangman-cli.git
cd hangman-cli

```


2. **Prepare a words file:**
Create a plain text file (e.g., `words.txt`) in your project directory containing space-separated words:
```text
python developer algorithm terminal hangman computer programming

```



### Running the Game

Execute the main Python file:

```bash
python main.py

```

---

## 🎮 How to Play

1. **Enter File Path:** When prompted, enter the relative or absolute path to your word list file (e.g., `words.txt`).
2. **Enter Index:** Provide a positive integer index to select a secret word from the list.
3. **Guess Letters:** Type a single letter and press `Enter`.
* **Correct Guess:** Reveals the letter's position(s) in the secret word.
* **Incorrect Guess:** Increments your attempt counter and advances the Hangman ASCII drawing.
* **Invalid/Duplicate Input:** Shows an error marker (`X`) and lists previously tried letters.


4. **Win/Loss Condition:** Guess the full word within **6 incorrect attempts** to win!

---

## 📁 Code Architecture

| Function | Description |
| --- | --- |
| `welcome_screen()` | Prints the initial welcome banner in ASCII art. |
| `choose_word(file_path, index)` | Extracts a specific word from the text file according to the given index. |
| `check_valid_input(letter, old_letters)` | Validates whether an input is a single alphabetic, previously unguessed letter. |
| `try_update_letter_guessed(...)` | Handles input updates and outputs historic guesses if invalid. |
| `show_hidden_word(...)` | Formats and prints the current status of guessed vs. hidden letters (`_`). |
| `print_hangman(num_of_tries, photos)` | Displays the current visual hangman state based on wrong attempts. |
| `check_win(secret_word, old_letters)` | Evaluates whether all letters in the secret word have been uncovered. |

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
