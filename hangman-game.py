import random

def get_word(difficulty):
    words = {
        'easy': ['apple', 'ball', 'cat', 'dog', 'fish'],
        'medium': ['python', 'rocket', 'jungle', 'laptop', 'mobile'],
        'hard': ['elephant', 'avalanche', 'dictionary', 'university', 'javascript']
    }
    return random.choice(words[difficulty])

def display_hangman(attempts):
    stages = [
        """
           ----
           |  |
           |  O
           | /|\
           | / \\
           |
        """,
        """
           ----
           |  |
           |  O
           | /|\
           | / 
           |
        """,
        """
           ----
           |  |
           |  O
           | /|\
           | 
           |
        """,
        """
           ----
           |  |
           |  O
           | /|
           | 
           |
        """,
        """
           ----
           |  |
           |  O
           |  |
           | 
           |
        """,
        """
           ----
           |  |
           |  O
           |  
           | 
           |
        """,
        """
           ----
           |  |
           |  
           |  
           | 
           |
        """
    ]
    return stages[attempts]

def play_hangman():
    print("Welcome to Hangman! Choose a difficulty level: Easy, Medium, or Hard")
    difficulty = input("Enter difficulty: ").lower()
    while difficulty not in ['easy', 'medium', 'hard']:
        difficulty = input("Invalid choice! Enter Easy, Medium, or Hard: ").lower()
    
    word = get_word(difficulty)
    word_letters = set(word)
    guessed_letters = set()
    attempts = 6
    
    while attempts > 0 and word_letters:
        print(display_hangman(attempts))
        print("Guessed letters:", " ".join(guessed_letters))
        print("Word:", " ".join([letter if letter in guessed_letters else '_' for letter in word]))
        
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word_letters:
            word_letters.remove(guess)
            guessed_letters.add(guess)
        else:
            attempts -= 1
            guessed_letters.add(guess)
            print("Wrong guess!")
    
    if not word_letters:
        print("Congratulations! You guessed the word:", word)
    else:
        print(display_hangman(attempts))
        print("Game Over! The word was:", word)

if __name__ == "__main__":
    play_hangman()
