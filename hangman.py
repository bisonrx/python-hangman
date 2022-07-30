'''Importing the random and time libraries:'''

import random
import time
# Initial Steps to invite in the game:
print("\nWelcome to Hangman game by DataFlair\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)

var = time.asctime( time.localtime(time.time()) )
print(var)
'''
Code Explanation:
Import random: This is used to randomly choose an item from a list [] or basically a sequence.
Import time: This module is used to import the actual time from your pc to use in the program.
Time.sleep(): This is used to halt the execution of the program for a few seconds.
It is a fun way to put the user of the game in short suspense.
'''

'''2. Define the main function:'''
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game =""

'''
Code Explanation:
We define the main function that initializes the arguments: global count, global display, 
global word, global already_guessed, global length and global play_game. 
They can be used further in other functions too depending on how we want to call them.
Words_to_guess: Contains all the Hangman words we want the user to guess in the game.
Word: we use the random module in this variable to randomly choose the word from words_to_guess in the game.
Length: len() helps us to get the length of the string.
Count: is initialized to zero and would increment in the further code.
Display: This draws a line for us according to the length of the word to guess.
Already_guessed: This would contain the string indices of the correctly guessed words.
'''

''' 3. Develop a loop to execute the game again: '''

# A loop to re-execute the game when the first round ends:
def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()

'''
Code Explanation:
Play_loop: This function takes in the argument of play_game.
Play_game: We use this argument to either continue the game after it is played once or 
end it according to what the user suggests.
While loop is used to execute the play_game argument. 
It takes the parameter, y=yes and n=no. If the user gives an input of something else other than y/n,
it asks the question again for the appropriate answer. If the user inputs “y”,
the game restarts, otherwise the game ends.
'''

''' 4. Initialize conditions for hangman game: '''
# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()

'''
Code Explanation:
We call all the arguments again under the hangman() function.
Limit: It is the maximum guesses we provide to the user to guess a particular word.
Guess: Takes the input from the user for the guessed letter.
Guess.strip() removes the letter from the given word.
If loop checks that if no input is given, or two letters are given at once, or a number is entered as an input,
it tells the user about the invalid input and executes hangman again.
'''

''' 5. The rest of the whole hangman program combined together: '''

    elif guess in word:
         already_guessed.extend([guess])
         index = word.find(guess)
         word = word[:index] + "_" + word[index + 1:]
         display = display[:index] + guess + display[index + 1:]
         print(display + "\n")
    elif guess in already_guessed:
         print("Try another letter.\n")
    else:
        count += 1
        if count == 1:
                time.sleep(1)
                print("   _____ \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
            elif count == 2:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
            elif count == 3:
               time.sleep(1)
               print("   _____ \n"
                     "  |     | \n"
                     "  |     |\n"
                     "  |     | \n"
                     "  |      \n"
                     "  |      \n"
                     "  |      \n"
                     "__|__\n")
               print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
            elif count == 4:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
            elif count == 5:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\ \n"
                      "  |    / \ \n"
                      "__|__\n")
                print("Wrong guess. You are hanged!!!\n")
                print("The word was:",already_guessed,word)
                play_loop()
        if word == '_' * length:
            print("Congrats! You have guessed the word correctly!")
            play_loop()
        elif count != limit:
            hangman()
    main()
    hangman()

'''
Code Explanation:

If the letter is correctly guessed, index searches for that letter in the word.
Display adds that letter in the given space according to its index or where it belongs in the given word.
If we have already guessed the correct letter before and we guess it again, 
It tells the user to try again and does not lessen any chances.
If the user guessed the wrong letter, the hangman starts to appear which also tells us how many guesses are left.
Count was initialized to zero and so with every wrong guess its value increases with one.
Limit is set to 5 and so (limit- count) is the guesses left for the user with every wrong input.
If it reaches the limit, the game ends, showing the right guesses (if any) and the word that was supposed to be guessed.
If the word is guessed correctly, matching the length of the display argument, the user has won the game.
Play_loop asks the user to play the game again or exit.
Main() and hangman() would start again if the play_loop executes to yes.
'''