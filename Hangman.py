import random


class Hangman:
    def start_game(self):
        list_of_words = ['abruptly', 'beekeeper', 'caliph', 'daiquiri', 'espionage', 'fishhook', 'gabby']
        result = random.choice(list_of_words)
        number_of_guesses = len(result) + 3
        player_guesses = ''
        while number_of_guesses > 0:
            count = 0
            for letter in result:
                if letter in player_guesses:
                    print(letter, end="")
                else:
                    print("_", end="")

            guess = input("Please input a character:")
            player_guesses += guess

            if guess not in result:
                number_of_guesses -= 1
                print(f"Wrong guess, number of turns left {number_of_guesses}")

            for letter in player_guesses:
                if letter in result:
                    count += 1

            if count == len(result):
                print("Correct word, you win")
                break



game = Hangman()
game.start_game()