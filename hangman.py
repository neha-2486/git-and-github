import random

def selectword():
    words=['python','c++','challenge','hangman','programming','developer']
    return random.choice(words)

def display_word(word,guessed_letters):
    result=''.join(letter if letter in guessed_letters else '_' for letter in word)
    return result

def play_hangman():
    word=selectword()
    guessed_letters=set()
    total_attempts=5
    print("Welcome to the Hangman game: \n")
    
    while total_attempts>0:
        print(f"Current word is {display_word(word,guessed_letters)}.\n")
        print(f"Attempts remained are {total_attempts}.\n")
        user_guess=input("Guess a letter: ").lower()
        
        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Please enter a single letter n also a valid guess! ")
            continue
        
        if user_guess in guessed_letters:
            print("You have guessed the letter !")
            continue
        
        guessed_letters.add(user_guess)
        
        if user_guess in word:
            print("You guess it right! ")
            
        else:
            print("You guess it wrong! ")
            total_attempts -= 1
            
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations you have guessed the word {word}")
            break
        
    # user_input=input("Do you wants to play again yes/no .")
    # if user_input.lower()!='yes':
    #     print("<--------Exit-------->")
    #     print("Thanks for playing😊")
        
           
    else:
        print(f"\nGame over! The word is {word}")
    
    
        
play_hangman()
        
    
    